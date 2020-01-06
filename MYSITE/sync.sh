# run in background with this command
# nohup python manage.py runserver 0.0.0.0:8999 &

echo "$1" 
if (( $1 == 0 ))
then
    echo "===> Otion $1: Local over Gitnote"
    rsync -arP --delete ~/dev/src/MYSITE/ ~/gitnote/MYSITE/
elif (( $1 == 1 ))
then
    echo "===> Otion $1: Gitnote Over Local"
    rsync -arP --delete ~/gitnote/MYSITE/ ~/dev/src/MYSITE/
else
    echo "===> something else..."
fi
