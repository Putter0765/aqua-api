from flask import Flask, request, jsonify
import spacy
from flask_cors import CORS

nlp = spacy.load("text_model")
app = Flask(__name__)
CORS(app)

# ฟังก์ชันสำหรับดึงชื่อจากข้อความ
def extract_names(input_text):
    doc = nlp(input_text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    return names

@app.route("/")
def index():
    return jsonify({"message": "Name API is running"}), 200  # เปลี่ยนจาก redirect เป็นข้อความ

@app.route("/extract_names", methods=["POST"])
def extract_names_from_request():
    data = request.get_json()
    input_message = data.get("message")
    if not input_message:
        return jsonify({"error": "Message is required"}), 400

    names = extract_names(input_message)
    formatted_names = "\n".join(names)
    return jsonify({"names": formatted_names})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
