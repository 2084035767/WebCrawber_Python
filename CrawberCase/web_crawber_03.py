import requests
from bs4 import BeautifulSoup
import bs4


# 获取目标网址的文本信息
def getHtmlText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"


# 通过BeautifulSoup库解析网页，将需要的信息加入到一个列表中
def fillUnivList(ulist, demo):
    soup = BeautifulSoup(demo, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):  # 判断tr标签是不是bs4定义的tag标签，过滤掉其它的
            tds = tr.find_all('td')  # 将td标签内容加入到tds列表中
            aa = tds[1].find("a").string  # 因为大学名字在td标签的子标签a中，所以需要单独提取
            ulist.append([tds[0].string, aa, tds[4].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}{1:{3}^10}{2:^10}"
    print(tplt.format("序号", "学校名称", "分数", chr(12288)))  # 中文空格填充，能保证输出对齐
    for i in range(num):
        u = ulist[i]
        a = u[0].strip()  # 去掉字符串类两边的空格
        b = u[1].strip()
        c = u[2].strip()
        print(tplt.format(a, b, c, chr(12288)))


def main():
    url = "https://www.shanghairanking.cn/rankings/bcur/2020"
    ulist = []
    demo = getHtmlText(url)
    fillUnivList(ulist, demo)
    printUnivList(ulist, 30)


main()
