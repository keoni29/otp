#!/bin/sh

mkdir $1 || exit

for i in $(seq 1 $2); do echo "Generating key \#" $i "!" && dd if=/dev/urandom of=$1/$1-$i.otp bs=65K count=1; done

zip -r otpkeys-$1.zip $1

