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

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/gsk-renderer-gl-patch << 'EOF'
#!/bin/bash
echo "Setting GSK_RENDERER to gl"
export GSK_RENDERER=gl
echo "%{reboot_needed_message}"
EOF
chmod +x %{buildroot}%{_bindir}/gsk-renderer-gl-patch

%files
%{_bindir}/gsk-renderer-gl-patch

%post
echo "To apply the patch, run 'gsk-renderer-gl-patch' and then reboot your system."

%changelog
* 2024-10-11T13:20:54Z Malix <alixbrunetcontact@gmail.com> - 1.0
- Initial Release
