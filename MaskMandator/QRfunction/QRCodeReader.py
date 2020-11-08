#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:04:28 2020

@author: jacobzietek

pip install opencv-python
"""

def read_qr(img_name):
     import cv2
     img = cv2.imread(img_name)     
     det = cv2.QRCodeDetector()
     return det.detectAndDecode(img)
 
qr_code_value = read_qr("test22.png")

'''
import qrtools
qr = qrtools.QR()
qr.decode("test1.png")p
print(qr.data)
'''
'''
from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open('test1.png'))
print(data)
'''