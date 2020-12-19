from flask import Flask, render_template, request, redirect, send_from_directory, send_file, url_for
import os
import time
import sys
import processUserInput
import flash
#whatever the program that will provide the image

ALLOWED_EXTENSIONS = {'png', 'jpg'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './'

@app.route('/')
def home():
   return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
if __name__ == '__main__':
   app.run(debug=True)


