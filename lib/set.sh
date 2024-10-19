#!/bin/sh

# shellcheck source=lib/variables.sh
. /usr/lib/gsk-renderer-gl-patch/variables.sh

mkdir -p "$ENV_DIR"
echo "GSK_RENDERER=gl" >>"$CONF_FILE"

# shellcheck source=lib/reboot.sh
. /usr/lib/gsk-renderer-gl-patch/reboot.sh
