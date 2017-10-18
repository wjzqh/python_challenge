import urllib
import urllib2

data= {}
number = '12345'

for i in range(100):
	''' 
	if you connect to the network in proxy server, add the following process.
	proxy = urllib2.ProxyHandler({'http': 'http://username:pwd@ip:port'})
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)
	'''
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
	
	number_list = [i for i in page if i.isdigit()]
	foo.close()
	if number_list == []:
		print "There is not number in the content of page."
		break
	number = number_list[0]
