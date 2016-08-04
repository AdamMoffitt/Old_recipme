import urllib2
import cookielib
import re

link = 'http://allrecipes.com/recipe/241607/vietnamese-grilled-lemongrass-chicken/'
hdr = {'User-Agent' : 'Mozilla/5.0', 'Accept': 'text/html,applicatin/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
req = urllib2.Request(link, headers=hdr)
url = urllib2.urlopen(req)
html = url.read()

links = re.findall('(?<=href=")/recipe/[\w|\W]*?(?=")', html)

outFile = open('output_html.txt', 'w')
print >> outFile, html
outFile.close()

# outFile = open('list.txt', 'w')
# for link in links:
# 	print >> outFile, 'http://allrecipes.com/'+link
# outFile.close()