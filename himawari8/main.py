import logging
import os
import platform
import time

from .downloader import start_downloading

KDE_PLASMA_DE = ["/usr/share/xsessions/plasma", "plasma"]


# Special imports depending on OS
if platform.system() == "Windows":
    from .wallpaper.windows10 import set_wallpaper
elif platform.system() == "Linux":
    # If we are using KDE desktop environment
    if os.environ.get("DESKTOP_SESSION") in KDE_PLASMA_DE:
        from .wallpaper.linux_kde import set_wallpaper
    else:
        logging.error("Desktop environment not supported")
else:
    logging.error("OS not supported")


def main():
    while True:
        print('Starting...')
        wallpaper_path = start_downloading()
        if wallpaper_path != -1:
            print(wallpaper_path)
            set_wallpaper(wallpaper_path)
        time.sleep(600)


if __name__ == '__main__':
    main()
