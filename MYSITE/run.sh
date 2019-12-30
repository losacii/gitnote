if [ $1 -eq 0  ]
then
    python manage.py runserver 0.0.0.0:8000
elif [ $1 -eq 1  ]
then
    nohup python manage.py runserver 0.0.0.0:8999 &
else
    echo "Something Else"
fi
