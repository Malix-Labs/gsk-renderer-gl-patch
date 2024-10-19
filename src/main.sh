#!/bin/bash

if [ "$1" == "set" ]; then
	. /usr/lib/set.sh
elif [ "$1" == "revert" ]; then
	. /usr/lib/revert.sh
else
	echo "Invalid argument. Use 'set' or 'revert'."
fi
