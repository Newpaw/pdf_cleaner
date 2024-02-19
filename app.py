from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import os
import pdf_cleaner
import logging
from uuid import uuid4
from threading import Timer

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ujistěte se, že složky existují
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def delete_files(input_path, output_path):
    """Funkce pro mazání souborů po uplynutí časového limitu."""
    try:
        os.remove(input_path)
        os.remove(output_path)
        logging.info(f"Deleted: {input_path} and {output_path}")
    except Exception as e:
        logging.error(f"Error deleting files: {e}")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and file.filename.endswith('.pdf'):
            unique_id = str(uuid4())
            secure_name = secure_filename(file.filename)
            original_name_without_ext = os.path.splitext(secure_name)[0]
            output_filename = f"{original_name_without_ext}_{unique_id}.pdf"
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{unique_id}_{secure_name}")
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
            file.save(input_path)
            pdf_cleaner.pdf_to_images_and_back(input_path, output_path)
            Timer(3600, delete_files, args=[input_path, output_path]).start()
            return send_file(output_path, as_attachment=True, download_name=output_filename)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new PDF</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
