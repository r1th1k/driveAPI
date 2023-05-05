from Google import Create_Service
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
import io
import os

CLIENT_SECRET_FILE = "demo.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# file_name = input("Enter file name: ")
# mime_type = mimeFind(file_name)
file_name = "baizhu.jpg"
mime_type = "image/jpg"

def up():
    metadata = {
        'name': file_name,
        'parents': ['1-dbGLNe0Dk8AhmCQV8XZG5hI2TdV5YVz'] 
    }
    media = MediaFileUpload(file_name, mimetype=mime_type)

    service.files().create(body = metadata, media_body=media, fields="id").execute()

def down():
    file_id="19lt2GYwyju_HDpiHnqCsYdXPCfBhZY3Q"
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print('Download progress {0}'.format(status.progress()*100))
    fh.seek(0)
    with open(os.path. join('./', file_name), 'wb') as f:
        f.write(fh. read())
        f.close

down()

