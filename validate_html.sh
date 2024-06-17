# #!/bin/sh

# Using https://validator.github.io/validator/


DIRECTORY_PATH="out"

REGEXP=".*(" # open regex
REGEXP="${REGEXP}Empty.heading|Duplicate.ID|The.first.occurrence.of.ID" # fix laters
REGEXP="${REGEXP}|exceeded.the.column.count.established|not.allowed.as.child.of.element|Use.CSS.instead|Unclosed.element|Bad.character|but.there.were.open.elements|violates.nesting.rules|Probable.causes..Unescaped"
REGEXP="${REGEXP}).*" # close regex

# Empty.heading: c64disasm/c64disasm_en.txt above RRBY

#REGEXP="" # no filter, all errors/warnings

# show info/warnings and errors
PARAMS='--format gnu --asciiquotes '$DIRECTORY_PATH

# only show errors
#PARAMS='--errors-only '$PARAMS

HTML_PARAMS='--filterpattern '$REGEXP' '$PARAMS

echo $HTML_PARAMS

#echo "HTML:"
vnu --skip-non-html $HTML_PARAMS

# echo -e "\n\n\n CSS:"
# vnu --skip-non-css  $PARAMS
#
# echo -e "\n\n\n SVG:"
# vnu --skip-non-svg  $PARAMS
