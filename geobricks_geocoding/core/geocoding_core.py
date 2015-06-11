from geopy.geocoders import Nominatim
from geobricks_common.core.log import logger
import time

log = logger(__file__)

# TODO: creating a switch to the different geocoding services
geolocator = Nominatim()
rlock = False
cached_places = {}
request_sleep_time = 1.1
waiting_sleep_time = 0.5
timeout = 30


def get_locations(places):
    """
    @param places: array of places to search i.e. ["FAO, Rome", "Paris"]
    @type: string:
    @return: location obj containing the location.raw, location.address and location.latitude location.longitude
             return None if place not found
    """
    try:
        results = []
        for place in places:
            if place in cached_places:
                results.append(cached_places[place])
            else:
                while rlock:
                    time.sleep(waiting_sleep_time)
                time.sleep(request_sleep_time)
                result = get_location(place)
                if result is not None:
                    cached_places[place] = result
                    results.append(result)
                else:
                    results.append([])
        return results
    except Exception, e:
        log.warn(e)
        # TODO: remove it from here
        results.append([])
        pass
    finally:
        return results

def get_location(place):
    """
    @param place: place to search i.e. "FAO, roma"
    @type: string:
    @return: location obj containing the location.raw, location.address and location.latitude location.longitude
             return None if place not found
    """
    try:
        location = geolocator.geocode(place.lower(), timeout=timeout)
        rlock = False
        if location is not None:
            return [location.latitude, location.longitude]
        else:
            return []
    except Exception, e:
        raise Exception(e)


def get_reverse(lat, lon):
    """
    @param lat: place to search i.e. "52.509669"
    @type: float
    @param lon: place to search i.e. "13.376294"
    @type: float
    @return: location obj containing the location.raw, location.address and location.latitude location.longitude
             return None if place not found
    """
    try:
        return geolocator.reverse(lat, lon)
    except Exception, e:
        raise Exception(e)