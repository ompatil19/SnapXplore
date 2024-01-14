from googleapiclient.discovery import build
from google.oauth2 import service_account
import csv
import os 

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'
PARENT_FOLDER_ID = "1LAQOQlEWx6JcwIxku2glP657GQwJQGWD"
CSV_FILE = 'uploaded_links.csv'

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_photo(file_path, location):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': location,
        'parents': [PARENT_FOLDER_ID]
    }

    media = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()

    file_id = media.get('id')
    file_link = f'https://drive.google.com/uc?id={file_id}'

    log_to_csv(location, file_link)

def log_to_csv(location, file_link):
    with open(CSV_FILE, mode='a', newline='') as csv_file:
        fieldnames = ['name', 'category', 'url']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Check if the CSV file is empty, if so, write header
        if csv_file.tell() == 0:
            writer.writeheader()

        writer.writerow({'name': location, 'category': 'pilgrimages', 'url': file_link})

# Beaches Data Upload 
pilgrimages =  os.listdir("Web Scraping/images/pilgrimage")
file = "Web Scraping/images/pilgrimage/"
for pilgrimage in pilgrimages:
    folder_path = file + pilgrimage + "/"
    f = os.listdir(folder_path)
    for i in f:
        name = i.split('.')[0]
        name  = ''.join([j for j in name if not j.isdigit() and j!= '_'])
        name = name.replace('_', ' ')
        name = name.strip()

        url = folder_path + i
        upload_photo(url, name)
