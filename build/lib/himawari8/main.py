import logging
import os
import platform
import time

from .downloader import start_downloading

KDE_PLASMA_DE = ['/usr/share/xsessions/plasma', 'plasma']


# Imports depending on OS
if platform.system() == 'Windows':
    from .wallpaper.windows10 import set_wallpaper
elif platform.system() == 'Linux':
    de = os.environ.get('DESKTOP_SESSION')
    if de in KDE_PLASMA_DE:
        from .wallpaper.linux_kde import set_wallpaper
    elif de in ['i3', '/usr/share/xsessions/bspwm']:
        from .wallpaper.linux_i3_bspwm import set_wallpaper
    else:
        logging.error('Desktop environment not supported')
else:
    logging.error('OS not supported')


def main():
    while True:
        wallpaper_path = start_downloading()
        if wallpaper_path != -1:
            set_wallpaper(wallpaper_path)
            print(f'Wallpaper has been successfully updated {wallpaper_path}')
        time.sleep(600)


if __name__ == '__main__':
    main()
