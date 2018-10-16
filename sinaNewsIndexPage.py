from urllib import request,error
import urllib
import re

data = request.urlopen("http://news.sina.com.cn/").read()
data2 = data.decode("utf-8","ignore")
pat = 'href="(http://news.sina.com.cn/.*?)"'
url_list = re.compile(pat).findall(data2)
for i in range(0,len(url_list)):
    try:
        print("第{}次爬取".format(i))
        this_url = url_list[i]
        file = "/home/pyvip/crawler/sinaNews/"+str(i)+".html"
        request.urlretrieve(this_url,file)
        print("*****成功*****")
    except error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)