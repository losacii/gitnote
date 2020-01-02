# run in background with this command
# nohup python manage.py runserver 0.0.0.0:8999 &

echo "$1" 
if (( $1 == 0 ))
then
    echo "===> Otion $1: starting server"
    python manage.py runserver 0.0.0.0:8999
elif (( $1 == 1 ))
then
    echo "===> Otion $1: starting server, on background..."
    nohup python manage.py runserver 0.0.0.0:8999 &
else
    echo "===> something else..."
fi
