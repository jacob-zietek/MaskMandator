from flask import Flask, render_template, request, redirect, send_from_directory, send_file
import os
import time
import sys
import processUserInput
#whatever the program that will provide the image

app = Flask(__name__)



@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = reques.files('file')
        filename = f.filename
            if filename(filename.index("."):] == ".png":
                f.save('uploaded_file.png')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    processUserInput.main()