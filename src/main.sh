#!/bin/bash

if [ "$1" == "set" ]; then
	# shellcheck source=lib/set.sh
	. /usr/lib/set.sh
elif [ "$1" == "revert" ]; then
	# shellcheck source=lib/revert.sh
	. /usr/lib/revert.sh
else
	echo "Invalid argument. Use 'set' or 'revert'."
fi
