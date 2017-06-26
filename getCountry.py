"""Länderkürzel zu einer IP-Adresse bestimmen """
import json
import urllib2

def getCountry(ipAddress):
    response = urllib2.urlopen("http://freegeoip.net/json/"+ipAddress,timeout=4)
    jsontxt = response.read().decode("utf-8")
    responseJson = json.loads(jsontxt)
    return responseJson.get("country_code")

# Test mit 2 IP Adressen
print getCountry("50.78.253.58")
print getCountry("131.152.1.1")