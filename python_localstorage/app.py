import os
from flask import Flask, request, render_template, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename



UPLOAD_FOLDER = 'files/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


files_list = os.listdir(path="./files")
data = [{ 
    'title': str(i),
    'text': str(i),
    'mobileText': str(i),
    'img': f'http://192.168.1.35:5000/uploads/{i}',
    'link': f'http://192.168.1.35:5000/uploads/{i}'
    } for i in files_list ]


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template('file.html', data=data)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

'''
@app.route('/api')
def api():
    
    return jsonify(data)
'''

if __name__ == '__main__':
	app.run(debug=True, host='192.168.1.35')