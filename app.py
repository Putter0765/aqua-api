import os
from flask import Flask, request, jsonify
import spacy
from PIL import Image
import pytesseract
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# โหลดโมเดล NLP
nlp = spacy.load("text_model")

# API สำหรับดึงชื่อจากข้อความ
@app.route("/extract_names", methods=["POST"])
def extract_names():
    data = request.get_json()
    input_message = data.get("message")
    if not input_message:
        return jsonify({"error": "Message is required"}), 400

    doc = nlp(input_message)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    return jsonify({"names": names})

# API สำหรับดึงสถานที่จากข้อความ
@app.route("/extract_locations", methods=["POST"])
def extract_locations():
    data = request.get_json()
    input_message = data.get("message")
    if not input_message:
        return jsonify({"error": "Message is required"}), 400

    doc = nlp(input_message)
    locations = [ent.text for ent in doc.ents if ent.label_ == "LOCATION"]
    return jsonify({"locations": locations})

# API สำหรับ OCR (ดึงข้อความจากรูปภาพ)
@app.route('/text-upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img = Image.open(file.stream)
        text = pytesseract.image_to_string(img)
        return jsonify({'text': text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# หน้าแรกของ API
@app.route("/")
def index():
    return jsonify({"message": "API is running"}), 200

# รันแค่พอร์ตเดียว (ให้ Render กำหนดพอร์ต)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
