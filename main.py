import datetime
import logging
import tempfile
import time

import dbus
import requests

download_url = 'https://seg-web.nict.go.jp/wsdb_osndisk/fileSearch/download'
token_url = 'https://seg-web.nict.go.jp/wsdb_osndisk/shareDirDownload/bDw2maKV'
token_var_name = 'FIXED_TOKEN = "'
token_len = 40


# Don't know how it works
def set_kde_wallpaper(filepath, plugin='org.kde.image'):
    script = """
    const allDesktops = desktops();
    for (let i = 0; i < allDesktops.length; i++) {
        const d = allDesktops[i];
        d.wallpaperPlugin = '%s';
        d.currentConfigGroup = Array('Wallpaper', '%s', 'General');
        d.writeConfig('Image', 'file://%s')
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(script % (plugin, plugin, filepath))


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
    response = session.get(token_url).content.decode()
    token_pos = response.find(token_var_name)
    return response[token_pos + len(token_var_name):token_pos + len(token_var_name) + token_len]


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
    return session.post(url=download_url, data=data)


# Save file to temp directory
def save_file(file):
    path_to_save = tempfile.gettempdir() + '/himawari8_wallpaper.png'
    with open(path_to_save, 'wb') as f:
        f.write(file)
    return path_to_save


def start():
    session = requests.Session()
    token = get_token(session)
    file_response = download_file(session, token)
    if file_response.status_code == 200:
        path = save_file(file_response.content)
        set_kde_wallpaper(path)
    else:
        logging.error(f'Download file request status code is {file_response.status_code}')


def main():
    while True:
        start()
        time.sleep(600)


if __name__ == '__main__':
    main()
