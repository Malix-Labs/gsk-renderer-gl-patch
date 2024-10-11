#!/bin/sh

sed -i '/^GSK_RENDERER=gl$/d' %{_sysconfdir}/environment.d/gsk.conf
