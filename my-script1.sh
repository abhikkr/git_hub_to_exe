#!/bin/sh
echo "Enter the git link:"
echo
read git_link
git clone $git_link
python3 check_file.py
dir=$(ls -t | head -n1)
echo "$dir"
#rm -rf $dir