#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
#echo "$BASEDIR"
#echo $BASEDIR/.venv/bin/python $BASEDIR/pycpulimit.py $@
$BASEDIR/.venv/bin/python $BASEDIR/pycpulimit.py $@

