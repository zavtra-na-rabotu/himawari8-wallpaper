import datetime
import logging
import os

import requests

DOWNLOAD_URL = 'https://seg-web.nict.go.jp/wsdb_osndisk/fileSearch/download'
TOKEN_URL = 'https://seg-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV'
TOKEN_VAR_NAME = 'FIXED_TOKEN = "'
TOKEN_LEN = 40


# Generate name of the latest photo
def generate_file_name():
    now = datetime.datetime.now()
    year = now.strftime('%Y')
    month = now.strftime('%m')
    day = now.strftime('%d')
    hour = now.strftime('%H')
    minute = now.strftime('%M')[0] + '0'
    return f'/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/{year}/{month}-{day}/{hour}/hima8{year}{month}{day}{hour}{minute}00fd.png'


# Response is just an html page
# Token is a variable in one of js scripts inside this page
# So we are trying to find it by variable name
def get_token(session):
    response = session.get(TOKEN_URL).content.decode()
    token_pos = response.find(TOKEN_VAR_NAME)
    return response[token_pos + len(TOKEN_VAR_NAME):token_pos + len(TOKEN_VAR_NAME) + TOKEN_LEN]


# Download latest photo
def download_file(session, token):
    file_name = generate_file_name()
    data = {
        'dl_path': file_name,
        'filelist[0]': file_name,
        'action': 'dir_download_dl',
        '_method': 'POST',
        'data[FileSearch][hashUrl]': 'bDw2maKV',
        'data[FileSearch][fixedToken]': token,
        'data[FileSearch][is_compress]': 'false'
    }
    return session.post(url=DOWNLOAD_URL, data=data)


# Save file to temp directory
def save_file(file):
    path_to_save = os.path.expanduser('~') + '/himawari8.png'
    with open(path_to_save, 'wb') as f:
        f.write(file)
    return path_to_save


def start_downloading():
    session = requests.Session()
    token = get_token(session)
    print(f'Token {token}')
    file_response = download_file(session, token)
    if file_response.status_code == 200:
        return save_file(file_response.content)
    else:
        logging.error(f'Download file request status code is {file_response.status_code}')
        return -1
