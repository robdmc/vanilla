#! /usr/bin/env bash

rm -rf env 2>/dev/null
virtualenv env
. ./env/bin/activate

pip install -e .
echo .  "`pwd`/env/bin/activate && cd `pwd`" > ~/rcvanilla.sh 
echo
echo
echo This project can now be activated by running the command
echo . ~/rcvanilla.sh 


