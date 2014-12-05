from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksGeocoding',
    version='0.1.0',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks library to manage geocoding.',
    install_requires=[
        "flask",
        'flask-cors',
        'geopy'
    ],
    url='http://pypi.python.org/pypi/GeobricksGeocoding/',
    keywords=['geobricks', 'geocoding', 'geopy', 'gis']
)
