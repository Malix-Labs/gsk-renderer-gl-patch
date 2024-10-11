#!/bin/sh

. ./lib/variables.sh

mkdir -p "$ENV_DIR"
echo "GSK_RENDERER=gl" >>"$CONF_FILE"

. ./lib/reboot.sh
