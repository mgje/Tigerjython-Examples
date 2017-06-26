""" Response Header einer HTTP-Anfrage ausgeben """
from urllib2 import urlopen

endpoint = "http://www.tigerjython.ch"
handler = urlopen(endpoint)
headers = handler.headers
code = handler.getcode()

print "HTTP-Status:", code
print headers