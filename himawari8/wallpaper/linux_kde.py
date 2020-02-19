import dbus


# There is bug or feature ? KDE doesn't update wallpaper if name of the file didn't change
# Workaround:
# d.writeConfig('Color', '0, 0, 0') fills the background with black color
# d.writeConfig('Image', 'file://%s') sets wallpaper
def set_wallpaper(path, plugin='org.kde.image'):
    script = """
    var allDesktops = desktops();
    for (let i = 0; i < allDesktops.length; i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = '%s';
        d.currentConfigGroup = Array('Wallpaper', '%s', 'General');
        d.writeConfig('Color', '0, 0, 0')
        d.writeConfig('Image', 'file://%s')
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(script % (plugin, plugin, path))
