Summary: NZGL release files
Name: nzgl-release
Version: 1.0
Release: 6%{?dist}
License: GPLv2
Source0: nzgl.repo
Source1: RPM-GPG-KEY-Biomatters

%description
NZGL repository and Biomatters signing key.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/pki/rpm-gpg

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config %attr(0644,root,root) /etc/yum.repos.d/*
%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/*

%changelog
* Thu Dec 06 2012 Carl Jones <carl@biomatters.com> - 1.0-6
- Split out RHN repositories

* Tue Sep 11 2012 Carl Jones <carl@biomatters.com> - 1.0-5
- Rename NZGL repositories

* Thu Sep 05 2012 Carl Jones <carl@biomatters.com> - 1.0-4
- Remove seperate -source repository

* Tue Aug 28 2012 Carl Jones <carl@biomatters.com> - 1.0-3
- Change RHEL repository names to avoid conflict with RHN

* Fri Aug 24 2012 Carl Jones <carl@biomatters.com> - 1.0-2
- Add nzgl-stable and nzgl-unstable repositories

* Fri Aug 24 2012 Carl Jones <carl@biomatters.com> - 1.0-1
- Initial release.
