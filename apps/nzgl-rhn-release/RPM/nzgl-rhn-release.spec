Summary: NZGL RHN release files
Name: nzgl-rhn-release
Version: 1.0
Release: 1%{?dist}
License: GPLv2
Source0: nzgl-rhn.repo

%description
NZGL RHN repository.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config %attr(0644,root,root) /etc/yum.repos.d/*

%changelog
* Thu Dec 06 2012 Carl Jones <carl@biomatters.com> - 1.0-1
- Initial release.
