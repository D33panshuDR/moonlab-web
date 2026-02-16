import csv
import requests
import os
import re
from dotenv import load_dotenv 

load_dotenv()

SHEET_URL = os.getenv("GOOGLE_SHEET_URL")

if not SHEET_URL:
    print("Error: GOOGLE_SHEET_URL not found in .env file.")
    exit(1)

CONTENT_DIR = "content/people"
KEEP_FILES = ["_index.md", "sujit.md"]

def clean_filename(name):
    clean = re.sub(r'[^a-zA-Z0-9\s]', '', name).lower().strip()
    return re.sub(r'\s+', '-', clean) + ".md"

def sync_people():
    print(f"Connecting to Google Sheet...")
    
    try:
        response = requests.get(SHEET_URL)
        response.raise_for_status()
        content = response.content.decode('utf-8')
        reader = csv.DictReader(content.splitlines())
        rows = list(reader)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    # Cleanup
    print(f"Cleaning old profiles in {CONTENT_DIR}...")
    if not os.path.exists(CONTENT_DIR):
        os.makedirs(CONTENT_DIR)

    for filename in os.listdir(CONTENT_DIR):
        # Skip deleting if the file is in KEEP list
        if filename in KEEP_FILES:
            continue
            
        file_path = os.path.join(CONTENT_DIR, filename)
        os.remove(file_path)

    count = 0
    for row in rows:
        name = row.get('Name', '').strip()
        
        if not name:
            continue

        filename = clean_filename(name)
        
        if filename in KEEP_FILES:
            print(f"Skipping protected file: {filename}")
            continue

        filepath = os.path.join(CONTENT_DIR, filename)
        
        raw_group = row.get('Group', 'student').strip().lower()
        raw_interests = row.get('Interests', '').strip()

        md = f"""---
title: "{name}"
role: "{row.get('Role', '').strip()}"
group: "{raw_group}"
bio: "{row.get('Bio', '').strip()}"
profile_image: "{row.get('Image', '').strip()}"
interests: "{raw_interests}"
contact:
  github: "{row.get('Github', '').strip()}"
  linkedin: "{row.get('Linkedin', '').strip()}"
  scholar: "{row.get('Scholar', '').strip()}"
---
"""
        with open(filepath, "w", encoding='utf-8') as f:
            f.write(md)
            count += 1

    print(f"Success! Generated {count} profiles.")

if __name__ == "__main__":
    sync_people()