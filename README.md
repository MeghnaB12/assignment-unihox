# assignment-unihox

# Assignment UniHox

This repository contains a set of Python scripts for extracting metadata from PDFs, downloading files, performing OCR on PDFs without text, and saving the extracted data as structured JSON files. It uses libraries like `pytesseract`, `pdfminer`, and `requests` to provide a comprehensive solution for handling PDFs.

## Features

- **Crawl and Download PDFs**: Automatically download PDF files from web links.
- **Extract PDF Metadata**: Retrieve title, authors, creation date, and other metadata from PDF documents.
- **OCR Text Extraction**: Use Tesseract to perform OCR-based text extraction on PDFs without embedded text.
- **Save Data as JSON**: The extracted metadata and OCR text are saved in a structured JSON format.
- **Error Handling**: Includes error handling and logging for robust operation.
- **Checksums**: Ensures that already processed files are skipped to avoid redundancy.

## Installation

### 1. Clone the Repository

git clone https://github.com/MeghnaB12/assignment-unihox.git
cd assignment-unihox

### 2. Install Dependencies
Make sure you have Python 3.7+ installed. Then, install the required dependencies by running:
pip install -r requirements.txt

Dependencies:
pytesseract: OCR (Optical Character Recognition) for extracting text from images.
pdf2image: Converts PDF pages to images for OCR processing.
pdfminer.six: Extracts embedded text from PDFs.
requests: For making HTTP requests to download files.
beautifulsoup4: For scraping PDF links from web pages.
playwright: For automating web browsing and crawling pages.
hashlib: For generating checksums to track previously processed files.
os and pathlib: For handling file and directory paths.

### 3. Install Tesseract (for OCR)
Tesseract is required for OCR functionality. Install it on your system as follows:
For Windows:
Download and install Tesseract from Tesseract GitHub.
Add Tesseract’s installation path to your system’s PATH environment variable.
For macOS:
brew install tesseract
For Linux:
sudo apt install tesseract-ocr

Usage

Prepare the environment: Ensure all dependencies are installed and Tesseract is correctly set up on your system.
Run the Script:
Modify the script main.py to include your desired URLs in the TARGET_URLS list.
Run the script using the following command:
python main.py
The script will:
Crawl the target URLs and download the PDFs.
Extract metadata from each PDF.
If the PDF does not contain embedded text, OCR will be performed to extract text.
Save the metadata and OCR text as JSON files in the output/json_records directory.
Error Handling
The script includes basic error handling for file downloading and PDF processing. If a file fails to download or a PDF cannot be processed, the script will log the error and continue with the next file.
Logs are printed in the console, and files are skipped if they are already processed (using checksums).
Log Example:
[INFO] Downloading: https://example.com/pdf1.pdf
[INFO] Extracted embedded text from /path/to/pdf1.pdf
[INFO] Saved JSON: output/json_records/doc_20220501T123456.json
[ERROR] Metadata extraction failed for /path/to/invalid.pdf: <error message>
File Structure

main.py: The main script for crawling, downloading PDFs, extracting metadata, and OCR text extraction.
utils/: Utility functions for crawling, downloading files, extracting metadata, performing OCR, and saving JSON data.
requirements.txt: List of Python dependencies.
output/: Directory where JSON files and other outputs are stored.

Considerations and Trade-offs

Error Handling: The script includes basic error handling for network issues and PDF processing failures. This ensures that one failure does not stop the entire process.
OCR Efficiency: OCR is used as a fallback when embedded text extraction fails. While OCR can handle images, it is generally slower and less accurate than direct text extraction. This trade-off ensures that all PDFs, even those without text, are processed.
Checksums: The script uses SHA-256 checksums to track downloaded files. This avoids re-downloading or re-processing files. However, the checksum file (checksums.json) can grow large if many files are processed over time.
Parallelism: The script currently processes files sequentially. For large-scale crawling and OCR tasks, adding concurrency (e.g., using concurrent.futures) could improve performance, but it might add complexity in handling errors and managing resources.


