import dbus


def set_wallpaper(path, plugin='org.kde.image'):
    script = """
    var allDesktops = desktops();
    print (allDesktops);
    for (let i = 0; i < allDesktops.length; i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = '%s';
        d.currentConfigGroup = Array('Wallpaper', '%s', 'General');
        d.writeConfig('Image', 'file://%s')
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(script % (plugin, plugin, path))
