#!bin/bash
if [ $# != 3 ]; then 
    for x in $(seq 100)
    do
        echo "You fool! You didn't enter enough arguments! Boo!"
    done
    sleep 2
    echo "You idiot."
    exit 1
fi
mkdir temp
cd temp
python ../walk2D.py $1 $2 $3
convert -delay 50 -loop 0 tmp_*.png ../walk.gif
rm *.png
cd ..
rmdir temp
