#!/bin/sh

mkdir -p "%{buildroot}%{_sysconfdir}/environment.d/"
echo "GSK_RENDERER=gl" >>"%{buildroot}%{_sysconfdir}/environment.d/gsk.conf"
