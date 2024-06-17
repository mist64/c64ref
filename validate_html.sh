# #!/bin/sh

# Using https://validator.github.io/validator/


DIRECTORY_PATH="out"

REGEXP=".*(" # open regex

# TODO: XXX fix

# > duplicate ID
REGEXP="${REGEXP}Duplicate.ID|The.first.occurrence.of.ID"

 # > unescaped <Akku> <STOP> from kernal txts
REGEXP="${REGEXP}|not.allowed.as.child.of.element|Unclosed.element|but.there.were.open.elements|Bad.character|violates.nesting.rules"
# > unescaped <> from c64mem
REGEXP="${REGEXP}|Probable.causes..Unescaped"

REGEXP="${REGEXP}).*" # close regex

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
