# 京东商品信息打印案例
import requests
import re


# 发起网页请求
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


# 爬取页面信息
def parsePage(ilt, html):
    try:  # 分析页面，提取信息
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):  # 循环写入
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


# 输出打印
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"  # 打印模板
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0  # 计数器
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

# 主函数
def main():
    goods = '书包' # 请求参数
    depth = 3 # 打印深度
    start_url = 'https://search.jd.com/Search?keyword=' + goods + '&enc=utf-8&wq=' + goods
    infoList = []  # 接收列表
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(56 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()
