import  zlib  
import binascii  
import bz2  
  
#判断十六进制是否能被解析成ascii码  
def readword(c):  
    if c.isalpha() or c.isdigit():  
        return c  
#显示数据的长度，十六进制表示，字符串表示  
def show(data,length=24):  
    print('data length: ' ,len(data))  
    x=binascii.hexlify(data[:length])  
    y=map(readword,[i for i in list(data[:length])])
    print('hex: ',x)  
    print('str: ',list(y))  

if __name__=='__main__':  
    #读取文件内容  
    file=open('..\\data\\package.pack','rb').read()  
    #解压  
    data=zlib.decompress(file)  
    show(data)  
    logs=''  
    #根据提示一循环解压  
    while True:  
        if data[:2]==b'\x78\x9c':   #开头两个字符十六进制，也可以写成b'x\x9c'，因为‘x'的十六进制为\x78  
            data = zlib.decompress(data)  
            logs+=' '  
        elif data[:2]==b'\x42\x5a': #bz2文件开头十六进制， 表示：BZ  
            data = bz2.decompress(data)  
            logs += '#'  
        elif data[-2:] == b'\x9c\x78': #这个来自于第二个提示：往回看就代表反向操作  
            data = zlib.decompress(data[::-1])  
            logs += '\n'  
        else:  
            break  
  
    show(data)  
    print(data[::-1])  
    print(logs)