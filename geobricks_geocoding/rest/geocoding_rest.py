import json
import os
from flask import Blueprint
from flask import Response
from flask.ext.cors import cross_origin
from geobricks_geocoding.utils.log import logger
from geobricks_geocoding.core.geocoding_core import get_locations

log = logger(__file__)

app = Blueprint("geocoding", "geocoding")

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
        'type': 'geocoding'
    }
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@app.route('/latlon/<name>', methods=['GET'])
@app.route('/latlon/<name>', methods=['GET'])
@cross_origin(origins='*')
def find_geocoding(name):
    '''
    Find lat lon of places by name.
    :param name: String of places separated by "|"
    :return: an array or array containing the different lat and lon
    '''
    print name
    names = name.split("|")
    result = get_locations(names)
    return Response(json.dumps(result), content_type='application/json; charset=utf-8')


