import string
text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq 
	glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu 
	ynnjw ml rfc spj.'''
table = string.maketrans(string.ascii_lowercase,string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
str = string.translate(text,table)###or text.translate(table)
print str

s="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.  lmu ynnjw ml rfc spj."
o=""
for x in s:
	if ord(x)>=ord('a') and ord(x)<=ord('z'):
		o+=chr((ord(x)+2-ord('a'))%26+ord('a'))
	else:
		o+=x
print o

#use nested ternary operators:true_part if condition else false_part
for x in s:
    print chr(ord(x) if ord(x) < ord('a') else  ord(x)+2 if ord(x)+2 <= ord('z') else ord(x)-24),
