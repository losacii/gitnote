#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
pairs = (
    ('~/.bashrc',               'confiles/_bashrc'),
    ('~/.bash_aliases'          'confiles/_bash_aliases'),
    ('~/.config/i3/config',     'confiles/_i3config'),
    ('~/.i3status.conf',        'confiles/_i3status.conf'),
    ('~/.inputrc'               'confiles/_inputrc'),
    ('~/.xinitrc',              'confiles/_xinitrc'),
    ('/etc/default/keyboard',   'confiles/_etc.default.keyboard'),
    ('~/.SpaceVim.d/init.toml', 'confiles/xxxxxxxxxxxxxxxx'),
    ('~/.SpaceVim.d/config/init.vim'),
    ('~/.vim/myVimrc.vim'),
)
print(pairs)
