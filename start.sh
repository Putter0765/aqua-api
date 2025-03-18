#!/bin/ba

# ติดตั้ง dependencies
pip install -r requirements.txt  

# ดาวน์โหลดโมเดล Spacy
python -m spacy download en_core_web_sm  

# รัน API หลัก (OCR + NLP รวมกัน)
python app.py  
