from random import choice

di = {}

for _ in range(10000):
    r = choice(('Zhang', 'Wang', 'Li', 'Ma'))
    print('===> Dict randomly gets value', r)
    if str(r) in di.keys():
        di[str(r)] += 1
    else:
        di[str(r)] = 1

print("\n===> Value Count:")
for key in di:
    print("{:8} ~ {:4} counts".format(key, di[key]))

print("\n===> Sorted:")
for k in sorted(di, key=di.__getitem__, reverse=True):
    print("{:8} ~ {:4} counts".format(k, di[k]))


# print(di.keys())
# print(di.values())
# print('old' in di.values()) # False
# print('very old' in di.values()) # True
# print(5 in di.values()) # True


# Binary sort Application

# data Visualization

# Ultisnippets: repn!!

# Fuzzy Finder: Ctrlp

# NerdTree

# coc, kite, neocomplete, NCM2
# ici
# flygrep
# emmet

'''
    - ici.vim: OK
    - fzf: OK
    - fzf.vim: OK
    - vim-sneak: OK
    - FlyGrep.vim: OK
    - vim-highlightedyank: OK
    - vim-snippets: OK
    - nerdtree: OK
    - ultisnips: OK
    - emmet-vim: OK
    - vim-surround: OK
    - auto-pairs: OK
    - nerdcommenter: OK
    - vim-airline: OK
    - nvim-yarp: OK
    - ncm2: OK
        - vim-lsp: OK
        - ncm2-vim-lsp: OK
        - async.vim: OK
        - ncm2-look.vim: OK
        - nc.vim: OK
        - ncm2-bufword: OK
        - ncm2-path: OK
    - molokai: OK

'''
