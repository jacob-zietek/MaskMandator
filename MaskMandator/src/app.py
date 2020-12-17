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

#@app.route('/upload', methods=['GET', 'POST'])
#def upload_file(file):
#    if request.method == 'POST':
#        # check if the post request has the file part
#        if 'file' not in request.files:
#            flash('No file part')
#            return redirect(request.url)
#        file = request.files['file']
#        # if user does not select file, browser also
#        # submit an empty part without filename
#        if file.filename == '':
#            flash('No selected file')
#            return redirect(request.url)
#        if file and allowed_file(file.filename):
#            filename = file.filename
#            file.save(os.path.join(app.config['uploaded.png'], filename))
#            context = {'return_string', processUserInput.main()}
#            return render_template('index.html', context=context)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
if __name__ == '__main__':
   app.run(debug=True)


