#!/bin/bash

if [ "$1" == "set" ]; then
	./lib/set.sh
elif [ "$1" == "revert" ]; then
	./lib/revert.sh
else
	echo "Invalid argument. Use 'set' or 'revert'."
fi
