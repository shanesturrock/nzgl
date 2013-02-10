Summary: Configuration files and scripts for NZGL VMs.
Name: nzgl-sysscripts
Version: 1.2
Release: 1%{?dist}
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