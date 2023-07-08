from flask import Flask, request, jsonify
import PyPDF2,pdb
import pytesseract
from PIL import Image
from pdftotext.pdftotext import pdf_page_to_text
# from pdftotext.pdf_to_text import pdf_to_text as pdf_page_to_text
import os
import random
from cleanup import cleanup_thread
cleanup_thread.start()
try:
    os.mkdir("tmp")
except:pass
app = Flask(__name__)

pdf_files = {}  # Dictionary to store uploaded PDF files

@app.route('/upload_file', methods=['POST'])
def upload_file():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    
    # Check if the file has a PDF extension
    if file.filename.split('.')[-1].lower() != 'pdf':
        return jsonify({'error': 'Invalid file format, only PDF files are supported'}), 400

    # Generate a unique PDF ID
    # pdf_id = str(hash(file.read()))
    # Save the file to the dictionary with the PDF ID as the key
    pdfid = random.randint(10000,10000000000)
    file.save(f"tmp/{pdfid}.pdf")

    return jsonify({'pdf_id': pdfid}), 200

@app.route('/extract_text', methods=['GET'])
def extract_text():
    # Get the PDF ID from the request's query parameter
    pdf_id = request.args.get('pdf_id')

    # Check if the PDF ID is valid
    filename = f"tmp/{pdf_id}.pdf"
    if not os.path.isfile(filename):
        return jsonify({'error': 'file not exist please re-upload and try again'}), 400

   
    page_number = request.args.get('page', type=int)
    page_index =page_number -1
    pdf_reader = PyPDF2.PdfReader(filename)
    total_pages = len(pdf_reader.pages)
    try:
        extract_text = pdf_page_to_text(pdf_reader,page_index,filename)
        return jsonify({'page': f"{page_number} of {total_pages}", 'text': extract_text}), 200
    except IndexError:
        return jsonify({'page': f"{page_number} of {total_pages}", 'message': "out of index page not found"}), 200
if __name__ == '__main__':
    app.run()
