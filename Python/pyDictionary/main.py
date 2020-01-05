import requests
from bs4 import BeautifulSoup
import os
import sys

# 获取当前终端的宽度和高度
rows, columns = os.popen('stty size', 'r').read().split()

TERM_WIDTH = int(columns) # 宽度

def blit(s):
    l = 0
    words = s.split(' ')
    for word in words:
        if l + len(word) >= TERM_WIDTH:
            sys.stdout.write('\n')
            l = len(word) + 1
        else:
            l += len(word) + 1
        sys.stdout.write(word + ' ')


def blit1(s, padding):
    sys.stdout.write(' ' * (padding + 2))
    l = padding + 2
    words = s.split(' ')
    for word in words:
        if l + len(word) >= TERM_WIDTH - padding:
            sys.stdout.write('\n' + ' ' * padding)
            l = len(word) + 1 + padding
        else:
            l += len(word) + 1
        sys.stdout.write(word + ' ')


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
            blit1(p.text, 3); sys.stdout.write('\n')
    print(" ~" * 32)

    # print(soup.b)  # first bold tag
    # print(soup.p)  # first p tag
    # find_all returns a list

    #lists = soup.find_all('p', {'class': 'short'})


def dict_youdao(word):
    url0 = "http://youdao.com/example/blng/eng/{}/#keyfrom=dict.main.moreblng"

    # 根据 url 获取内容
    result = requests.get(url0.format(word));
    src = result.content

    soup = BeautifulSoup(src, 'lxml')
    #soup = BeautifulSoup(src, 'html.parser')

    tagsx = soup.find('div', {'id':'bilingual'}).find_all('p', {'class': None})
    example_count = 0
    for t in tagsx:
        text = t.text.strip('\n')
        blit1(text, 3); sys.stdout.write('\n')
        if contains_chinese(text):
            print()
            example_count += 1
            if example_count >= 7: break

if __name__ == '__main__':
    word = sys.argv[1]
    dict_vocabulary(word)
    dict_youdao(word)
    
