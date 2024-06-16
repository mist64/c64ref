# charset resources

./generate.py > $1/index.html

cp -p ../style.css $1
cp -p *.css *.js $1

mkdir $1/bin
cp -p bin/*.bin $1/bin
