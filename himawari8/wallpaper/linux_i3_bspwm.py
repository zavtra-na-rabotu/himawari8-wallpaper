import subprocess


def set_wallpaper(path):
    subprocess.run(['feh', '--bg-fill', '--no-xinerama', path])
