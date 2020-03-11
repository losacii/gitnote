import requests
import re
from random import randint
from sys import stdout

res = requests.get('http://hq.sinajs.cn/list=s_sh000001')
res.encoding = res.apparent_encoding

rees = re.search('".*"', res.text)
resString = rees.group()

text = "SHN Now: {} {}".format(
    resString.split(',')[1], randint(100000, 999999))

stdout.write(text)

