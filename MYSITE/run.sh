# run in background with this command
# nohup python manage.py runserver 0.0.0.0:8999 &

echo "$1 is 5? " 
if (( $1 == 5 ))
then
    echo "===> Otion $1: starting server"
    python manage.py runserver 0.0.0.0:8999
else
    echo "===> Otion $1: starting server"
    nohup python manage.py runserver 0.0.0.0:8999 &
fi

if (( $1 == 'b' ))
then
    echo "background"
fi
