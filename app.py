# app.py
from flask import Flask, request, jsonify, send_file
import os
from pixelise import process_image  # Import the image-processing function

print("Flask app is starting...")
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Ensure the upload and processed folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file:
        # Save the uploaded file with its original name
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Generate a processed file name based on the input file name
        output_filename = f"processed_{filename}"
        output_path = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)

        # Process the image
        process_image(file_path, output_path, num_pixels=50)

        # Return the processed image
        return send_file(output_path, mimetype='image/jpeg', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)