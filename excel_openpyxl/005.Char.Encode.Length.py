def str_byte_len(s):
    return len(s.encode('utf-8'))

x = str_byte_len('hello world!')
y = str_byte_len('自发')
print(x, y) # 12 6

