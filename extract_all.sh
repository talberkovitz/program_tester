#!/bin/sh
zip_files=`find . -name '*.zip'`

for zip_file in *.zip;
do
    unzip -d "${zip_file:0:$((${#zip_file} - 4))}" "$zip_file"
done;
