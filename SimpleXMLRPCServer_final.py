#!/usr/bin/python

#desmet_t@hotmail.com
#12/12/2018

#SERVICE PROVIDER

#SimpleXMLRPCServer is the library to create an XML-RPC server


from xmlrpc.server import SimpleXMLRPCServer
import logging
import random
import datetime


#Set up logging
logging.basicConfig(level=logging.DEBUG)

server = SimpleXMLRPCServer (('localhost', 9000),logRequests=True)

#register XML-RPC introspextion functions such as system.listMethods()
server.register_introspection_functions()

#Multicall provides a way to encapsulate multiple calls to a remote server into a single request
server.register_multicall_functions()

#Expose functions

def get_weather_station_location():
	return "Oizy - Belgium"
server.register_function(get_weather_station_location)

def get_weather_station_coordinates():
	return "49.8966N-5.011E"
server.register_function(get_weather_station_coordinates)

def get_date():
	my_datetime = datetime.datetime.now()
	return my_datetime.strftime("%Y-%m-%d %H:%M:%S")
server.register_function(get_date)

def get_temperature():
	return random.randint(-20,40)
server.register_function(get_temperature)

def get_wind_direction():
	wind_directions = ['N','NE','E','SE','S','SW','W','NW']
	random.shuffle(wind_directions)
	return (wind_directions)[0]
server.register_function(get_wind_direction)

def get_wind_speed():
	return random.randint(0,12)
server.register_function(get_wind_speed)

try:
	print ('Use Control-C to EXIT')
	server.serve_forever()
except KeyboardInterrupt:
	print ('Exiting')	
