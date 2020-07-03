# echo & echom
echo
echom   ~   echom will save the output
            and let you run :message to view it later

# comments
use " at beginning of line

# Setting Options
:set number
:set nu
:set number!

:set relativenumber
:set relativenumber! (toggle boolean option)

# Checking Options
:set number?
:set nu?
:set rnu? (relativenumber)

# Options with values
:set number
:set numberwidth=4

:set wrap
:set shiftround
:set matchtime

# Setting multiple Options at Once
:set number numberwidth=6

# Mapping
map <space> <c-w>w
map <c-d> dd
* Dont put " comment after a mapping line


