import subprocess


def set_wallpaper(path):
    subprocess.run(["gsettings", "set", "org.cinnamon.desktop.background", "picture-uri", path])
