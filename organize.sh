#!/bin/sh
for student in *;
do
    cd "$student"
    mkdir q1 q2 q3
    file=`find . -name "*q1*.c"`
    if [ -z "$file" ]
    then
        file=`find . -name "1.c"`
    fi
    mv "$file" q1/
    file=`find . -name "*q2*.c"`
    if [ -z "$file" ]
    then
        file=`find . -name "2.c"`
    fi
    mv "$file" q2/
    file=`find . -name "*q3*.c"`
    if [ -z "$file" ]
    then
        file=`find . -name "3.c"`
    fi
    mv "$file" q3/
    cd ..
done;
