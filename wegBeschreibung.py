"""Wegbeschreibung für eine Route von A nach B bei Google anfordern und als Text ausgeben."""
import urllib2
import json
import re

## Trick um HTML Elemente weg zu bekommen
DIV_RE = re.compile(r"<div.+div>")
TAG_RE = re.compile(r"<[^>]+>")
def remove_tags(text):
    t2 = DIV_RE.sub('',text)
    return TAG_RE.sub('', t2)

## Parameter für Route
start = "Emma Herwegh-Platz 2 Liestal"
ziel = "Badi Liestal"
sprache = "de" # "en"
art = "walking" #driving walking transit bicycling
start = urllib2.quote(start.encode("utf-8"))
ziel = urllib2.quote(ziel.encode("utf-8"))

geocode_url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&avoid=highways&mode=%s&language=%s" % (start,ziel,art,sprache)
req = urllib2.urlopen(geocode_url)
jsonResponse = json.loads(req.read())

print "Distanz:" + jsonResponse["routes"][0]["legs"][0]["distance"]["text"]
print "Dauer:" + jsonResponse["routes"][0]["legs"][0]["duration"]["text"]

for step in jsonResponse["routes"][0]["legs"][0]["steps"]:
    print step["distance"]["text"] + " > "+ remove_tags(step["html_instructions"])


