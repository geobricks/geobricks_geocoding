import json
import os
import urllib2
from flask import Blueprint
from flask import Response, request, url_for
from flask.ext.cors import cross_origin
from geobricks_common.core.log import logger
from geobricks_geocoding.core.geocoding_core import get_locations

log = logger(__file__)

app = Blueprint("geocoding", "geocoding")


@app.route('/')
@cross_origin(origins='*')
def root():
    """
    Root REST service.
    @return: Welcome message.
    """
    return 'Welcome to Geocoding Service!'

@app.route('/discovery/')
@app.route('/discovery')
@cross_origin(origins='*')
def discovery():
    """
    Discovery service available for all Geobricks libraries that describes the plug-in.
    @return: Dictionary containing information about the service.
    """
    out = {
        'name': 'Geocoding service',
        'description': 'Geocoding service.',
        'type': 'SERVICE'
    }
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@app.route('/place/<name>', methods=['GET'])
@app.route('/place/<name>', methods=['GET'])
@cross_origin(origins='*')
def find_geocoding(name):
    '''
    Find lat lon of places by name.
    :param name: String of places separated by "|"
    :return: an array or array containing the different lat and lon
    '''
    log.info("Searching for places: " + name)
    names = name.split("|")
    result = get_locations(names)
    if result is None:
        result = []
    return Response(json.dumps(result), content_type='application/json; charset=utf-8')
