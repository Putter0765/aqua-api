#!/bin/bash

# ติดตั้ง Tesseract OCR
apt-get update && apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev

# ติดตั้ง dependencies
pip install -r requirements.txt  

# ดาวน์โหลดโมเดล Spacy
python -m spacy download en_core_web_sm  

# รัน API หลัก (OCR + NLP รวมกัน)
python app.py  
