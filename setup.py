from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksGeocoding',
    version='0.1.4',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks library to manage geocoding.',
    install_requires=[
        # 'watchdog',
        # "flask",
        # 'flask-cors',
        # 'geopy',
        # 'GeobricksCommon'
    ],
    url='http://pypi.python.org/pypi/GeobricksGeocoding/',
    keywords=['geobricks', 'geocoding', 'geopy', 'gis']
)
