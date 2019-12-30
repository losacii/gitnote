import os
import sys
import time

# sys.stdout.write("Work Directory: ")
# os.system("pwd")
# time.sleep(0.2)
# 
# print(os.listdir("."))
# 
# print("Dir Name:")
print(os.path.dirname(__file__))
print('\n' * 16)




'''

snippet t "A simple HTML tag" b
<${1:div}>
    hello world
</${1/(\w+).*/$1/}>
endsnippet

snippet todo "TODO reminder" b
<!-- TODO: `echo $USER` ${1:description} -->
endsnippet

snippet vstm "Vimscript time"
`!v strftime("%c")`
endsnippet
	

snippet 'rep (\d+) (\S+)' "repeat word n times" r
`!p 
count = int(match.group(1))
snip.rv = count * (match.group(2) + ' ')`
endsnippet

snippet 'repn (\d+) (.+)' "repeat word n times" r
`!p 
count = int(match.group(1))
word = match.group(2)
snip.rv = count * (word + '\n')`
endsnippet

'''
