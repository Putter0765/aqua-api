#!/bin/bash
pip install -r requirements.txt  # ติดตั้ง dependencies
python -m spacy download en_core_web_sm  # ดาวน์โหลดโมเดล Spacy
python location-api.py &  # รัน location-api.py
python name-api.py &  # รัน name-api.py
python ocr-api.py  # รัน OCR API (ตัวสุดท้ายไม่ต้อง &)
