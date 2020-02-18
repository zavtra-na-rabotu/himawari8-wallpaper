import ctypes


def set_wallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
