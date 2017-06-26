""" HTTP-Anfrage und den Inhalt der Antwort (Response body) ausgeben"""
from urllib2 import urlopen
endpoint = "http://www.tigerjython.ch/index.php?inhalt_links=navigation.inc.php&inhalt_mitte=home/home.inc.php"
response = urlopen(endpoint)
html = response.read()
print html