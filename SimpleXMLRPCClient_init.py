#!/usr/bin/python

#desmet_t@hotmail.com
#12/12/2018

#SERVICE REQUESTER

#The xmlrpclib module lets you communicate from Python with any XML-RPC server written in any language

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
#proxy = xmlrpc.client.ServerProxy('http://localhost:9000', verbose=True)

multicall = xmlrpc.client.MultiCall(proxy)

#print((proxy.system.listMethods()))
#print("Weather station:", proxy.get_weather_station_location())
#print("Coordinates:", proxy.get_weather_station_coordinates())
#print("=" * 50)
#print(proxy.get_temperature(), "degrees Celcius")
#print(proxy.get_wind_speed(), "Beaufort", proxy.get_wind_direction())

multicall.get_weather_station_location()
multicall.get_weather_station_coordinates()
multicall.get_temperature()
multicall.get_wind_speed()
multicall.get_wind_direction()
result = multicall()

print(" Weather station: %s\n Coordinates: %s\n ==================================================\n %d degrees Celcius\n %d Beaufort %s " % tuple(result))