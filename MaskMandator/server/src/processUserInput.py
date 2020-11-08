#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 22:28:30 2020

@author: jacobzietek
"""

from API_KEYS import main as API_LIST

from cloudant import cloudant
from cloudant import cloudant_iam
import numpy as np

project_id, model_id, DB_USERNAME, DB_API_KEY = API_LIST()

from google.cloud import automl

import os

def isWearingMask(file_path):
    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = automl.AutoMlClient.model_path(
        project_id, "us-central1", model_id
    )

    # Read the file.
    with open(file_path, "rb") as content_file:
        content = content_file.read()

    image = automl.Image(image_bytes=content)
    payload = automl.ExamplePayload(image=image)

    # params is additional domain-specific parameters.
    # score_threshold is used to filter the result
    # https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictrequest
    params = {"score_threshold": "0.8"}

    request = automl.PredictRequest(
        name=model_full_id,
        payload=payload,
        params=params
    )
    response = prediction_client.predict(request=request)

    #print("Prediction results:")
    for result in response.payload:
        #print("Predicted class name: {}".format(result.display_name))
        #print("Predicted class score: {}".format(result.classification.score))
        return True if (result.display_name == "with_mask" and result.classification.score > 0.8) else False

def getName(idNumber): # Gets name of student
    
    name = ""
    
    with cloudant_iam(DB_USERNAME, DB_API_KEY) as client:

        student_id = idNumber

        my_database = client['purdue']
        my_doc = my_database[':'.join(("id", student_id))]
        name = my_doc['name']
        
    return name
        

def incrementInfringements(idNumber): # Incriments number of mask infringements a student has
    
    with cloudant_iam(DB_USERNAME, DB_API_KEY) as client:

        student_id = idNumber
            
        my_database = client['purdue']
        my_doc = my_database[':'.join(("id", student_id))]
        
        my_doc["num_infringes"] = my_doc["num_infringes"] + 1
        
        my_doc.save()
        
def getInfringements(idNumber): # Returns number of mask infringements a student has
    
    num_infringes = 0
    
    with cloudant_iam(DB_USERNAME, DB_API_KEY) as client:
        
        student_id = idNumber

        my_database = client['purdue']
        my_doc = my_database[':'.join(("id", student_id))]
        
        num_infringes = my_doc["num_infringes"]
        
    return num_infringes


def underlyingHealthCondition(idNumber): # Returns bool, true if student has underlying health condition

    health_condition = "no"

    with cloudant_iam(DB_USERNAME, DB_API_KEY) as client:
  
        student_id = idNumber

        my_database = client['purdue']
        my_doc = my_database[':'.join(("id", student_id))]
        
        health_condition = my_doc["underlying_health_condition"]
        
    return True if health_condition == "yes" else False


def read_qr(img_name):
     import cv2
     img = cv2.imread(img_name)     
     det = cv2.QRCodeDetector()
     return det.detectAndDecode(img)


def main():
    project_id, model_id, DB_USERNAME, DB_API_KEY = API_LIST()
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceAccountToken_GoogleVision.json'
    
    numStudents = 6
    
    idArray = np.linspace(1, numStudents, numStudents)
    
    
    file_path = "face.png"
    
    qr_file_path = "qrCode.png"
    
    #file_path = "/Users/jacobzietek/Documents/RPIHacks2020/bryan.png"
    #qr_file_path = "/Users/jacobzietek/Documents/RPIHacks2020/test1.png"
    
    wearingMark = isWearingMask(file_path)
    
    qrValue = read_qr(qr_file_path)[0]
    
    print(qrValue)
    
    if(float(qrValue) not in idArray or qrValue == ""):
        return("ID not found! Please retry.")
    
    if(getInfringements(qrValue) > 3):
        return("You have more than 3 infringements on your account. Please do not enter and talk to the main office.")
    
    if(underlyingHealthCondition(qrValue)):
        return("You have an underlying health condition! Please do not enter.")

    if(not wearingMark):
        incrementInfringements(qrValue)
        return("Please put on your mask! You have been penalized.")
        
    user_name = getName(qrValue)
    
    return("Access granted. Thank you, {}, and stay safe!".format(user_name))
        
    
    
print(main())