""" Geokoordinaten zu einer Adresse anfordern """
import urllib2
import pprint
import json
add = "Universitätstrasse 6 ETH Zürich"
add = urllib2.quote(add)  #(add.encode("utf-8"))
geocode_url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % add
req = urllib2.urlopen(geocode_url)
jsonResponse = json.loads(req.read())
pprint.pprint(jsonResponse) 