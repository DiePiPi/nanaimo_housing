# gg_map.py
"""
Get map from google "maps distance matrix API"
"""
import os
import googlemaps
from datetime import datetime
from datetime import timedelta
import pytz 


def GetGGDistance(origin, destination, mode):
	"""
	Will return a matrix with each row as a pair of destination and origin.
	available modes:
	'driving', 'walking', 'transit' or 'bicycling'
	Returns duration and distance
	"""
	
	GG_MAPS_KEY = os.environ['GG_MAPS_KEY']
	gmaps = googlemaps.Client(key = GG_MAPS_KEY)
	
	
	# let us set the time at tomorrow 8am.
	tomorrow = datetime.now(pytz.timezone('America/Vancouver')) + timedelta( days = 1 )
	tomorrow_9am = tomorrow.replace( hour = 9 )
	
	directions_result = gmaps.distance_matrix(origin,
	                                     destination,
	                                     mode=mode,
	                                     departure_time=tomorrow_9am)

	duration = directions_result['rows'][0]['elements'][0]['duration']['text']
	distance = directions_result['rows'][0]['elements'][0]['distance']['text']
	return duration, distance
	
def GetGGBus(origin, destination):
	"""
	Will return a duration and distance to nearest bus stop going to 
	<destination>.
	Returns a tuple of length 2.
	"""
	GG_MAPS_DIRECTIONS = os.environ['GG_MAPS_DIRECTIONS']
	gmaps = googlemaps.Client(key = GG_MAPS_DIRECTIONS)
	tmp = gmaps.directions( origin, destination, mode = 'transit' )
	bus_stop = tmp[0]['legs'][0]['steps'][0]['transit_details']['departure_stop']['location']
	return GetGGDistance( origin, bus_stop, mode = 'walking' )
