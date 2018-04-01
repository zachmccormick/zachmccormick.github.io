#! /bin/bash

# fixes markdown using fmt
for f in $(find . -name '*.md') 
do 
    fmt -w 120 $f > $f.tmp
    mv $f.tmp $f
done

