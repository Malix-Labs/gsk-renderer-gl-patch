Name: gsk-renderer-gl-patch
Summary: Patch for GSK rendering issues (sets GSK_RENDERER=gl)
Version: 1.0.5
Release: 1%{?dist}
URL: https://github.com/Malix-Labs/%{name}
Source0: %{url}/releases/tag/%{name}-%{version}.tar.gz
License: unlicense
Group: System/Configuration/Files
Requires: sed

%description
Patch for GSK rendering issues (sets GSK_RENDERER=gl)

%prep
%autosetup

%build
# Nothing to build

%install
install -D -m 544 ./src/main.sh %{buildroot}%{_bindir}/%{name}
install -D -m 544 ./lib/set.sh %{buildroot}%{_libexecdir}/%{name}/set.sh
install -D -m 544 ./lib/revert.sh %{buildroot}%{_libexecdir}/%{name}/revert.sh
install -D -m 544 ./lib/reboot.sh %{buildroot}%{_libexecdir}/%{name}/reboot.sh
install -D -m 544 ./lib/variables.sh %{buildroot}%{_libexecdir}/%{name}/variables.sh

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}/set.sh
%{_libexecdir}/%{name}/revert.sh
%{_libexecdir}/%{name}/reboot.sh
%{_libexecdir}/%{name}/variables.sh
%exclude %{_libexecdir}/%{name}/debugsourcefiles.list
%doc docs/CONTRIBUTING.md
%doc docs/README.md
%license LICENSE

%post
gsk-renderer-gl-patch set

%preun
gsk-renderer-gl-patch revert

%changelog
* Fri Oct 18 2024 Malix <alixbrunetcontact@gmail.com> 1.0.5-1
- add ./ (alixbrunetcontact@gmail.com)
- test with autosetup (alixbrunetcontact@gmail.com)
- zefzef (alixbrunetcontact@gmail.com)
- test with q (alixbrunetcontact@gmail.com)
- a (alixbrunetcontact@gmail.com)
- add files (alixbrunetcontact@gmail.com)
- a (alixbrunetcontact@gmail.com)
- asas (alixbrunetcontact@gmail.com)
- asasa (alixbrunetcontact@gmail.com)
- now what (alixbrunetcontact@gmail.com)
- a (alixbrunetcontact@gmail.com)
- a (alixbrunetcontact@gmail.com)
- k (alixbrunetcontact@gmail.com)
- a (alixbrunetcontact@gmail.com)
- Source0 (alixbrunetcontact@gmail.com)
- test (alixbrunetcontact@gmail.com)
- use var (alixbrunetcontact@gmail.com)
- enhance: %%prep (alixbrunetcontact@gmail.com)
- feat: rpm licence (alixbrunetcontact@gmail.com)
- enhance: %%files (alixbrunetcontact@gmail.com)
- deprecate: sources (alixbrunetcontact@gmail.com)
- fix: devcontainer command (alixbrunetcontact@gmail.com)
- fix: devcontainer postStartCommand (alixbrunetcontact@gmail.com)
- test: reorder source (alixbrunetcontact@gmail.com)
- fix: source order (alixbrunetcontact@gmail.com)
- enhance: fhs (alixbrunetcontact@gmail.com)
- feat: README (alixbrunetcontact@gmail.com)
- feat: build test (alixbrunetcontact@gmail.com)
- test agauin (alixbrunetcontact@gmail.com)
- libmacro (alixbrunetcontact@gmail.com)
- source macro (alixbrunetcontact@gmail.com)
- test (alixbrunetcontact@gmail.com)
- enhance: spec (alixbrunetcontact@gmail.com)
- test (alixbrunetcontact@gmail.com)
- feat: copr-cli package (alixbrunetcontact@gmail.com)

* Fri Oct 11 2024 Malix <alixbrunetcontact@gmail.com> 1.0.4-1
- yes test tito

* Fri Oct 11 2024 Malix-off <alixbrunetcontact@gmail.com> 1.0.3-1
- enhance: change perm (alixbrunetcontact@gmail.com)

* Fri Oct 11 2024 Malix <alixbrunetcontact@gmail.com>
- new package built with tito
