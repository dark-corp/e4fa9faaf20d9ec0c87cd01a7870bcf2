#!/usr/bin/python
import urllib
import sys
import time
import argparse
import urllib.request, urllib.parse, urllib.error
url = 'https://www.youtube.com/watch?v=d3ygM_sIeoI'
print("baixando com urllib")
urllib.request.urlretrieve(url, "nice.mp4")

print("baixando com urllib2")
f = urllib.request.urlopen(url)
data = f.read()

with open("nice.mp4", "wb") as code:
    code.write(data)
