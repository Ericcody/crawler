import requests
import codecs
from bs4 import BeautifulSoup
#codecs 包便于处理中文编码
# 爬取页面的url
DOWNLOAD_URL = 'https://movie.douban.com/top250/'


def download_page(url):
    """
    获取url页面内容，返回页面的html源代码
    """
    # header 设置请求头来模拟浏览器登陆，User-Agent 用来表示浏览器类型 这里设置为欸chrome
    # 服务器通过校验请求的U-A来识别爬虫，这算是最简单的一种反爬虫机制了，通过模拟浏览器的U-A，能够很轻松地绕过这个问题
    headers = {
        'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    data = requests.get(url,headers=headers).content
    return data


def parse_html(html):
    # 创建BeautifulSoup对象
    soup = BeautifulSoup(html,'html.parser')
    # 查找class为grid_view的ol标签，得到电影集合
    movie_list_soup = soup.find('ol',attrs={'class':'grid_view'})

    movie_name_list = []
    # 解析每个电影，即使解析每个li标签
    for movie_li in movie_list_soup.find_all('li'):
        # li中的类名为hd的块标签div对应每个电影的具体信息，包括标题图片，链接等
        detail = movie_li.find('div',attrs={'class':'hd'})
        # 得到电影名
        movie_name = detail.find('span',attrs={'class':'title'}).getText()
        # print(movie_name)
        movie_name_list.append(movie_name)

    # 循环结束，跳至下一页，找到下一页标签，类名为next的span标签，具体链接在span标签的a标签中
    next_page = soup.find('span',attrs={'class':'next'}).find('a')
    # 如果a 标签不存在了，就说明到最后一页了，
    if next_page:
        # 存在a标签 则返回电影名列表，和下一页的链接
        return movie_name_list,DOWNLOAD_URL + next_page['href']
    return movie_name_list,None


def main():
    """
    爬虫主程序
    """
    url = DOWNLOAD_URL

    # 将爬去到的电影名写入movies文件
    with codecs.open('movies','wb',encoding='utf-8') as fp:
        while url :
            html = download_page(url)
            movies,url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))
    # print (download_page(DOWNLOAD_URL))

if __name__ == '__main__':
    main()