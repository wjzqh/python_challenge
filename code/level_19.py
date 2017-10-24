import urllib,re,wave,email,StringIO,struct
url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html'
src = urllib.urlopen(url).read()
#.匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
c = re.compile("<!--\n(.*)\n-->", re.DOTALL)
#re findall 方法能够以列表的形式返回能匹配的子串
data = c.findall(src)[0]

message = email.message_from_string(data)
audio = message.get_payload(0).get_payload(decode=True)
'''
w = wave.open(StringIO.StringIO(audio))      
w2=wave.open('endian.wav','w')   
w2.setnchannels(w.getnchannels())
w2.setsampwidth(w.getsampwidth())
w2.setframerate(w.getframerate())

frm=w.readframes(w.getnframes()) 
wave.big_endian=1            
w2.writeframes(frm)              
w.close()                        
w2.close()

f = wave.open(StringIO.StringIO(audio)) 
guts = f.readframes(f.getnframes())
f.close()
for i in 0, 1:
    out = wave.open("i%d.wav" % i, "wb")
    out.setparams((1, 2, 11025//2, 55788//2, 'NONE', 'not compressed'))
    out.writeframes(guts[i::2])
    out.close() 
'''
wav = wave.open(StringIO.StringIO(audio))
owav = wave.open('indians2.wav','wb')
owav.setparams(wav.getparams())

org = wav.readframes(-1)
dest = struct.unpack('>' + str(wav.getnframes()) + 'h', org)
sdest = "".join([struct.pack('<h', x) for x in dest])
owav.writeframes(sdest)
owav.close()
#the result is idiot             