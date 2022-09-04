import requests

# 待爬取得URL地址
url = 'https://jiangtao.today/2022/06/13/%E5%A4%A7%E5%AD%A6%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9F%BA%E7%A1%80/'
# 模拟浏览器发请求
r = requests.get(url)
# res返回的状态码【成功：200 ；不成功：404】
print(r.status_code)
# 对数据编码
r.encoding = 'utf-8'
# # 保存数据
print(r.headers)
# with open('data.html', 'wb') as f:
#     f.write(r.content)
