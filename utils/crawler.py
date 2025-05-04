import os
import time
import hashlib
from playwright.sync_api import sync_playwright
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

DOWNLOAD_DIR = os.path.abspath("output")

def compute_sha256(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def is_valid_url(url):
    return any(url.lower().endswith(ext) for ext in ('.pdf', '.epub', '.html'))

def save_file(url, dest_folder):
    try:
        dest_folder = os.path.abspath(dest_folder)
        os.makedirs(dest_folder, exist_ok=True)
        filename = os.path.basename(urlparse(url).path)
        local_path = os.path.join(dest_folder, filename)

        response = requests.get(url, stream=True, timeout=15)
        if response.status_code == 200:
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return local_path
        else:
            print(f"[WARNING] Failed to download {url} (Status: {response.status_code})")
    except Exception as e:
        print(f"[ERROR] Exception downloading {url}: {e}")
    return None

def crawl_and_download(start_url):
    downloaded_files = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(start_url)
            time.sleep(2)  

            html = page.content()
            soup = BeautifulSoup(html, "html.parser")
            links = soup.find_all("a", href=True)

            for link in links:
                href = urljoin(start_url, link['href'])
                if is_valid_url(href):
                    print(f"[INFO] Downloading: {href}")
                    saved_path = save_file(href, DOWNLOAD_DIR)
                    if saved_path:
                        downloaded_files.append(saved_path)
                time.sleep(1)  
            browser.close()
    except Exception as e:
        print(f"[ERROR] Crawler failed for {start_url}: {e}")
    return downloaded_files
