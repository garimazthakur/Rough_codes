from flask import Flask
import os
import urllib.request
UPLOAD_FOLDER = '/home/softuvo/Garima/Flask Practice/Flask_practice/Learnings/images'
app = Flask(__name__)
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename


app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_files():

    return "." in filename and filename.rsplit('.',1)[1].lower()
@app.route("/")
def upload_form():
    return render_template('upload.html')
    








