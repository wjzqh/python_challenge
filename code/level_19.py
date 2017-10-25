import urllib,re,wave,email,StringIO,struct
url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html'
src = urllib.urlopen(url).read()
#.匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
c = re.compile("<!--\n(.*)\n-->", re.DOTALL)
#re findall 方法能够以列表的形式返回能匹配的子串
data = c.findall(src)[0]

message = email.message_from_string(data)
audio = message.get_payload(0).get_payload(decode=True)

f = wave.open(StringIO.StringIO(audio)) 
guts = f.readframes(f.getnframes())

f.close()
for i in 0, 1:
    out = wave.open("..\\data\\i%d.wav"%i, "wb")
    out.setparams(f.getparams())
    out.setframerate(f.getframerate()//2)
    out.setnframes(f.getnframes()//2)
    out.writeframes(guts[i::2])
    out.close() 
#the result is idiot             