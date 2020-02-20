import subprocess
import pathlib


def set_wallpaper(path):
    uri = pathlib.Path(path).as_uri()
    subprocess.run(["gsettings", "set", "org.cinnamon.desktop.background", "picture-uri", uri])
