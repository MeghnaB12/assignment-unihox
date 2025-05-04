import fitz  # PyMuPDF
from datetime import datetime

def parse_creation_date(date_str):
    """Parse PDF date string like 'D:20220101120000' into ISO 8601 date."""
    if date_str and date_str.startswith("D:"):
        try:
            dt = datetime.strptime(date_str[2:16], "%Y%m%d%H%M%S")
            return dt.date().isoformat()  
        except Exception:
            pass
    return ""

def extract_metadata(file_path):
    try:
        doc = fitz.open(file_path)
        meta = doc.metadata or {}
        
        return {
            "title": meta.get("title", "").strip(),
            "authors": [meta["author"].strip()] if meta.get("author") else [],
            "pub_year": parse_creation_date(meta.get("creationDate", "")),
            "language": "Sanskrit",  
            "source_url": "",        
            "scraped_at": datetime.utcnow().isoformat() + "Z"
        }
    except Exception as e:
        print(f"[ERROR] Metadata extraction failed for {file_path}: {e}")
        return {
            "title": "",
            "authors": [],
            "pub_year": "",
            "language": "Sanskrit",
            "source_url": "",
            "scraped_at": datetime.utcnow().isoformat() + "Z"
        }
