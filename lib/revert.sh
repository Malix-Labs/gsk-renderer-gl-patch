#!/bin/sh

. /usr/lib/gsk-renderer-gl-patch/variables.sh

sed -i '/^GSK_RENDERER=gl$/d' "$CONF_FILE"

. /usr/lib/gsk-renderer-gl-patch/reboot.sh
