import zipfile
zip = '..\\data\\channel.zip'
z = zipfile.ZipFile(zip,'r')
number = '90052'
suffix = '.txt'
comments = []
while True:
	if number is '':
		break;
	content = z.read(number+suffix)
	comments.append(z.getinfo(number+suffix).comment)
	content = content.split()
	number = ''
	for i in content:
		if i.isdigit():
			number = str(i)
			break

print "".join(comments)

'''
Printing the result forms the letters 'HOCKEY', but using that as a URL will tell you "it's in the air" and to look at the letters. 
Indeed, the letters of the word hockey have been built up out of the letters O, X, Y, G, E, and N, and 'oxygen' leads to the next level.
'''