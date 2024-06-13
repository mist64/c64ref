# #!/bin/sh

# Using https://validator.github.io/validator/


DIRECTORY_PATH="out out_unmodified"

REGEXP=".*(Trailing.slash|Consider.adding.a..lang.|Consider.using.the..h1..element.as.a.top.level.heading.only|Stray.end.tag|Duplicate.ID|The.first.occurrence.of.ID|row.group.established.by.a|exceeded.the.column.count.established|not.allowed.as.child.of.element|Use.CSS.instead|Unclosed.element|Bad.character|but.there.were.open.elements|cannot.be.represented.as.XML|A.slash.was.not.immediately.followed.by|not.allowed.on.element|violates.nesting.rules|is.not.serializable.as.XML|Probable.causes..Unescaped|Probable.cause..Matching.quote.missing|missing.immediately.before|Probable.cause..Missing|an.element.of.the.same.type.was.already.open|Empty.heading|No.space.between.attributes|Duplicate.attribute).*"


#REGEXP="" # no filter, all errors/warnings

# show info/warnings and errors
PARAMS='--format gnu --asciiquotes '$DIRECTORY_PATH

# only show errors
#PARAMS='--errors-only '$PARAMS

HTML_PARAMS='--filterpattern '$REGEXP' '$PARAMS

echo $HTML_PARAMS

echo "HTML:"
vnu --skip-non-html $HTML_PARAMS

# echo -e "\n\n\n CSS:"
# vnu --skip-non-css  $PARAMS
#
# echo -e "\n\n\n SVG:"
# vnu --skip-non-svg  $PARAMS
