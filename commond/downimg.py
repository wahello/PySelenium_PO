__author__ = 'tsbc'

import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(page):
	rs = r'src="(.*?\.mp4)">'
	imgre = re.compile(rs)
	imglist = re.findall(imgre, page)

	for imgurl in imglist:
		#urllib.urlretrieve(imgurl, "%s.mp4" % x)
		print imgurl

page = getHtml("http://www.jikexueyuan.com/course/659_4.html")
print page
print getImg(page)