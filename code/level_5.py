import pickle

#打开文件
pk_file=open("..\\data\\banner.p","rb")



#将文件反序列化成对象
data=pickle.load(pk_file)

str=""

#对输出做处理
for list in data:
    print(list)
    for i in list:
        str+=i[0]*i[1]
    str+='\n'
print (str)