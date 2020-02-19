import argparse
import logging
import os
import platform
import time

from himawari8.downloader import download_latest_image

KDE_PLASMA_DE = ['plasma', '/usr/share/xsessions/plasma']
WINDOW_MANAGERS = ['i3', 'awesome', '/usr/share/xsessions/bspwm']
PLATFORM = platform.system()


# Imports depending on OS
if PLATFORM == 'Linux':
    de = os.environ.get('DESKTOP_SESSION')
    if de in KDE_PLASMA_DE:
        from himawari8.wallpaper.linux_kde import set_wallpaper
    elif de in WINDOW_MANAGERS:
        from himawari8.wallpaper.linux_feh import set_wallpaper
    else:
        exit('Desktop environment not supported')
elif PLATFORM == 'Darwin':
    from himawari8.wallpaper.osx import set_wallpaper
elif PLATFORM == 'Windows':
    from himawari8.wallpaper.windows10 import set_wallpaper
else:
    exit('OS not supported')


def try_to_update_wallpaper():
    wallpaper_path = download_latest_image()
    if wallpaper_path != -1:
        set_wallpaper(wallpaper_path)
        print(f'Wallpaper has been successfully updated {wallpaper_path}')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interval', type=int, help='wallpaper update interval in minutes')
    return parser.parse_args()


def main():
    args = parse_arguments()
    if args.interval is not None:
        while True:
            try_to_update_wallpaper()
            time.sleep(args.interval * 60)
    else:
        try_to_update_wallpaper()


if __name__ == '__main__':
    main()
