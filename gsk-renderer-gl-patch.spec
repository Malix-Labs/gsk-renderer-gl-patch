Name: gsk-renderer-gl-patch
Version: 1.0.1
Release: 1%{?dist}
Summary: Patch for GSK rendering issues (sets GSK_RENDERER=gl)
License: unlicense
URL: https://github.com/Malix-Labs/%{name}
Source0: https://github.com/Malix-Labs/%{name}/releases/tag/%{name}-%{version}.tar.gz
Group: System/Configuration/Files
Requires: sed

%description
Patch for GSK rendering issues (sets GSK_RENDERER=gl)

%prep
%setup -q

%build
# Nothing to build

%install
install -D -m 544 ./src/main.sh %{buildroot}%{_bindir}/%{name}
install -D -m 544 ./lib/set.sh %{buildroot}%{_libdir}/%{name}/set.sh
install -D -m 544 ./lib/revert.sh %{buildroot}%{_libdir}/%{name}/revert.sh
install -D -m 544 ./lib/reboot.sh %{buildroot}%{_libdir}/%{name}/reboot.sh
install -D -m 544 ./lib/variables.sh %{buildroot}%{_libdir}/%{name}/variables.sh

%files
%license LICENSE
%doc docs/**
%dir %{_libdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}/set.sh
%{_libdir}/%{name}/revert.sh
%{_libdir}/%{name}/reboot.sh
%{_libdir}/%{name}/variables.sh

%post
gsk-renderer-gl-patch set

%preun
gsk-renderer-gl-patch revert

%changelog
* Fri Oct 18 2024 Malix <alixbrunetcontact@gmail.com> 1.0.1-1
- new package built with tito

* Fri Oct 18 2024 Malix <alixbrunetcontact@gmail.com>
- init
