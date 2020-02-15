import os
import platform

from setuptools import setup

KDE_PLASMA_DE = ["/usr/share/xsessions/plasma", "plasma"]

requirements = [
    "certifi==2019.11.28",
    "chardet==3.0.4",
    "idna==2.8",
    "requests==2.22.0",
    "urllib3==1.25.8",
]

if platform.system() == "Linux" and os.environ.get("DESKTOP_SESSION") in KDE_PLASMA_DE:
    requirements.append("dbus-python==1.2.16")

setup(
    name='himawari8-wallaper',
    version='0.1',
    packages=['himawari', 'wallpaper'],
    url='',
    license='',
    author='Dmitry Vasilev',
    author_email='mekon26@gmail.com',
    description='Wallpapers from himawari8 satellite',
    install_requires=requirements
)
