# centos_ver is a number (2,3,4,5). It can be provided in the build system or
# via the command line with the following define for rpmbuild
# --define "centos_ver 5"
# If centos_ver is not provided the following will find it and should work on
# all current redhat based EL rebuilds, will not work properly on FC though

%{!?centos_ver: %define centos_ver %(Z=`rpm -q --whatprovides /etc/redhat-release`;A=`rpm -q --qf '%{V}' $Z`; echo ${A:0:1})}
# end centos_ver test

Name:           freenx
Version:        0.7.3
Release:        9%{?dist}
Summary:        Freenx application/thin-client server
Group:          Applications/Internet 
License:        GPL
URL:            http://freenx.berlios.de
# latest source from http://svn.berlios.de/svnroot/repos/freenx/freenx-server/
# source contains the svn revision number for tracking.
Source0:        %{name}-server-%{version}.tar.gz
Source1:        nxcheckload.centos
Source2:        nxserver.logrotate
Patch631:       freenx-0.7.3-r631.patch
Patch0:		freenx-0.7.1-nxnode-fullscreen.patch
Patch1:         freenx-0.7.2-centos-diffs.patch
Patch2:		freenx-0.7.2-initd-script.patch
Patch3:		freenx-0.7.2-mswindows-sessreg.patch
Patch4:		freenx-0.7.3-centos-nxserver.patch
Patch5:		freenx-0.7.3-centos-nxnode.patch
Patch6:		freenx-0.7.3-centos-nxsetup.patch
Patch7:         freenx-0.7.3-centos-nxdialog.patch
Patch8:		freenx-0.7.3-centos-space-in-passwd-bug4274.patch
Patch9:		freenx-0.7.3-centos-leading-dash-in-passwd-bug4275.patch
Patch10:	freenx-0.7.3-centos-md5sum-bug4360.patch
Patch11:	freenx-0.7.2-centos-el6-diffs.patch
Patch12:	freenx-0.7.3-centos-add-xdmcp.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: openssh-server nc expect dbus-x11 perl xorg-x11-server-utils
Requires: nx >= 2.0.0
Requires: xorg-x11-fonts-misc

%if "%centos_ver" == "4"
Requires:	xorg-x11 xorg-x11-tools
Buildrequires:	xorg-x11-devel
%endif

%if "%centos_ver" == "5"
Requires: xorg-x11-server-Xorg xorg-x11-apps
BuildRequires: imake
%endif

%if "%centos_ver" == "6"
Requires: xorg-x11-server-Xorg xorg-x11-apps xorg-x11-fonts-misc
BuildRequires: imake
%endif

%description
Freenx is an application/thin-client server based on nx technology. 
NoMachine nx is the next-generation X compression and roundtrip suppression
scheme. It can operate remote X11 sessions over 56k modem dialup links
or anything better. This package contains a free (GPL) implementation
of the nxserver component.

%prep
%setup -q -n %{name}-server-%{version} 

%patch631 -p1
%patch0 -p1
%if "%centos_ver" == "5"
%patch1 -p1
%endif
%if "%centos_ver" == "6"
%patch11 -p1
%endif
%patch2 -p1

%if "%centos_ver" == "4"
%patch3 -p1
%endif

%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch12 -p1

# activate logging in nxloadconfig as default
%{__perl} -pi.orig -e '
		s|NX_LOG_LEVEL=0|NX_LOG_LEVEL=4|;
		s|NX_LOGFILE=\/var\/log\/nxserver.log|NX_LOGFILE=\/var\/log\/nx\/nxserver.log|;
	' nxloadconfig

%build
pushd nxserver-helper
make
popd

pushd nxviewer-passwd
xmkmf
make World
popd

