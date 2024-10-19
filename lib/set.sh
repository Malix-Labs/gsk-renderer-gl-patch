#!/bin/sh

. /usr/lib/gsk-renderer-gl-patch/variables.sh

mkdir -p "$ENV_DIR"
echo "GSK_RENDERER=gl" >>"$CONF_FILE"

. /usr/lib/gsk-renderer-gl-patch/reboot.sh
