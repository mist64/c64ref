# c64io generate script

# $1 base directory
# $2 folder name

DIR=$1/$2
mkdir -p $DIR

./generate.py > $DIR/index.html

cp -p ../style.css $1
