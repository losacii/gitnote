# run in background with this command
# nohup python manage.py runserver 0.0.0.0:8999 &

echo "$1" 
if (( $1 == 0 ))
then
    echo "===> Otion $1: Syncing to Gitnote"
    rsync -arP --delete ../MYSITE/ ~/gitnote/MYSITE/
elif (( $1 == 1 ))
then
    echo "===> Otion $1: Syncing From Gitnote..."
    rsync -arP --delete ~/gitnote/MYSITE/ ../MYSITE/
else
    echo "===> something else..."
fi
