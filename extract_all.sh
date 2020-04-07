#!/bin/sh
zip_files=`find . -name '*.zip'`

for zip_file in $zip_files;
do
    unzip -d "$tar_file" $tar_file
done;
