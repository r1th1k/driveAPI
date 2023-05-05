from Google import Create_Service

CLIENT_SECRET_FILE = "demo.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folders = ["pokemon", "genshin"]

for folder in folders:
    metadata = {
        'name':folder,
        'mimeType':'application/vnd.google-apps.folder'
        #parents : []
    }

    service.files().create(body = metadata).execute()

