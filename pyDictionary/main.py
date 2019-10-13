import requests
from bs4 import BeautifulSoup
import sys

#检验是否含有中文字符
def contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

def dict_vocabulary(word):
    url1 = "http://www.vocabulary.com/dictionary/{}".format(word)

    # 根据 url 获取内容
    result = requests.get(url1); # print(result.status_code) # 200, 404
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')

    # 获取标签列表
    print(" ~" * 32)
    ptags = soup.find_all('p')
    for p in ptags:
        if p.attrs:
            print(p.text, '\n')
    print(" ~" * 32)

    # print(soup.b)  # first bold tag
    # print(soup.p)  # first p tag
    # find_all returns a list

    #lists = soup.find_all('p', {'class': 'short'})


def dict_youdao(word):
    url1 = "https://www.youdao.com/example/blng/eng/thug/#keyfrom=dict.main.moreblng"

    # 根据 url 获取内容
    result = requests.get(url1);
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')

    tagsx = soup.find('div', {'id':'bilingual'}).find_all('p', {'class': None})
    example_count = 0
    for t in tagsx:
        text = t.text.strip('\n')
        print(text)
        if contains_chinese(text):
            print()
            example_count += 1
            if example_count >= 8: break

if __name__ == '__main__':
    word = sys.argv[1]
    dict_vocabulary(word)
    #dict_youdao(word)
    
