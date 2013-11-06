#!/bin/bash

RANGE=101

number=$RANDOM
let "number %= $RANGE"

echo "掷出了 $number 上限为 100"
