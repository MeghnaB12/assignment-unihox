# assignment-unihox

## Features

- **Crawl and Download PDFs**: Automatically download PDF files from web links.
- **Extract PDF Metadata**: Retrieve title, authors, creation date, and other metadata from PDF documents.
- **OCR Text Extraction**: Use Tesseract to perform OCR-based text extraction on PDFs without embedded text.
- **Save Data as JSON**: The extracted metadata and OCR text are saved in a structured JSON format.
- **Error Handling**: Includes error handling and logging for robust operation.
- **Checksums**: Ensures that already processed files are skipped to avoid redundancy.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MeghnaB12/assignment-unihox.git
cd assignment-unihox
```
### Dependencies

The project relies on the following Python libraries:

- **pytesseract**: Performs Optical Character Recognition (OCR) to extract text from images.
- **pdf2image**: Converts PDF pages into images for OCR processing.
- **pdfminer.six**: Extracts embedded (selectable) text directly from PDFs.
- **requests**: Handles HTTP requests for downloading files.
- **beautifulsoup4**: Parses and extracts PDF links from HTML pages.
- **playwright**: Automates headless browsing and crawling of dynamic websites.
- **hashlib**: Generates SHA-256 checksums to avoid reprocessing the same files.
- **os** and **pathlib**: Manage file system paths and directories.

### Setting Up a Virtual Environment

To isolate project dependencies, build a Python virtual environment.

### On macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```
### On windows

python -m venv venv
venv\Scripts\activate

To install all dependencies, use:

```bash
pip install -r requirements.txt
pip install playwright 

```

### 3. Install Tesseract (for OCR)

Tesseract is required to perform OCR (Optical Character Recognition) on scanned PDFs.

#### For Windows:
1. Download the installer from the [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).
2. Install it and **add the installation path** (e.g., `C:\Program Files\Tesseract-OCR`) to your system’s **PATH** environment variable.

#### For macOS:
```bash
brew install tesseract
```

#### For Linux (Debian/Ubuntu-based):

```bash
sudo apt update
sudo apt install tesseract-ocr
```

### Usage

#### Prepare the Environment

- Ensure all dependencies are installed using `pip install -r requirements.txt`.
- Install and configure **Tesseract OCR** on your system (see above).
- Make sure you have `poppler` installed for PDF to image conversion (`pdf2image`).

#### Modify the Script

- Open `main.py` in your editor (e.g., VS Code).
- Update the `TARGET_URLS` list with the URLs you want to crawl and process.

#### Run the Script

```bash
caffeinate python3 main.py
```

The script will crawl the target URLs and download the PDFs. Extract metadata from each PDF. If the PDF does not contain embedded text, OCR will be performed to extract text.
Save the metadata and OCR text as JSON files in the output/json_records directory. Its better if you use single URL at a time otherwise it takes a lot of time.

### Considerations and Trade-offs

- **Error Handling**  
  The script includes basic error handling for network issues and PDF processing failures. This ensures that one failure does not stop the entire process.

- **OCR Efficiency**  
  OCR is used as a fallback when embedded text extraction fails. While OCR can handle image-based PDFs, it is generally slower and less accurate than direct text extraction. This trade-off ensures that all PDFs, including scanned documents, are processed.

- **Checksums**  
  The script uses SHA-256 checksums to track downloaded files and prevent redundant downloads or re-processing. However, the `checksums.json` file can grow large over time if many files are processed.

- **Parallelism**  
  Currently, the script processes files sequentially. For large-scale crawling and OCR tasks, introducing concurrency (e.g., with threading or async I/O) could significantly improve performance. However, it would also add complexity in error handling and resource management.



