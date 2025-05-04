import json
from pathlib import Path
from datetime import datetime
import re

def sanitize_filename(name):
    """Remove invalid characters from filename."""
    
    return re.sub(r'[^a-zA-Z0-9._-]', '_', name)

def save_json(data, output_dir, overwrite=True):
    """Save data as JSON, ensuring valid document_id and sanitized filenames."""
   
    if 'document_id' not in data or not data['document_id']:
        
        timestamp = datetime.utcnow().strftime('%Y%m%dT%H%M%S')
        data['document_id'] = f"doc_{timestamp}"

    
    file_name = sanitize_filename(data['document_id']) + ".json"
    
   
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
   
    json_file = output_path / file_name

   
    if not overwrite and json_file.exists():
        print(f"[SKIP] JSON already exists: {json_file}")
        return

    try:
       
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[INFO] Saved JSON: {json_file}")
    except IOError as e:
        print(f"[ERROR] I/O error occurred while saving JSON: {e}")
    except Exception as e:
        print(f"[ERROR] Failed to save JSON: {e}")

def load_existing_checksums(checksum_file):
    """Load existing checksums from the checksum file."""
    if Path(checksum_file).exists():
        try:
            with open(checksum_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"[ERROR] Failed to decode JSON in {checksum_file}")
            return {}
        except IOError as e:
            print(f"[ERROR] I/O error occurred while reading {checksum_file}: {e}")
            return {}
    return {}

def save_checksums(checksums, checksum_file):
    """Save updated checksums to the checksum file."""
    try:
        with open(checksum_file, 'w', encoding='utf-8') as f:
            json.dump(checksums, f, indent=2, ensure_ascii=False)
        print(f"[INFO] Saved checksums to {checksum_file}")
    except IOError as e:
        print(f"[ERROR] I/O error occurred while saving checksums: {e}")
    except Exception as e:
        print(f"[ERROR] Failed to save checksums: {e}")
