# c64mem generate script

# $1 base directory
# $2 folder name

DIR=$1/$2
mkdir -p $DIR

./generate.py > $DIR/index.html

cp -p ../style.css $1

# the c64mem_*.txt files are only used for generating index.html
# format.py and symbols.txt are helpers for adding symbols to new txts
# texteinschub.md is some addition that is here for completeness
