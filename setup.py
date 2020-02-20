import os
import platform

from setuptools import setup, find_packages

KDE_PLASMA_DE = ['plasma', '/usr/share/xsessions/plasma']

requirements = [
    'certifi',
    'chardet',
    'idna',
    'requests',
    'urllib3',
]

if platform.system() == 'Linux' and os.environ.get('DESKTOP_SESSION') in KDE_PLASMA_DE:
    requirements.append('dbus-python')

setup(
    name='himawari8-wallaper',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.0',
    url='',
    license='',
    author='Dmitry Vasilev',
    author_email='mekon26@gmail.com',
    description='Wallpapers from himawari8 satellite',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'himawari = himawari8.main:main',
        ]
    }
)
