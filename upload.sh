scp style.css            $1:/var/www/c64ref/

(cd c64disasm; ./combine.py > index.html)
scp c64disasm/index.html $1:/var/www/c64ref/c64disasm/

(cd c64mem; ./combine.py > index.html)
scp c64mem/index.html    $1:/var/www/c64ref/c64mem/

(cd kernal; ./generate.py > index.html)
scp kernal/index.html    $1:/var/www/c64ref/kernal/
