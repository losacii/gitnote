# check if file exists
FILE=/home/vi/.bashrc
if [ -f "$FILE" ]; then
    echo "\"$FILE\" --> file EXIST."
else
    echo "\"$FILE\" --> not exist"
fi
