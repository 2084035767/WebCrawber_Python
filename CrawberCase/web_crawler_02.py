# 京东商品案例
# import requests
#
# url = 'https://item.jd.com/100019791896.html'
#
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[:100])
# except:
#     print("error")

# 百度关键词案例
# import requests
#
# url = 'https://www.baidu.com/s'
# kv = {'wd': 'python'}
# try:
#     r = requests.get(url, params=kv)
#     print(r.request.url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(len(r.text))
#     r.close()
# except:
#     print("error")

# 图片的爬取与存储
# import requests
# import os
#
# url = 'https://w.wallhaven.cc/full/9m/wallhaven-9mjoy1.png'
# root = 'F:\python\pystudy'
# path = root + url.split('/')[-1]
#
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     elif not os.path.exists(path):
#         r = requests.get(url)
#         with open(path, 'wb') as f:
#             f.write(r.content)
#             f.close()
#     else:
#         print('文件已存在')
# except:
#     print("error")

# IP地址查询案例
import requests

url = 'https://www.ip138.com/iplookup.asp?ip='
try:
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("error")
