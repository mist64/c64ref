# 6502 generate script

# $1 base directory
# $2 folder name

DIR=$1/$2
mkdir -p $DIR

cp -p index.html $DIR

cp -p ../style.css $1
cp -p *.js cpu_*.txt $DIR

# there are four svgs that are not copied: TODO: XXX maybe add them?
