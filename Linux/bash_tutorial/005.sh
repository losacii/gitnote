#! /bin/bash
sum=0
x=0

while (( $x <= 100 ))
do
    sum=$((sum+x))
    x=$((x+1))
done

echo $sum
