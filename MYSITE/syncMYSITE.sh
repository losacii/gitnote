if [ $1 -eq 0  ]
then
    echo "\n <<<=== backward <<<"
    rsync -arP --delete ~/gitnote/MYSITE/ ~/dev/src/MYSITE/
elif [ $1 -eq 1  ]
then
    echo "\n >>>=== forward >>>"
    rsync -arP --delete ~/dev/src/MYSITE/ ~/gitnote/MYSITE/
else
    echo "Something Else"
fi
