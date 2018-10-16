import re
import threading
from urllib import request

headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0;win64;x64;rv:61.0) Gecko/20100101 Firefox/61.0")
opener = request.build_opener()
opener.addheaders=[headers]
request.install_opener(opener)
# for i in range(1,5):
#     url = ""
#     page_data = request.urlopen(url).read().decode("utf-8","ignore")
#     pat = ''
#     data_list = re.compile(pat,re.S).findall(page_data)
#     for j in range(0,len(data_list)):
#         print("第"+str(i)+"页第"+str(j)+"个段子内容是：")
#         print(data_list[j])


# 多线程模式
class One(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1, 30,2):
            url = ""
            page_data = request.urlopen(url).read().decode("utf-8", "ignore")
            pat = ''
            data_list = re.compile(pat, re.S).findall(page_data)
            for j in range(0, len(data_list)):
                print("第" + str(i) + "页第" + str(j) + "个段子内容是：")
                print(data_list[j])

class Two(threading.Thread):
    # 爬偶数页
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0, 30,2):
            url = ""
            page_data = request.urlopen(url).read().decode("utf-8", "ignore")
            pat = ''
            data_list = re.compile(pat, re.S).findall(page_data)
            for j in range(0, len(data_list)):
                print("第" + str(i) + "页第" + str(j) + "个段子内容是：")
                print(data_list[j])
# 开启线程
one = One()
two = Two()
one.start()
two.start()


# 多线程例子
# class A(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         for i in range(0,10):
#             print("我是线程A")
# class B(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         for i in range(0,10):
#             print("我是线程B")
#
# t1 = A()
# t1.start()
# t2 = B()
# t2.start()


