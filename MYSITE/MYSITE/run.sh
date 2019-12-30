# python manage.py runserver 0.0.0.0:8000

# run in background with this command
# nohup python manage.py runserver 0.0.0.0:8999 &

echo "$1 is 5? " 
if (( $1 == 5 ))
then
    echo "Yes"
else
    echo "No, it is $1"
fi

if (( $1 == 'b' ))
then
    echo "background"
fi
