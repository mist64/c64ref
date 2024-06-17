# charset generate script

# $1 base directory
# $2 folder name

DIR=$1/$2
mkdir -p $DIR

./generate.py > $DIR/index.html

cp -p ../style.css $1
cp -p *.css *.js $DIR

mkdir -p $DIR/bin
cp -p bin/*.bin $DIR/bin
