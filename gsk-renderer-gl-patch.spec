Name: gsk-renderer-gl-patch
Summary: Patch for GSK rendering issues (sets GSK_RENDERER=gl)
Version: 1.0.4
Release: 1%{?dist}
URL: https://github.com/Malix-Labs/%{name}
Source0: %{url}/releases/tag/%{name}-%{version}.tar.gz
License: unlicense
Group: System/Configuration/Files
Requires: sed

%description
Patch for GSK rendering issues (sets GSK_RENDERER=gl)

%prep
%setup -q

%build
# Nothing to build

%install
install -D -m 544 src/main.sh %{buildroot}%{_bindir}/%{name}
install -D -m 544 lib/set.sh %{buildroot}%{_libexecdir}/%{name}/set.sh
install -D -m 544 lib/revert.sh %{buildroot}%{_libexecdir}/%{name}/revert.sh
install -D -m 544 lib/reboot.sh %{buildroot}%{_libexecdir}/%{name}/reboot.sh
install -D -m 544 lib/variables.sh %{buildroot}%{_libexecdir}/%{name}/variables.sh

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}/set.sh
%{_libexecdir}/%{name}/revert.sh
%{_libexecdir}/%{name}/reboot.sh
%{_libexecdir}/%{name}/variables.sh
%doc docs/*
%license LICENSE

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
