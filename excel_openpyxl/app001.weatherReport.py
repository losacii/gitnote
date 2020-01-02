import requests
import random
from bs4 import BeautifulSoup

url = 'http://www.weather.com.cn/weathern/101170105.shtml' # 数据地址,从浏览器copy
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400'
}
timeout = random.choice(range(80, 180)) # 超时时间
req = requests.get(url, headers=header, timeout=timeout) 
req.encoding = 'utf-8' # 防止中文乱码
code = req.status_code # 返回状态,200代表OK
print(code)




soup = BeautifulSoup(req.text, 'html.parser')

# 分析得 <ul class="t clearfix"> 标签下记录了我们想要的数据,因此只需要解析这个标签即可
ul_tag = soup.find('li', 'date-container')  # 利用 css 查找
print(ul_tag) # 取出七天数据


# 打印每一天数据
li_tag = ul_tag.findAll('li') 
for tag in li_tag:
    print(tag.find('h1').string)  # 时间
    print(tag.find('p', 'wea').string)  # wea
    # 温度的tag格式不统一,做容错
    try:
        print(tag.find('p', 'tem').find('span').string)  # 高温
        print(tag.find('p', 'tem').find('i').string)  # 低温
    except:
        print('没有高温或低温数据')
        pass
    print(tag.find('p', 'win').find('i').string)  # win
    print("_______________ 分割线 ____________________")