pushd nxredir
make
popd

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}/%{_sysconfdir}/nxserver
mkdir -p %{buildroot}/%{_var}/lib/nxserver/db/closed
mkdir -p %{buildroot}/%{_var}/lib/nxserver/db/running
mkdir -p %{buildroot}/%{_var}/lib/nxserver/db/failed
mkdir -p %{buildroot}/%{_var}/log/nx
mkdir -p %{buildroot}/%{_initrddir}
chmod 700 %{buildroot}/%{_var}/lib/nxserver
chmod 700 %{buildroot}/%{_var}/lib/nxserver/*
chmod 700 %{buildroot}/%{_var}/lib/nxserver/db/*

if [ -e nxserver-helper/nxserver-helper ]
then
	install -m 755 nxserver-helper/nxserver-helper %{buildroot}/%{_bindir}
fi

if [ -e nxviewer-passwd/nxpasswd/nxpasswd ]
then
        install -m 755 nxviewer-passwd/nxpasswd/nxpasswd %{buildroot}/%{_bindir}
fi

if [ -e nxredir/nxredir ]
then
        install -m 755 nxredir/nxredir %{buildroot}/%{_bindir}
fi

if [ -e nxredir/libnxredir.so.0 ]
then
	install -D -p -m 644 nxredir/libnxredir.so.0 %{buildroot}/%{_libdir}/libnxredir.so.0
fi

install -m 755 nxcups-gethost nxdesktop_helper nxdialog nxkeygen nxloadconfig\
 nxnode nxnode-login nxprint nxserver nxsetup nxviewer_helper\
 %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}/%{_bindir}/nxcheckload

install -m 644 node.conf.sample %{buildroot}/%{_sysconfdir}/nxserver
install -p -m 644 %{buildroot}/%{_sysconfdir}/nxserver/node.conf.sample %{buildroot}/%{_sysconfdir}/nxserver/node.conf
install -p -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/logrotate.d/nxserver

install -m 755 init.d/freenx-server %{buildroot}/%{_initrddir}


# activate logging in node.conf as default
%{__perl} -pi -e '
		s|#NX_LOG_LEVEL=0|NX_LOG_LEVEL=4|;
		s|#NX_LOGFILE=\/var\/log\/nxserver.log|NX_LOGFILE=\/var\/log\/nx\/nxserver.log|;
	' %{buildroot}/%{_sysconfdir}/nxserver/node.conf

%clean
rm -rf %{buildroot}

%post
export $(grep ^NX_DIR %{_bindir}/nxloadconfig)
export $(grep ^NX_HOME_DIR %{_bindir}/nxloadconfig)
export $(grep ^NX_SESS_DIR %{_bindir}/nxloadconfig)
export $(grep ^NX_ETC_DIR %{_bindir}/nxloadconfig)
export $(grep ^NX_LOGFILE %{_bindir}/nxloadconfig)
export $(grep ^SSH_AUTHORIZED_KEYS %{_bindir}/nxloadconfig)
/sbin/service sshd condrestart
touch $NX_ETC_DIR/passwords $NX_ETC_DIR/passwords.orig $NX_LOGFILE
chmod 600 $NX_ETC_DIR/pass* $NX_LOGFILE
if [ ! -e $NX_ETC_DIR/users.id_dsa ]
then
	%{_bindir}/ssh-keygen -f $NX_ETC_DIR/users.id_dsa -t dsa -N "" > /dev/null 2>&1
fi
if [ -e $NX_HOME_DIR/.ssh/client.id_dsa.key ] && [ -e $NX_HOME_DIR/.ssh/server.id_dsa.pub.key ]
then
        mv -f $NX_HOME_DIR/.ssh/client.id_dsa.key $NX_ETC_DIR/client.id_dsa.key
        mv -f $NX_HOME_DIR/.ssh/server.id_dsa.pub.key $NX_ETC_DIR/server.id_dsa.pub.key
fi
if ! { getent passwd | egrep -q "^nx:"; }
then
        %{_sbindir}/useradd -r -d $NX_HOME_DIR -s %{_bindir}/nxserver nx
        mkdir -p $NX_HOME_DIR/.ssh
fi
if [ ! -e $NX_ETC_DIR/client.id_dsa.key ] || [ ! -e $NX_ETC_DIR/server.id_dsa.pub.key ]
then
	rm -f $NX_ETC_DIR/client.id_dsa.key
	rm -f $NX_ETC_DIR/server.id_dsa.pub.key
	%{_bindir}/ssh-keygen -q -t dsa -N '' -f $NX_ETC_DIR/local.id_dsa
	mv $NX_ETC_DIR/local.id_dsa $NX_ETC_DIR/client.id_dsa.key
	mv $NX_ETC_DIR/local.id_dsa.pub $NX_ETC_DIR/server.id_dsa.pub.key
fi
cp -f $NX_ETC_DIR/client.id_dsa.key $NX_HOME_DIR/.ssh/client.id_dsa.key
cp -f $NX_ETC_DIR/server.id_dsa.pub.key $NX_HOME_DIR/.ssh/server.id_dsa.pub.key
chmod 600 $NX_ETC_DIR/client.id_dsa.key $NX_ETC_DIR/server.id_dsa.pub.key\
 $NX_HOME_DIR/.ssh/client.id_dsa.key $NX_HOME_DIR/.ssh/server.id_dsa.pub.key
echo -n "no-port-forwarding,no-X11-forwarding,no-agent-forwarding,command=\"%{_bindir}/nxserver\" "\
 > $NX_HOME_DIR/.ssh/authorized_keys2
cat $NX_HOME_DIR/.ssh/server.id_dsa.pub.key >> $NX_HOME_DIR/.ssh/authorized_keys2
chmod 640 $NX_HOME_DIR/.ssh/authorized_keys2
echo -n "127.0.0.1 " > $NX_HOME_DIR/.ssh/known_hosts
cat %{_sysconfdir}/ssh/ssh_host_rsa_key.pub >> $NX_HOME_DIR/.ssh/known_hosts
chown -R nx:root %{_var}/lib/nxserver
chown -R nx:root $NX_SESS_DIR
if [ -e %{_var}/lib/nxserver/running ]
then
	mv %{_var}/lib/nxserver/running/* $NX_SESS_DIR/running
	mv %{_var}/lib/nxserver/closed/* $NX_SESS_DIR/closed
	mv %{_var}/lib/nxserver/failed/* $NX_SESS_DIR/failed
	rm -rf %{_var}/lib/nxserver/running
	rm -rf %{_var}/lib/nxserver/closed
	rm -rf %{_var}/lib/nxserver/failed
	chown -R nx:root $NX_SESS_DIR
fi
chown -R nx:root $NX_ETC_DIR
chown -R nx:root $NX_HOME_DIR
chmod -R 700 $NX_HOME_DIR
chmod 700 `dirname $NX_LOGFILE`
chown nx:root `dirname $NX_LOGFILE`
chown nx:root $NX_LOGFILE

# selinux fix -- run restorecon on nx's home
if [ -e /sbin/restorecon ]; then
   /sbin/restorecon -R /var/lib/nxserver
fi
# end of selinux fix

/sbin/chkconfig --add freenx-server
/sbin/service freenx-server start

%preun
if [ $1 = 0 ]
then
	export $(grep ^NX_DIR %{_bindir}/nxloadconfig)
	export $(grep ^NX_HOME_DIR %{_bindir}/nxloadconfig)
	rm %{_var}/lib/nxserver/db/closed/* > /dev/null 2>&1
	rm %{_var}/lib/nxserver/db/running/* > /dev/null 2>&1
	rm %{_var}/lib/nxserver/db/failed/* > /dev/null 2>&1
	mv -f $NX_HOME_DIR/.ssh/client.id_dsa.key /etc/nxserver/  > /dev/null 2>&1
	mv -f $NX_HOME_DIR/.ssh/server.id_dsa.pub.key /etc/nxserver/  > /dev/null 2>&1
	/sbin/service freenx-server stop
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog CONTRIB nxcheckload.sample nxacl.sample
%{_bindir}/*
%{_libdir}/libnxredir.so.0
%dir %{_sysconfdir}/nxserver
%config(noreplace) %{_sysconfdir}/nxserver/node.conf
%{_sysconfdir}/nxserver/node.conf.sample
%{_sysconfdir}/logrotate.d/nxserver
%{_initrddir}/freenx-server
%dir %{_var}/lib/nxserver
%dir %{_var}/lib/nxserver/db
%dir %{_var}/lib/nxserver/db/closed
%dir %{_var}/lib/nxserver/db/running
%dir %{_var}/lib/nxserver/db/failed
%dir %{_var}/log/nx

%changelog
* Fri Jun 1 2012 Johnny Hughes <johnny@centos.org> 0.7.3-9
- added xdmcp to nxnode

* Mon Aug 22 2011 Akemi Yagi <toracat@centos.org> 0.7.3-8
- added selinux fix (run restorecon on nx's home directory) 
  (centos bug 5052)

* Sat May 14 2011 Johnny Hughes <johnny@centos.org> 0.7.3-7
- added install of libnxredir.so.0 to libdir (centos bug 4868) 

* Sun Oct  3 2010 Akemi Yagi <toracat@centos.org> 0.7.3-6
- added centos-6 support
- added centos-el6-diffs.patch for centos-6
- added Requires: xorg-x11-fonts-misc for centos-6

* Sun Jul 11 2010 Akemi Yagi <toracat@centos.org> 0.7.3-5
- re-added a patch missed in 0.7.3-4 (bug4398)
- applied enhancements contributed by Uwe Beck <ubeck(at)ubeck.com>
  (bug4408)
   default /etc/nxserver/node.conf file
   activate logging
   logrotate
   rpm -Uhv can handle logfile
- applied a patch that fixes problems with loadbalancing contributed by
  Uwe Beck <ubeck(at)ubeck.com> (bug4404)
  freenx-0.7.3-r631.patch -- adopted from the freenx-round-robin-loadbalance.patch
  included in freenx svn version 631 
  ( http://bugs.gentoo.org/show_bug.cgi?id=235204 )
  add /usr/bin/nxcheckload   

* Thu Jun  3 2010 Akemi Yagi <toracat@centos.org> 0.7.3-4
- applied freenx-0.7.3-centos-space-in-passwd-bug4274.patch
- applied freenx-0.7.3-centos-leading-dash-in-passwd-bug4275.patch
- applied freenx-0.7.3-centos-md5sum-bug4360.patch

* Wed Jan 27 2010 Akemi Yagi <toracat@centos.org> 0.7.3-3
- applied freenx-0.7.3-centos-nxnode.patch (bug3836)
- applied freenx-0.7.3-centos-nxsetup.patch (bug2931,3817)
- applied freenx-0.7.3-centos-nxdialog.patch (bug4182)

* Sun Aug 31 2009 Akemi Yagi <toracat@centos.org> 0.7.3-2
- applied patches to nxserver
  http://bazaar.launchpad.net/~freenx-team/freenx-server/ubuntu/revision/86#nxserver
  http://mail.kde.org/pipermail/freenx-knx/2009-May/008126.html

* Tue Oct 28 2008 Johnny Hughes <johnny@centos.org> 0.7.3-1
- upgraded to version 0.7.3

* Fri Jul 18 2008 Johnny Hughes <johnny@centos.org> 0.7.2-3
- fixed COMMAND_SESSREG="/usr/X11R6/bin/sessreg" in nxloadconfig for centos4

* Sat Apr 12 2008 Johnny Hughes <johnny@centos.org> 0.7.2-1
- upgraded to upstream code freenx-server-0.7.2

* Tue Nov 20 2007 Johnny Hughes <johnny@centos.org> 0.7.1.svn416-3
- modified the init.d script to also chown .X11-unix if not owned by root
  (possible on an upgrade from nx-2 to nx-3).

* Mon Nov  5 2007 Johnny Hughes <johnny@centos.org> 0.7.1.svn416-2
- upgraded to freenx svn version 416
- modified the freenx-server script to be CentOS chkconfig compatible.

* Tue Oct 16 2007 Johnny Hughes <johnny@centos.org> 0.7.1-1
- rebased on freenx-0.7.1

* Mon May 28 2007 Johnny Hughes <> 0.6.0-13
- rebased on freenx-0.6.0

* Mon Jan  1 2007 Johnny Hughes <johnny@centos.org> 0.5.0-12
- upgraded to the latest svn version of freenx (currently rev. 282)
- renamed fc5patch.diff to centos4.diff and modified it for CentOS-4
  compatibility
- removed nxclient.diff as that functionality was rolled in upstream.
- changed spec to build and install nxserver-helper to add nxnode slave mode

* Wed Nov 22 2006 Johnny Hughes <johnny@centos.org> 0.5.0-11
- upgraded to nx-2.0.0 server components for CentOS.
- used version 0.5.0-11 to make it an upgrade to CentOS-4 current release
- rolled in patch nxnode-2.1.x-fullscreen.patch from the previous CentOS
  freenx (different offset).

* Thu Sep 28 2006 Rick Stout <zipsonic[AT]gmail.com> 0.5.0-5
- updated nxclient script to svn which fixes problems with suspend when
  !M client is not installed on the server.
* Mon Aug 28 2006 Rick Stout <zipsonic[AT]gmail.com> 0.5.0-4
- upping version for rebuild
- added fix for nxsetup not displaying the proper message
- updated the node.conf.sample to show the fedora defaults
- added dbus-x11 to dependencies to fix BZ# 200756
- added AGENXT_EXTRA_OPTIONS_X to nxloadconfig for modular x.org compat
* Sun Jul 07 2006 Rick Stout <zipsonic[AT]gmail.com> 0.5.0-2
- updating dependencies to have the nx 2.0.0 backend
- tweaked nxloadconfig for gnome and kde startup and nx 2.0.0 backend
- added --override switch to nxsetup to warn users that the setup was already completed
- retweaked BZ# 197812 fix
* Sun Jul 07 2006 Rick Stout <zipsonic[AT]gmail.com> 0.5.0-1
- updated to 0.5.0 final
- fixed bug with nx user home directory permissions. BZ# 197812
* Sun Jun 11 2006 Rick Stout <zipsonic[AT]gmail.com> 0.5.0-0.5.test7
- Removed buildarch: noarch, and added excludearch: x86_64 to fix broken dependencies in x86_64
* Wed Jun 07 2006 Rick Stout <zipsonic[AT]gmail.com> 0.5.0-0.3.test7
- added dist tag
* Wed Jun 07 2006 Rick Stout <zipsonic[AT]gmail.com> 0.5.0-0.2.test7
- fixed variable/macro inconsistencies
* Tue Jun 06 2006 Rick Stout <zipsonic[AT]gmail.com> 0.5.0-0.1.test7
- reworked spec for fedora-extras
* Wed May 05 2006 Rick Stout <zipsonic[AT]gmail.com> 0.4.9-0.5.0-test7.0.FC5.1
- fixed an error that would not allow useradd to create a home directory in
  /var/lib if selinux was set to enforcing
* Wed Apr 13 2006 Rick Stout <zipsonic[AT]gmail.com> 0.4.9-0.5.0-test7.0.FC5.0
- updated to freenx 0.5.0 test7
- updated nxloadconfig for fc5 specfic items
- applied fix to error in nxloadconfig on test7
* Wed Feb 02 2006 Rick Stout <zipsonic[AT]gmail.com> 0.4.4-2.FC5
- updated nxloadconfig for fc5
- updated dependencies for fc5
* Thu Jan 26 2006 Rick Stout <zipsonic[AT]gmail.com> 0.4.4-2
- updated authorized keys file code to disable port, X11 and agent forwarding for for the nx account
- miscellaneous macro housekeeping 
* Sat Aug 06 2005 Rick Stout <zipsonic[AT]gmail.com> 0.4.4-1
- updated to 0.4.4
* Wed Aug 03 2005 Rick Stout <zipsonic[AT]gmail.com> 0.4.3.9-2
- updated to 0.4.4-rc1
- added patch to nxloadconfig to require 1.5.0 nx backend
* Mon Aug 01 2005 Rick Stout <zipsonic[AT]gmail.com> 0.4.3-1
- updated to 0.4.3
* Tue Jul 26 2005 Rick Stout <zipsonic[AT]gmail.com> 0.4.2-1
- updated to 0.4.2
* Tue Jun 28 2005 Rick Stout <zipsonic[AT]gmail.com> 0.4.1-1
- updated to 0.4.1
- updated freenx url
* Fri May 06 2005 Rick Stout <zipsonic[AT]gmail.com> 0.4.0-1
- Updated to 0.4.0
- updated netcat.diff for obvious reasons
* Mon Apr 11 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.1-4
- spec cleanup
* Tue Mar 22 2005 Rick Stout <zipsonic[AT]gmail.com> - 0:0.3.1
- Updated to 0.3.1 release
* Tue Mar 08 2005 Rick Stout <zipsonic[AT]gmail.com> - 0:0.3.0
- Updated to 0.3.0 release
- Removed home directory patch as it is now default
* Mon Feb 14 2005 Rick Stout <zipsonic[AT]gmail.com> - 0:0.2.8
- Updated to 0.2.8 release
- Fixes some security issues
- Added geom-fix patch for windows client resuming issues
* Thu Dec 02 2004 Rick Stout <zipsonic[AT]gmail.com> - 1:0.2.7
- Fixed package removal not removing the var session directories
* Tue Nov 23 2004 Rick Stout <zipsonic[AT]gmail.com> - 0:0.2.7
- Updated to 0.2.7 release
- fixes some stability issues with 0.2.6
* Fri Nov 12 2004 Rick Stout <zipsonic[AT]gmail.com> - 1:0.2.6
- Fixed a problem with key backup upon removal
* Fri Nov 12 2004 Rick Stout <zipsonic[AT]gmail.com> - 0:0.2.6
- Updated to 0.2.6 release
- Changed setup to have nx user account added as a system account.
- Changed nx home directory to /var/lib/nxserver/nxhome
* Thu Oct 14 2004 Rick Stout <zipsonic[AT]gmail.com> - 0:0.2.5
- updated package to 0.2.5 release
- still applying patch for netcat and useradd
* Fri Oct 08 2004 Rick Stout <zipsonic[AT]gmail.com> - 3:0.2.4
- Added nxsetup functionality to the rpm
- patched nxsetup (fnxncuseradd) script for occasional path error.
- Added patch (fnxncuseradd) to resolve newer client connections (netcat -> nc)
- Changed name to be more friendly (lowercase)
- Added known dependencies
* Thu Sep 30 2004 Rick Stout <zipsonic[AT]gmail.com> - 2:0.2.4
- Patch (fnxpermatch) to fix permissions with key generation
* Wed Sep 29 2004 Rick Stout <zipsonic[AT]gmail.com> - 1:0.2.4
- Initial Fedora RPM release.
- Updated SuSE package for Fedora
