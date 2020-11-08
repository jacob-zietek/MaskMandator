import os
import sys
import predict
#whatever the program that will provide the image

from flask import Flask, render_template, request, redirect, send_from_directory, send_file
app = Flask(__name__)

@app.route('/')
def home():
    return rener_template('index.html')
    
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = reques.files('file')
        filename = f.filename
        if filename(filename.index("."):] == ".png":
            f.save('uploaded_file.png')


    
if __name__ == "__main__":
    app.run(debug=True)

predict.main()
#whatever the program that will provide the image





#import os
#import sys
#from flask import Flask, render_template, request, redirect, send_from_directory, send_file
#app = Flask(__name__)

#@app.route('/')
#def home():
#   return render_template('layout.html')
#if __name__ == '__main__': 
#   app.run(host='0.0.0.0',port='80')
#   app.run(debug=True)

