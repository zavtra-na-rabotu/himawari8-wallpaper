import subprocess


def set_wallpaper(path):
    script = """
    /usr/bin/osascript<<END
    tell application "Finder"
        set desktop picture to POSIX file "%s"
    end tell
    END
    """
    subprocess.Popen(script % path, shell=True)
