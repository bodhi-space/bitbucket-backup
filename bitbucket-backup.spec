Summary: Python script to backup Bitbucket repos
Name: bitbucket-backup
Version: %{_version}
Release: 3%{?dist}
Url: https://github.com/bodhi-space/bitbucket-backup
Source0: %{name}-%{version}.tar.bz2
License: DO WHAT YOU WANT TO PUBLIC LICENSE
Group: System/Backups
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: python27
BuildRequires: python27-setuptools

%description
A bitbucket backup script forked by Hotschedules in order to fix some bugs.
The URL for the upstream maintainer is https://github.com/samkuehn/bitbucket-backup.

%prep
%setup

%build

%install
/usr/bin/python2.7 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES --install-layout amzn

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)

%changelog
* Wed Jan 16 2019 Alex Yamauchi <alex.yamauchi@hotschdules.com> - 0.2.3-3
- updating from the upstream, which does not use versioning.
* Thu Jan 11 2018 Tom Williams <tom.williams@hotschedules.com> - 0.2.2-3
- update spec, move to main source tree.
* Wed May 17 2017 Alex Yamauchi <alex.yamauchi@hotschedules.com>
- modifying metadata for Jenkins job migration, bumping release.
* Wed Nov 30 2016 Alex Yamauchi <alex.yamauchi@hotschedules.com>
- updating the version to 0.2.2 to implement repo cloning retries.
* Mon Jan 18 2016 Alex Yamauchi <alex.yamauchi@hotschedules.com>
- updating the version to 0.2.1 to fix bad exit codes.
