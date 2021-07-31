import os
import base64
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from test_ml import ml_softmax_test,cnn_test

UPLOAD_FOLDER = './pics'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    

    return render_template("index.html",count=1)

# WRITE ON A 32X32 CANVAS AND GIVE IMAGE TO THE PICKLE EXPORT TO GUESS WHAT NUMBER IT IS

@app.route("/test", methods=['GET', 'POST'])
def test():
     if request.method == 'POST':
         
        if 'file' not in request.values:
    
            flash('No file part')
            return redirect(request.url)

        file = request.values['file']

        #remove the begining of the file
        file = file.replace("data:image/png;base64,", "")
        
        convert_and_save(file)

        return str(cnn_test("imageToSave.png"))


def convert_and_save(b64_string):
    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))

if __name__ == "__main__":
    app.run(debug=True)