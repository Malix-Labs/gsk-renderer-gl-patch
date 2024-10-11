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
%include src/set.sh

%post
echo %{reboot_needed_message}

%postun
if [ "$1" -eq 0 ]; then
  %include src/revert.sh
  echo %{reboot_needed_message}
fi

%files
%{_sysconfdir}/environment.d/gsk.conf
src/set.sh
src/revert.sh

%changelog
* 2024-10-11T13:20:54Z Malix <alixbrunetcontact@gmail.com> - 1.0
- Initial Release
