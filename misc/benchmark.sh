#!/bin/bash
# generate a number of files with random sizes in a range

set -e

nofiles=2048 # number of files
 
mkdir -p test_files
rm -rf speed_test.csv
touch speed_test.csv

echo "File Size (KBs), Haesh Time, Sha512 Time, Sha256 Time, Sha1 Time, md5 Time" > speed_test.csv

for i in `eval echo {1..$nofiles}`
do
    touch ./test_files/file$i

    # create files in 512 byte increments
    dd count=$i if=/dev/urandom of=./test_files/file$i

    # get haesh time
    start_time=`date +%s%N`
    ./haesh.py -f ./test_files/file$i
    end_time=`date +%s%N`
    haesh_time=$(expr $end_time - $start_time)

    # get sha512
    start_time=`date +%s%N`
    sha512sum ./test_files/file$i
    end_time=`date +%s%N`
    sha512sumtime=$(expr $end_time - $start_time)

    # get md5 time
    start_time=`date +%s%N`
    md5sum ./test_files/file$i
    end_time=`date +%s%N`
    md5sum_time=$(expr $end_time - $start_time)

    # get sha1 time
    start_time=`date +%s%N`
    sha1sum ./test_files/file$i
    end_time=`date +%s%N`
    sha1sum_time=$(expr $end_time - $start_time)

    # get sha256
    start_time=`date +%s%N`
    sha256sum ./test_files/file$i
    end_time=`date +%s%N`
    sha256sum_time=$(expr $end_time - $start_time)

    kb_value=$(echo 'scale=2; ($i * 512)/1024' | bc)

    echo "${kb_value}, ${haesh_time}, ${sha512sumtime}, ${sha256sum_time}, ${sha1sum_time}, ${md5sum_time}" >> speed_test.csv

    rm ./test_files/file$i

done
