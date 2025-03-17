from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # อนุญาต CORS ให้กับทุก origin

@app.route('/text-upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img = Image.open(file.stream)
        text = pytesseract.image_to_string(img)  # ใช้ pytesseract ตรงๆ ไม่ต้องกำหนด path
        return jsonify({'text': text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # เปลี่ยนเป็น 5001
