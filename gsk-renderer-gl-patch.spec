Name: gsk-renderer-gl-patch
Version: 1.0.0
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
install -D -m 544 ./lib/set.sh %{buildroot}%{_libexecdir}/%{name}/set.sh
install -D -m 544 ./lib/revert.sh %{buildroot}%{_libexecdir}/%{name}/revert.sh
install -D -m 544 ./lib/reboot.sh %{buildroot}%{_libexecdir}/%{name}/reboot.sh
install -D -m 544 ./lib/variables.sh %{buildroot}%{_libexecdir}/%{name}/variables.sh

%files
%license LICENSE
%doc docs/**
%dir %{_libexecdir}/%{name}
%{_bindir}/%{name}
%{_libexecdir}/%{name}/set.sh
%{_libexecdir}/%{name}/revert.sh
%{_libexecdir}/%{name}/reboot.sh
%{_libexecdir}/%{name}/variables.sh

%post
gsk-renderer-gl-patch set

%preun
gsk-renderer-gl-patch revert

%changelog
* Fri Oct 18 2024 Malix <alixbrunetcontact@gmail.com>
- init
