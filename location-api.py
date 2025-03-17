from flask import Flask, render_template, request, jsonify
import spacy
from flask_cors import CORS

# โหลดโมเดลที่เทรนแล้ว (หรือโมเดลที่คุณฝึกมา)
nlp = spacy.load("text_model")
app = Flask(__name__)
CORS(app)  # อนุญาต CORS ให้กับทุก origin

# ฟังก์ชันสำหรับดึงสถานที่จากข้อความ
def extract_locations(input_text):
    doc = nlp(input_text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "LOCATION"]  # เปลี่ยนจาก 'PERSON' เป็น 'LOCATION'
    return locations

@app.route("/")
def index():
    return redirect("https://admin.takkitransport.com/test.php")

@app.route("/extract_locations", methods=["POST"])
def extract_locations_from_request():
    data = request.get_json()
    input_message = data.get("message")
    if not input_message:
        return jsonify({"error": "Message is required"}), 400

    locations = extract_locations(input_message)  # เปลี่ยนเป็นการเรียกฟังก์ชันสำหรับ 'LOCATION'
    return jsonify({"locations": locations})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)
