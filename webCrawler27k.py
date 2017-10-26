from BeautifulSoup import BeautifulSoup # BS3
import urllib2 
from urllib import urlretrieve

imdb_url='http://www.imdb.com/title/'

with open("tlist.txt") as title:
	for ln in title:
		t=ln.rstrip()
		url=imdb_url+t
		print url
		data = urllib2.urlopen(url).read()
		parsed_html = BeautifulSoup(data)
		ps = parsed_html.findAll("div", { "class" : "poster" })
		if len(ps) == 1:
			l=ps[0]
			od = dict( (x.encode("utf-8"),y.encode("utf-8")) for (x,y) in l.img.attrs)
    		#### save poster image to file ####
    		urlretrieve(od['src'], t+".png")
    		#### print out the table #####
			# print ",".join([od['alt'].replace(" Poster",""),t,od['src']])
