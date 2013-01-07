Summary: iptables configuration files for NZGL VMs
Name: nzgl-iptables
Version: 1.0
Release: 2%{?dist}
License: GPLv2
Source0: iptables
Source1: ip6tables

%description
iptables configuration files for NZGL VMs.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/sysconfig/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add iptables
/sbin/chkconfig --add ip6tables
/sbin/chkconfig iptables on
/sbin/chkconfig ip6tables on
/sbin/service iptables restart &>/dev/null
/sbin/service ip6tables restart &>/dev/null

%files
%defattr(-,root,root,-)
%config /etc/sysconfig/iptables
%config /etc/sysconfig/ip6tables

%changelog
* Mon Jan 07 2013 Carl Jones <carl@biomatters.com> - 1.0-2
- Enable services in %post

* Mon Jan 07 2013 Carl Jones <carl@biomatters.com> - 1.0-1
- Initial release.
