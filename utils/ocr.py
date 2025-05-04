import pytesseract
from pdf2image import convert_from_path
from pdfminer.high_level import extract_text as extract_pdf_text
import os

def extract_text_with_ocr(pdf_path):
   
    try:
        text = extract_pdf_text(pdf_path)
        if text and text.strip():
            print(f"[INFO] Extracted embedded text from {pdf_path}")
            return text.strip()
    except Exception as e:
        print(f"[WARNING] Failed direct text extraction: {e}")

   
    print(f"[INFO] Falling back to OCR for {pdf_path}")
    try:
        pages = convert_from_path(pdf_path, dpi=300)
        full_text = []

        for i, page in enumerate(pages):
            ocr_text = pytesseract.image_to_string(page, lang='san+eng')
            if ocr_text.strip():
                full_text.append(ocr_text.strip())
            else:
                print(f"[DEBUG] Skipped blank OCR page {i+1}")

        return "\n\n".join(full_text).strip()
    except Exception as e:
        print(f"[ERROR] OCR failed for {pdf_path}: {e}")
        return ""
