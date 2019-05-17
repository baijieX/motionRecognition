#!/bin/bash

a=`./examples/divideData.py && ./examples/trainData.py && ./examples/testData.py` 
b=`./examples/divideData.py && ./examples/trainData.py && ./examples/testData.py` 
echo $a
echo $b
let c=a+b
echo $c
