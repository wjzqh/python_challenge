import xmlrpclib
url = 'http://www.pythonchallenge.com/pc/phonebook.php'
phonebook = xmlrpclib.Server(url)
print phonebook.phone('Bert')