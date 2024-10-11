%define reboot_needed_message "Reboot needed to reload the \`GSK_RENDERER\` environment variable."

Name: gsk-renderer-gl-patch
Summary: Patch for GSK rendering issues (sets GSK_RENDERER=gl)
Version: 1.0.0
Release: 1%{?dist}
License: unlicense
Group: System/Configuration/Files
Requires: sed

%description
Patch for GSK rendering issues (sets GSK_RENDERER=gl)

%install
install -D -m 0755 src/main.sh %{buildroot}/usr/bin/gsk-renderer-gl-patch
install -D -m 0755 lib/set.sh %{buildroot}/usr/lib/gsk-renderer-gl-patch/set.sh
install -D -m 0755 lib/revert.sh %{buildroot}/usr/lib/gsk-renderer-gl-patch/revert.sh
install -D -m 0755 lib/reboot.sh %{buildroot}/usr/lib/gsk-renderer-gl-patch/reboot.sh
install -D -m 0755 lib/variables.sh %{buildroot}/usr/lib/gsk-renderer-gl-patch/variables.sh

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
* 2024-10-11T13:20:54Z Malix <alixbrunetcontact@gmail.com> - 1.0
- Initial Release
