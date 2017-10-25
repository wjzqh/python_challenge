#参照http://blog.csdn.net/jingza/article/details/52661653的解答过程
import requests  
import re  
url='http://www.pythonchallenge.com/pc/hex/unreal.jpg'  
  
def next_page(url,start=0,end=''):  
    #添加的头部请求  
    content_range={'Range':'bytes={0}-{1}'.format(start,end)}  
    # 登陆信息  
    auth = ('butter', 'fly')  
    #发送请求  
    req = requests.get(url, auth=auth,headers=content_range)  
    head=req.headers  
    con_range=head.get('Content-Range')  
    '''  
    打印网站连接状态，Content-Range，文件大小，文件前100个字节内容  
    '''  
    print('Status Code:',req.status_code)  
    print('Content-Range:', con_range)  
    print('content-size: ', len(req.content))  
    print('content[:100]: ', str(req.content[:100]))  
    #如果Content-Range存在，就寻找结尾并且把信息保存到first.txt  
    if con_range:  
        index = re.search(r'-(\d+)/', con_range).group(1)  
        text=req.content  
        with open('..\\data\\first.txt','wb') as f:  
            f.write(con_range.encode('utf-8')+b'\n')  
            f.write(text)  
            f.write(b'************************************* \n')  
  
if __name__=='__main__':  
    next_page(url,30203)
'''
分别替换next_page函数中的数字，最后得到30347，然后就没有了。
接下来，该如何进行呢？百度了一下，从前面开始不行，那么别人说是反过来，依次取2123456744、2123456712、1152983631。
会有很大235kb的数据，保存为dat数据文件。不知道它是什么类型的，但是在linux中可以使用命令file first.txt,知道这是一个zip文件，
所以我们解压的时候需要密码，密码就是invader，所以反过来就是：'redavni'
package.pack，从文件名可以想到需要解压数据，使用winhex查看文件数据开头的数据属于zlib 78 9c
'''
