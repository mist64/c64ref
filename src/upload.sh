#./generate.sh

rsync -P style.css            $1:/var/www/c64ref/
rsync -P c64disasm/index.html $1:/var/www/c64ref/c64disasm/
rsync -P c64mem/index.html    $1:/var/www/c64ref/c64mem/
rsync -P kernal/index.html    $1:/var/www/c64ref/kernal/
rsync -Pr charset/index.html charset/*.css charset/*.js charset/bin    $1:/var/www/c64ref/charset/

rsync -Pr colors/index.html colors/*.js $1:/var/www/c64ref/colors/
rsync -Pr 6502/index.html 6502/*.js 6502/cpu_*.txt $1:/var/www/c64ref/6502/
