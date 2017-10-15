import urllib
import urllib2

data= {}
number = '12345'

for i in range(100):
	data['nothing'] = number
	url_values = urllib.urlencode(data)
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
	full_url = url + '?' + url_values
	try:
		foo = urllib2.urlopen(full_url,timeout=20)
	except:
		print "timeout"
		break
	page = foo.read()
	print page
	page = page.split(" ")
	
	number = [i for i in page if i.isdigit()][0]
	foo.close()
	if number is "":
		print "the content of page is not number."
		break