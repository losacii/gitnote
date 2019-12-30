cat << emt

echo $1
if [ $1 -eq 0  ]
then
    echo "go"
elif [ $1 -eq 1  ]
then
    echo "back"
else
    echo "something else..."
fi

emt

echo $1
if [ $1 -eq 0  ]
then
    echo "go"
elif [ $1 -eq 1  ]
then
    echo "back"
else
    echo "something else..."
fi
