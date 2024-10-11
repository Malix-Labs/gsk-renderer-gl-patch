Name: gsk-renderer-gl-patch
Summary: Patch for GSK rendering issues (sets GSK_RENDERER=gl)
Version: 1.0.4
Release: 1%{?dist}
License: unlicense
Group: System/Configuration/Files
Requires: sed

%description
Patch for GSK rendering issues (sets GSK_RENDERER=gl)

%install
install -D -m 0544 %{_sourcedir}/src/main.sh %{buildroot}/usr/bin/gsk-renderer-gl-patch
install -D -m 0544 %{_sourcedir}/lib/set.sh %{buildroot}/usr/lib/gsk-renderer-gl-patch/set.sh
install -D -m 0544 %{_sourcedir}/lib/revert.sh %{buildroot}/usr/lib/gsk-renderer-gl-patch/revert.sh
install -D -m 0544 %{_sourcedir}/lib/reboot.sh %{buildroot}/usr/lib/gsk-renderer-gl-patch/reboot.sh
install -D -m 0544 %{_sourcedir}/lib/variables.sh %{buildroot}/usr/lib/gsk-renderer-gl-patch/variables.sh

%files
/usr/bin/gsk-renderer-gl-patch
/usr/lib/gsk-renderer-gl-patch/set.sh
/usr/lib/gsk-renderer-gl-patch/revert.sh
/usr/lib/gsk-renderer-gl-patch/reboot.sh
/usr/lib/gsk-renderer-gl-patch/variables.sh

%post
gsk-renderer-gl-patch set

%preun
gsk-renderer-gl-patch revert

%changelog
* Fri Oct 11 2024 Malix <alixbrunetcontact@gmail.com> 1.0.4-1
- yes test tito

* Fri Oct 11 2024 Malix-off <alixbrunetcontact@gmail.com> 1.0.3-1
- enhance: change perm (alixbrunetcontact@gmail.com)

* Fri Oct 11 2024 Malix <alixbrunetcontact@gmail.com>
- new package built with tito
