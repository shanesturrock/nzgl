Summary: Configuration files and scripts for NZGL VMs.
Name: nzgl-sysscripts
Version: 1.0
Release: 1%{?dist}
License: GPLv2
Source0: nzgl.action
Source1: nzgl.cron
Source2: nzgl-java-configure
Source3: nzgl-services-configure
Source4: nzgl-yum-upgrade

%description
Configuration files and scripts for NZGL VMs.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/yum/post-actions/
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum/post-actions/

mkdir -p $RPM_BUILD_ROOT/etc/cron.d/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.d/

mkdir -p $RPM_BUILD_ROOT/%{_sbindir}/
install -m 755 ${SOURCE2} $RPM_BUILD_ROOT/%{_sbindir}/
install -m 755 ${SOURCE3} $RPM_BUILD_ROOT/%{_sbindir}/
install -m 755 ${SOURCE4} $RPM_BUILD_ROOT/%{_sbindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/nzgl-java-configure
/usr/sbin/nzgl-services-configure

%files
%defattr(-,root,root,-)
/etc/yum/post-actions/nzgl.action
/etc/cron.d/nzgl.cron
/usr/sbin/nzgl-java-configure
/usr/sbin/nzgl-services-configure
/usr/sbin/nzgl-yum-upgrade

%changelog
* Mon Jan 07 2013 Carl Jones <carl@biomatters.com> - 1.0-1
- Initial release.
