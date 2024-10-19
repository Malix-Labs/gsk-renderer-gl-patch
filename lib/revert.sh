#!/bin/sh

# shellcheck source=lib/variables.sh
. /usr/lib/gsk-renderer-gl-patch/variables.sh

sed -i '/^GSK_RENDERER=gl$/d' "$CONF_FILE"

# shellcheck source=lib/reboot.sh
. /usr/lib/gsk-renderer-gl-patch/reboot.sh
