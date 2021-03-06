import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template, current_app, jsonify
from werkzeug.utils import secure_filename
from pathlib import Path

BASE_URL = 'foo'

PARENT_DIRECTORY = Path(__file__).parent.absolute()
UPLOAD_FOLDER = PARENT_DIRECTORY / 'uploads'
UPLOAD_FOLDER.mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {'wav'}

app = Flask(__name__, static_url_path="")
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = str(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        print('filename ' + file.filename)
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            filename = 'podcast.wav'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify(success=True)

    #return render_template('controller.html', base_url=BASE_URL)
    return current_app.send_static_file('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)