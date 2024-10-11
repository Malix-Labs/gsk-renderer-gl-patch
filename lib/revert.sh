#!/bin/sh

. ./lib/variables.sh

sed -i '/^GSK_RENDERER=gl$/d' "$CONF_FILE"

. ./lib/reboot.sh
