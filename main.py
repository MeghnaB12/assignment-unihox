import os
import hashlib
from datetime import datetime
from utils.crawler import crawl_and_download
from utils.extractor import extract_metadata
from utils.ocr import extract_text_with_ocr
from utils.helpers import save_json, load_existing_checksums, save_checksums

TARGET_URLS = [
    
    "https://ayushportal.nic.in/default.aspx"
]


OUTPUT_DIR = "output/json_records"
CHECKSUM_FILE = "output/checksums.json"

def sha256sum(file_path):
    """Generate sha256 checksum for the given file."""
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def normalize_authors(authors):
    """Normalize author names by stripping spaces and capitalizing them."""
    return [author.strip().title() for author in authors] if authors else []

def main():
    
    existing_checksums = load_existing_checksums(CHECKSUM_FILE)

    for url in TARGET_URLS:
       
        pdf_paths = crawl_and_download(url)

        if not pdf_paths:
            print(f"[ERROR] No PDFs found or download failed for {url}")
            continue

        for pdf_path in pdf_paths:
            pdf_path = os.path.abspath(pdf_path)
            checksum = sha256sum(pdf_path)

            
            if checksum in existing_checksums:
                print(f"[SKIP] Unchanged PDF, skipping: {pdf_path}")
                continue

            print(f"[INFO] Processing PDF: {pdf_path}")
            metadata = extract_metadata(pdf_path)
            text = extract_text_with_ocr(pdf_path)

            # Build the structured record
            record = {
                "site": url.split('/')[2],
                "document_id": checksum,
                "title": metadata.get("title", "").strip(),
                "authors": normalize_authors(metadata.get("authors", [])),
                "pub_year": metadata.get("pub_year", ""),
                "language": metadata.get("language", "Sanskrit"),
                "download_url": metadata.get("source_url", url),
                "checksum": checksum,
                "scraped_at": datetime.utcnow().isoformat() + "Z",
                "content": text
            }

            # Save the JSON record
            save_json(record, output_dir=OUTPUT_DIR)

            # Add the checksum to the dictionary
            existing_checksums[checksum] = pdf_path

    # Save updated checksums to file
    save_checksums(existing_checksums, CHECKSUM_FILE)

if __name__ == "__main__":
    main()
