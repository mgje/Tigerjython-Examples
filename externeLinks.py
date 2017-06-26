""" Externe Links einer Webseite überprüfen """
from HTMLParser import HTMLParser
from urllib2 import urlopen
import sys

class LinksExtractor(HTMLParser): # derive new HTML parser

    def __init__(self) :        # class constructor
        HTMLParser.__init__(self)  # base class constructor
        self.links = []        # create an empty list for storing hyperlinks

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        else:
            if len(attrs) > 0 :
                for attr in attrs :
                    if attr[0] == "href" :         # ignore all non HREF attributes
                        self.links.append(attr[1])
            
    def get_links(self) :     # return the list of extracted links
        return self.links
    

htmlparser = LinksExtractor() 
endpoint = "http://www.tigerjython.ch/index.php?inhalt_links=navigation.inc.php&inhalt_mitte=anhang/links.inc.php"  

response = urlopen(endpoint)
html = response.read()
response.close()

encodedhtml=html #unicode(html, "iso-8859-1")
htmlparser.feed(encodedhtml)      # parse the file saving the info about links
htmlparser.close()
links = htmlparser.get_links()   # get the hyperlinks list

for link in links:
    s = link[:7]
    if s.lower() == "http://":
        try:
            conn = urlopen(link,timeout=4)
            code = conn.getcode()
            msg = conn.msg
            conn.close()
            if code != 200:
                print "******** ERROR *********"
                print  msg + "  --> " + link 
                print "************************"+ "\n"
            else:
                print "OK: " + link + "\n"
        except:
            print   "******** no answer *********"
            print   "Fail ---> " + link 
            print   "****************************"+ "\n"
        
        sys.stdout.flush()
                