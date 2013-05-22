Summary: Configuration files and scripts for NZGL VMs.
Name: nzgl-sysscripts
Version: 1.6
Release: 2%{?dist}
License: GPLv2
Source0: nzgl.action
Source1: nzgl.cron
Source2: nzgl-configure-services
Source3: nzgl-configure-java
Source4: nzgl-yum-upgrade
Source5: nzgl-configure-gnome
Source6: panel-default-setup.entries.nzgl
Source7: galaxy.desktop
Source8: bioinformatics.menu
Source9: bioinformatics.directory

%description
Configuration files and scripts for NZGL VMs.

%prep

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/etc/yum/post-actions/
install -m 644 %{SOURCE0} %{buildroot}/etc/yum/post-actions/

mkdir -p %{buildroot}/etc/cron.d/
install -m 644 %{SOURCE1} %{buildroot}/etc/cron.d/

mkdir -p %{buildroot}%{_sbindir}/
install -m 755 %{SOURCE2} %{buildroot}/%{_sbindir}/
install -m 755 %{SOURCE3} %{buildroot}/%{_sbindir}/
install -m 755 %{SOURCE4} %{buildroot}/%{_sbindir}/
install -m 755 %{SOURCE5} %{buildroot}/%{_sbindir}/

mkdir -p %{buildroot}%{_sysconfdir}/gconf/schemas/
install -m 644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/gconf/schemas/

mkdir -p %{buildroot}%{_datadir}/applications/
install -m 644 %{SOURCE7} %{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}/%{_sysconfdir}/xdg/menus/applications-merged/
install -m 644 %{SOURCE8} %{buildroot}/%{_sysconfdir}/xdg/menus/applications-merged/

mkdir -p %{buildroot}%{_datadir}/desktop-directories/
install -m 644 %{SOURCE9} %{buildroot}%{_datadir}/desktop-directories/

%clean
rm -rf %{buildroot}

%post
/usr/sbin/nzgl-configure-java
/usr/sbin/nzgl-configure-services
/usr/sbin/nzgl-configure-gnome

%files
%defattr(-,root,root,-)
/etc/yum/post-actions/nzgl.action
/etc/cron.d/nzgl.cron
/usr/sbin/nzgl-configure-java
/usr/sbin/nzgl-configure-services
/usr/sbin/nzgl-configure-gnome
/usr/sbin/nzgl-yum-upgrade
/etc/gconf/schemas/panel-default-setup.entries.nzgl
/usr/share/applications/galaxy.desktop
/usr/share/desktop-directories/bioinformatics.directory
/etc/xdg/menus/applications-merged/bioinformatics.menu

%changelog
* Thu May 23 2013 Simon Buxton <simon@biomatters.com> - 1.6-2
- Update Galaxy menu shortcut to standard https port

* Wed May 22 2013 Simon Buxton <simon@biomatters.com> - 1.6-1
- Update Galaxy menu shortcut domain to galaxy.nzgenomics.co.nz

* Wed Apr 24 2013 Shane Sturrock <shane@biomatters.com> - 1.6-0
- Testing shows Tablet requires Java 7 so can't turn it off any more

* Tue Apr 23 2013 Shane Sturrock <shane@biomatters.com> - 1.5-0
- Fixed issues with messagebus being turned off and incorrect update
- script naming.

* Mon Mar 18 2013 Shane Sturrock <shane@biomatters.com> - 1.4-0
- Change galaxy.desktop application to link to new Galaxy server in NZGL

* Tue Feb 26 2013 Carl Jones <carl@biomatters.com> - 1.3-0
- Remove snmpd from default service list
- Add munin-node to default service list

* Tue Feb 05 2013 Carl Jones <carl@biomatters.com> - 1.2-1
- Fix nzgl.action paths

* Tue Feb 05 2013 Carl Jones <carl@biomatters.com> - 1.2-0
- Rename *-configure to configure-*
- Add desktop defaults to -configure-gnome

* Tue Feb 05 2013 Carl Jones <carl@biomatters.com> - 1.1-1
- Add panel defaults file and script.
- Add Galaxy menu entry.
- Add Bioinformatics menu.

* Mon Jan 07 2013 Carl Jones <carl@biomatters.com> - 1.0-1
- Initial release.
