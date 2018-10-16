import re
import time
import urllib.error
from urllib import request

#自定义函数，功能为使用代理服务器爬取一个网址
def use_proxy(proxy_addr,url):
    # 建立异常处理机制
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0;win64;x64;rv:61.0) Gecko/20100101 Firefox/61.0')
        proxy = request.ProxyHandler({'http':proxy_addr})
        opener = request.build_opener(proxy,request.HTTPHandler)
        request.install_opener(opener)
        data = request.urlopen(req).read()
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        # 若为url异常延时1秒执行
        time.sleep(1)
    except Exception as e:
        print("exception:"+str(e))
        #若为exception异常延时一秒
        time.sleep(1)

# 设置关键词
key = "Python"
#设置代理服务器
proxy = "127.0.0.1:8888"
#爬多少页
for i in range(0,5):
    key = request.quote(key)
    this_page_url = ""
    # a = "http://blog.csdn.net"
    this_page_data = use_proxy(proxy,this_page_url)
    print(len(str(this_page_data)))
    pat1 = '<a href="(.*?)"'
    # 这里的S表示.可以匹配多行
    rs1 = re.compile(pat1,re.S).findall(str(this_page_data))
    if len(rs1)==0:
        print("第"+str(i)+"页未成功")
        continue
    for j in range(0,len(rs1)):
        t_url = rs1[j]
        this_url = t_url.replace("amp;","")
        file = "/home/pyvip/crawler/weixin/第"+str(i)+"页第"+str(j)+"篇文章.html"
        this_data = use_proxy(proxy,this_url)
        try:
            fh = open(file,"wb")
            fh.write(this_data)
            fh.close()
            print("第"+str(i)+"页第"+str(j)+"篇文章成功下载")
        except Exception as e :
            print(e)
            print("第"+str(i)+"页第"+str(j)+"篇文章爬取失败")




