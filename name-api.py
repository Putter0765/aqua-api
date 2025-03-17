from flask import Flask, render_template, request, jsonify
import spacy


from flask_cors import CORS

# โหลดโมเดลที่เทรนแล้ว (หรือโมเดลภาษาอังกฤษทั่วไป)
nlp = spacy.load("text_model")
app = Flask(__name__)
CORS(app)  # อนุญาต CORS ให้กับทุก origin


# ฟังก์ชันสำหรับดึงชื่อจากข้อความ
def extract_names(input_text):
    doc = nlp(input_text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    return names

@app.route("/")
def index():
    return render_template("test.php")  # หน้าเว็บหลัก

@app.route("/extract_names", methods=["POST"])
def extract_names_from_request():
    data = request.get_json()
    input_message = data.get("message")
    if not input_message:
        return jsonify({"error": "Message is required"}), 400

    names = extract_names(input_message)
    # เว้นบรรทัดระหว่างชื่อ
    formatted_names = "\n".join(names)
    return jsonify({"names": formatted_names})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


