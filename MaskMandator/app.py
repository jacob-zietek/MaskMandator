#import statements
import os
import sys
from flask import Flask, render_template, request, redirect, send_from_directory, send_file
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('layout.html')
if __name__ == '__main__': 
   app.run(host='0.0.0.0',port='80')
   app.run(debug=True)

