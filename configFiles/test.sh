# check if file exists
fx=~/.bashrc
if [ -f "$fx" ]; then
    echo "$fx --> EXIST!"
else
    echo "$fx --> ERROR: NOT exist"
fi
