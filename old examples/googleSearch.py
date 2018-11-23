""" Google Search Beispiel aus dem Online-Lehrmittel TigerJython """
import urllib2, json

search = input("Enter a search string(AND-connect with +):")
url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + search
responseStr = urllib2.urlopen(url).read()
response = json.loads(responseStr)

responseData = response["responseData"]

results = responseData["results"]

for result in results:
    title = result["title"]
    url = result["url"]
    print title + " ---- " + url