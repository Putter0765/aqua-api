#!/bin/bash
python -m spacy download en_core_web_sm  # ติดตั้ง Spacy Model
python location-api.py &  # รัน location-api.py
python name-api.py &  # รัน name-api.py
python ocr-api.py  # รัน OCR API (ตัวสุดท้ายไม่ต้อง &)
