from flask import Flask, request, jsonify
import spacy
from flask_cors import CORS

nlp = spacy.load("text_model")
app = Flask(__name__)
CORS(app)

# ฟังก์ชันสำหรับดึงสถานที่จากข้อความ
def extract_locations(input_text):
    doc = nlp(input_text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "LOCATION"]
    return locations

@app.route("/")
def index():
    return jsonify({"message": "Location API is running"}), 200  # เปลี่ยนจาก redirect เป็นข้อความ

@app.route("/extract_locations", methods=["POST"])
def extract_locations_from_request():
    data = request.get_json()
    input_message = data.get("message")
    if not input_message:
        return jsonify({"error": "Message is required"}), 400

    locations = extract_locations(input_message)
    return jsonify({"locations": locations})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)
