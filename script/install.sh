#!/bin/sh

mkdir -p %{buildroot}%{_sysconfdir}/environment.d/
if ! grep -q "GSK_RENDERER=gl" %{buildroot}%{_sysconfdir}/environment.d/gsk.conf; then
  echo "GSK_RENDERER=gl" >> %{buildroot}%{_sysconfdir}/environment.d/gsk.conf
fi
