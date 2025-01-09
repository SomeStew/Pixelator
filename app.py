# app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Here you can add the code to process the image
        process_image(file_path)
        
        return jsonify({'message': 'File successfully uploaded'}), 200

def process_image(file_path):
    # Implement your image processing logic here
    print(f'Processing image: {file_path}')
    # For example, you could use OpenCV, PIL, etc. to process the image
    # Example: Process the image using OpenCV or PIL

if __name__ == '__main__':
    app.run(debug=True)
