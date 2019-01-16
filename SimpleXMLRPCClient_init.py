#!/usr/bin/python

#desmet_t@hotmail.com
#10/10/2018

#SERVICE REQUESTER

#The xmlrpclib module lets you communicate from Python with any XML-RPC server written in any language

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
#proxy = xmlrpc.client.ServerProxy('http://localhost:9000', verbose=True)

#print((proxy.system.listMethods()))

print("Weather station:", proxy.get_weather_station_location())

print("Coordinates:", proxy.get_weather_station_coordinates())

print("=" * 50)

print(proxy.get_temperature(), "degrees Celcius")

print(proxy.get_wind_speed(), "Beaufort", proxy.get_wind_direction())
