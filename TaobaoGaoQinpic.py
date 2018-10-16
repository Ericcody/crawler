from urllib import request,error
import urllib
import re

key_name = "衬衫"
key = request.quote(key_name)
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0;win64;x64;rv:61.0) Gecko/20100101 Firefox/61.0")

opener = request.build_opener()
opener.addheaders=[headers]
request.install_opener(opener)
for i in range(0,2):
    url = "http://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&clk1=225714fdf13d1c3335dada307002ca55&keyword={}&page=".format(key)+str(i)
    data1 = request.urlopen(url).read()
    data = data1.decode("utf-8","ignore")
    print(data)
    pat = 'pic_url":"//(.*?)"'
    image_list = re.compile(pat).findall(data)
    print(image_list)
    for j in range(0,len(image_list)):
        this_img = image_list[j]
        this_img_url = "http://" + this_img
        file = "/home/pyvip/crawler/img/"+str(i)+str(j)+".jpg"
        request.urlretrieve(this_img_url,filename=file)
