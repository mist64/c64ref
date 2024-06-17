./generate.py > $1/index.html

cp -p *.css *.js $1

mkdir -p $1/bin
cp -p bin/*.bin $1/bin
