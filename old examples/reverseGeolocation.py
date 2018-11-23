"""Inverse Geokodierung, zu einer Geokoordinate (Lat,Long) eine Adresse ermitteln"""
import urllib2
import pprint
import json

lat="47.3783606"
lon="8.5488485"
geocode_url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=false" % (lat,lon)
req = urllib2.urlopen(geocode_url,timeout=4)
jsonResponse = json.loads(req.read())
#pprint.pprint(jsonResponse) 
print jsonResponse["results"][0]["formatted_address"]