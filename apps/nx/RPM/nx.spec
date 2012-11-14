Name:           nx
Version:        3.5.0
Release:        2%{?dist}
Summary:        Proxy system for X11

Group:          Applications/Internet
License:        GPL, MIT/X11 for X11 bits
URL:            http://www.nomachine.com
Source0:	nxproxy-%{version}-1.tar.gz
Source1:	nxcomp-%{version}-2.tar.gz
Source2:	nxcompext-%{version}-1.tar.gz
Source3:	nx-X11-%{version}-2.tar.gz
Source4:	nxagent-%{version}-9.tar.gz
Source5:	nxscripts-%{version}-1.tar.gz
Source6:	nxssh-%{version}-2.tar.gz
Source7:	nxauth-%{version}-1.tar.gz
Source8:        nxcompshad-%{version}-2.tar.gz
Source9:	nxagent
Source10:	docs.tar.bz2
Source11:	nxwin-%{version}-4.tar.gz
#Source12:	nxesd-%{version}-2.tar.gz
Source13:	nxfind-provides.sh
Source14:	nxfind-provides-64.sh

%ifarch ppc64 x86_64 sparc64 ia64 s390x 
%define _use_internal_dependency_generator 0
%define __find_provides %{SOURCE14}
%else
%define _use_internal_dependency_generator 0
%define __find_provides %{SOURCE13}
%endif

# centos_ver is a number (2,3,4,5). It can be provided in the build system or
# via the command line with the following define for rpmbuild
# --define "centos_ver 5"
# If centos_ver is not provided the following will find it and should work on
# all current redhat based EL rebuilds, will not work properly on FC though

%{!?centos_ver: %define centos_ver %(Z=`rpm -q --whatprovides /etc/redhat-release`;A=`rpm -q --qf '%{V}' $Z`; echo ${A:0:1})}
# end centos_ver test

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if "%{centos_ver}" == "4"
BuildRequires:  expat-devel audiofile-devel openssl-devel libjpeg-devel libpng-devel xorg-x11-devel xorg-x11-deprecated-libs-devel doxygen dbus-devel autoconf automake libtool
Requires:       xorg-x11 xorg-x11-tools
%endif

%if "%{centos_ver}" == "5"
BuildRequires:  expat-devel audiofile-devel openssl-devel libjpeg-devel libpng-devel libX11-devel libXp-devel imake libXdamage-devel libXrandr-devel libXtst-devel doxygen dbus-devel autoconf automake libtool
Requires: xorg-x11-server-Xorg xorg-x11-apps xorg-x11-utils
%endif

%if "%{centos_ver}" == "6"
BuildRequires:  expat-devel audiofile-devel openssl-devel libjpeg-devel libpng-devel libX11-devel libXp-devel imake libXdamage-devel libXrandr-devel libXtst-devel doxygen dbus-devel autoconf automake libtool
Requires: xorg-x11-server-Xorg xorg-x11-apps xorg-x11-utils xorg-x11-fonts-misc
%endif

Requires(post): policycoreutils
Requires(postun): policycoreutils
Provides: nx-devel = %{version}-%{release}

%description
NX provides a proxy system for the X Window System.

%prep
%setup -q -T -c %{name}-%{version} -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a11

cat >> nx-X11/config/cf/host.def << EOF
#ifdef  i386Architecture
#undef  DefaultGcc2i386Opt
#define DefaultGcc2i386Opt      $RPM_OPT_FLAGS -fno-strict-aliasing
#endif
#ifdef  MipsArchitecture
#undef  DefaultGcc2MipsOpt
#define DefaultGcc2MipsOpt      $RPM_OPT_FLAGS -fno-strict-aliasing
#endif
#ifdef s390xArchitecture
#undef OptimizedCDebugFlags
#define OptimizedCDebugFlags $RPM_OPT_FLAGS -fno-strict-aliasing
#endif
#ifdef  AMD64Architecture
#undef  DefaultGcc2AMD64Opt
#define DefaultGcc2AMD64Opt $RPM_OPT_FLAGS -fno-strict-aliasing
#endif
EOF

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
perl -pi -e"s|CXXFLAGS=.-O.*|CXXFLAGS=\"$CXXFLAGS\"|" */configure
# build Compression Library and Proxy
for i in nxcomp nxproxy nxcompshad; do
  pushd $i 
  ./configure
%if "%{centos_ver}" == "4"
%ifarch ppc64 x86_64 sparc64 ia64 s390x 
  perl -pi -e "s,/usr/X11R6/lib ,/usr/X11R6/lib64 ,g" Makefile
%endif
%endif
  make
  popd
done
# build X11 Support Libraries and Agents
pushd nx-X11
  make World
popd
# build Extended Compression Library
pushd nxcompext
  ./configure; make
popd
# build nxssh
pushd nxssh
  ./configure --without-zlib-version-check; make
popd
## build nxesd
# pushd nxesd
#   ./configure; make
# popd

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}/NX/lib
mkdir -p %{buildroot}/%{_mandir}/man1

# install X11 Support Libraries and Agents
cp -a nx-X11/lib/X11/libX11.so.* \
      nx-X11/lib/Xext/libXext.so.* \
      nx-X11/lib/Xrender/libXrender.so.* \
      %{buildroot}/%{_libdir}/NX/lib
install -m 755 nx-X11/programs/Xserver/nxagent \
  %{buildroot}/%{_libdir}/NX
install -m 755 %{SOURCE9} %{buildroot}/%{_bindir}
# install Compression Libraries and Proxy
cp -a nxcomp/libXcomp.so.* %{buildroot}/%{_libdir}/NX/lib
cp -a nxcompext/libXcompext.so.* %{buildroot}/%{_libdir}/NX/lib
cp -a nxcompshad/libXcompshad.so.* %{buildroot}/%{_libdir}/NX/lib
install -m 755 nxproxy/nxproxy %{buildroot}/%{_libdir}/NX
ln -snf nxagent %{buildroot}/%{_bindir}/nxproxy
# install nxssh
pushd nxssh
  cp -a nxssh %{buildroot}/%{_libdir}/NX
  ln -snf nxagent %{buildroot}/%{_bindir}/nxssh
  chmod 755 %{buildroot}/%{_bindir}/nxssh
popd
## install nxesd
# pushd nxesd
#   cp -a nxesd %{buildroot}/%{_libdir}/NX
#   ln -snf nxagent %{buildroot}/%{_bindir}/nxesd
#   chmod 755 %{buildroot}/%{_bindir}/nxesd
# popd

# install scripts
if [ ! -d %{buildroot}/%{_datadir}/doc/%{name}-%{version} ]; then
 mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
fi
cp -r nxscripts %{buildroot}/%{_datadir}/doc/%{name}-%{version}

# documentation and license
tar xjf %{SOURCE10} -C %{buildroot}/%{_datadir}/doc/%{name}-%{version}
install -m 644 nxcomp/LICENSE   %{buildroot}/%{_datadir}/doc/%{name}-%{version}
if [ ! -d %{buildroot}/%{_datadir}/doc/%{name}-%{version}/nxcomp ]; then
  mkdir %{buildroot}/%{_datadir}/doc/%{name}-%{version}/nxcomp
fi
install -m 644 nxcomp/README    %{buildroot}/%{_datadir}/doc/%{name}-%{version}/nxcomp

if [ ! -d %{buildroot}/%{_datadir}/doc/%{name}-%{version}/nxcl/html ]; then
  mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}/nxcl/html
fi

#create symlink for 64bit arches
%ifarch ppc64 x86_64 sparc64 ia64 s390x 
if [ ! -d %{buildroot}/usr/lib ]; then
 mkdir -p %{buildroot}/usr/lib
fi

pushd %{buildroot}/usr/lib
ln -snf ../lib64/NX .
popd
%endif
#end 64bit symlink

%post
%{_sbindir}/semanage fcontext -f -- -a -t textrel_shlib_t '%{_libdir}/NX/lib/libXcomp.so.%{version}' 2>/dev/null || :
%{_sbindir}/semanage fcontext -f -- -a -t textrel_shlib_t '%{_libdir}/NX/lib/libXcompext.so.%{version}' 2>/dev/null || :
%{_sbindir}/semanage fcontext -f -- -a -t textrel_shlib_t '%{_libdir}/NX/lib/libXcompshad.so.%{version}' 2>/dev/null || :

%{_bindir}/chcon -t textrel_shlib_t %{_libdir}/NX/lib/libXcomp.so.%{version} 2>/dev/null || :
%{_bindir}/chcon -t textrel_shlib_t %{_libdir}/NX/lib/libXcompext.so.%{version} 2>/dev/null || :
%{_bindir}/chcon -t textrel_shlib_t %{_libdir}/NX/lib/libXcompshad.so.%{version} 2>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
  %{_sbindir}/semanage fcontext -f -- -d -t textrel_shlib_t '%{_libdir}/NX/lib/libXcomp.so.%{version}' 2>/dev/null || :
  %{_sbindir}/semanage fcontext -f -- -d -t textrel_shlib_t '%{_libdir}/NX/lib/libXcompext.so.%{version}' 2>/dev/null || :
  %{_sbindir}/semanage fcontext -f -- -d -t textrel_shlib_t '%{_libdir}/NX/lib/libXcompshad.so.%{version}' 2>/dev/null || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}
%{_bindir}/*
%dir %{_libdir}/NX
%{_libdir}/NX/*

#64bit symlink
%ifarch ppc64 x86_64 sparc64 ia64 s390x 
/usr/lib/NX 
%endif

%changelog
* Fri Jun  1 2012 Johnny Hughes <johnny@centos.org> - 3.5.0-2
- upgraded to nxwin-3.5.0-4 and nxagent-3.5.0-9

* Wed Oct 19 2011 Akemi Yagi <toracat@centos.org> - 3.5.0-1
- upgraded to the nx 3.5.0 code
  nxagent-3.5.0-7.tar.gz, nxauth-3.5.0-1.tar.gz, nxcomp-3.5.0-2.tar.gz
  nxcompext-3.5.0-1.tar.gz, nxcompshad-3.5.0-2.tar.gz, nxproxy-3.5.0-1.tar.gz
  nxscripts-3.5.0-1.tar.gz, nxssh-3.5.0-2.tar.gz, nxwin-3.5.0-2.tar.gz
  nx-X11-3.5.0-2.tar.gz

* Sat May 14 2011 Johnny Hughes <johnny@centos.org> - 3.4.0-7
- updated the following source
  nxagent-3.4.0-16
  nxwin-3.4.0-7  

* Mon Sep 20 2010 Akemi Yagi <toracat@centos.org> - 3.4.0-6
- added CentOS-6
- added Requires xorg-x11-fonts-misc if CentOS-6
- updated the following source
  nx-X11-3.4.0-4.tar.gz
  nxagent-3.4.0-11

* Thu Jul 10 2010 Akemi Yagi <toracat@centos.org> - 3.4.0-5
- updated the following source
  nxagent-3.4.0-9.tar.gz

* Thu Jun  3 2010 Akemi Yagi <toracat@centos.org> - 3.4.0-4
- updated the following sources
  nxagent-3.4.0-5.tar.gz, nxauth-3.4.0-3.tar.gz, nxcomp-3.4.0-7.tar.gz
  nxcompshad-3.4.0-3.tar.gz, nxesd-3.4.0-2.tar.gz, nxssh-3.4.0-2.tar.gz
  nxwin-3.4.0-5.tar.gz, nx-X11-3.4.0-3.tar.gz

* Tue Jan 26 2010 Akemi Yagi <toracat@centos.org> - 3.4.0-3
- upgraded to the nx 3.4.0 code

* Fri May 15 2009 Akemi Yagi <toracat@centos.org> - 3.3.0-13
- upgraded to the nx 3.3.0 code

* Tue Jul 15 2008 Johnny Hughes <johnny@centos.org> - 3.2.0-8
- upgraded to the following packages nxagent-3.2.0-8.tar.gz, nx-X11-3.2.0-2.tar.gz

* Sat May 31 2008 Johnny Hughes <johnny@centos.org> - 3.2.0-7
- included upstream upgrades through (First Maintenance Release of the NX
  3.2.0 Server and Node Packages) which updated the folowing sources
  nxagent-3.2.0-5.tar.gz, nxcomp-3.2.0-7.tar.gz, nxcompshad-3.2.0-3.tar.gz

* Sun Apr 13 2008 Johnny Hughes <johnny@centos.org> - 3.2.0-6
- split out nxcl, qtnx, nxlaunch as freenx-client SRPM

* Sat Apr 12 2008 Johnny Hughes <johnny@centos.org> - 3.2.0-5
- upgraded to nx 3.2.0 code

* Sat Apr 12 2008 Johnny Hughes <johnny@centos.org> - 3.1.0-5
- upgraded to version 3.1.0 code
- included updates through (Second Maintenance Release of the NX 3.1.0 Node
  Packages)
- modified nxfind-provides.sh and nxfind-provides-64.sh to work for 64bit and 32bit libs
- added nxcl client library
- added nxlaunch and qtnx cleints for centos-5 only (nxlaunch currently not stable so not built)

* Tue Oct 16 2007 Johnny Hughes <johnny@centos.org> - 3.0.0-4
- rolled in upstream updates to nxagent-3.0.0-88, nxcomp-3.0.0-48,
  nxssh-3.0.0-21.tar.gz, and nx-X11-3.0.0-37.tar.gz.
  (Fourth Maintenance Release of the NX 3.0.0)

* Sun Jul  8 2007 Johnny Hughes <johnny@centos.org> - 3.0.0-3.el5.centos
- rolled in upstream updates to nxwin-3.0.0-10 and nxagent-3.0.0-77
  (First Maintenance Release of the NX 3.0.0 Server Manager Packages)
- added --without-zlib-version-check to the configure statement for nxssh

* Thu Jun 28 2007 Johnny Hughes <johnny@centos.org> - 3.0.0-2.el5.centos
- created a symlink for 64bit arches to work around freenx/nx combo issues

* Tue Jun 26 2007 Johnny Hughes <johnny@centos.org> - 3.0.0-1.el5.centos
- upgraded to nx-3.0.0 code

* Mon May 28 2007 Johnny Hughes <johnny@centos.org> - 2.1.0-5.el5.centos
- rolled in upstream updates to nxcomp-2.1.0-8, nxagent-2.1.0-20 
  (Fifth Maintenance Release of NX 2.1.0 Server Packages)
- Modified code to detect CentOS-4 or CentOS-5 and to provide the proper
  requires and buildrequires for both.

* Thu Feb  8 2007 Johnny Hughes <johnny@centos.org> - 2.1.0-5.el4.centos4
- rolled in upstream updates to nxproxy-2.1.0-3, nxcomp-2.1.0-7, 
  nxcompext-2.1.0-5, nx-X11-2.1.0-3, nxagent-2.1.0-18, nxviewer-2.1.0-12,
  nxdesktop-2.1.0-10, nxscripts-2.1.0-5, nxssh-2.1.0-2 ( Fourth Maintenance
  Release of NX 2.1.0 Server Packages)

* Mon Jan  1 2007 Johnny Hughes <johnny@centos.org> - 2.1.0-4.el4.centos4
- rolled in upstream updates to nxcomp-2.1.0-6, nxcompext-2.1.0-4,
  nxagent-2.1.0-17, and nxviewer-2.1.0-11. (Third Maintenance Release of
  NX 2.1.0 Server Packages)

* Thu Nov 23 2006 Johnny Hughes <johnny@centos.org> - 2.1.0-3.c4
- rolled in upstream updates to nxagent-2.1.0-13, nxviewer-2.1.0-8,
  nxdesktop-2.1.0-8 (Second Maintenance Release of NX 2.1.0 Server Packages)

* Wed Nov 22 2006 Johnny Hughes <johnny@centos.org> - 2.1.0-2.c4
- rolled in upstream updates to nxcomp-2.1.0-5.tar.gz and 
  nxscripts-2.1.0-4.tar.gz (First Maintenance Release of NX 2.1.0
  Server Packages).

* Tue Nov 21 2006 Johnny Hughes <johnny@centos.org> - 2.1.0-1.c4
- modified build requires and requires to work with CentOS-4
- changed /usr/%{_libdir}/libXp.so* /usr/X11R6/%{_lib}/libXp.so*
  in the specfile due to different X locations.
- added back changes to copy nxpasswd and nxviewer from X11R6 to
  /usr/bin

* Thu Sep 28 2006 Rick Stout <zipsonic[AT]gmail.com> - 2.1.0-1
- updated to 2.1.0 release
* Mon Aug 28 2006 Rick Stout <zipsonic[AT]gmail.com> - 2.0.0-4
- upped release for rebuild request
- removed link in post for /usr/X11R6/lib/X11 as it is now
  handled in freenx
- updated to maintenance release 2
- added nxssh component for future qtnx client
* Thu Jul 13 2006 Rick Stout <zipsonic[AT]gmail.com> - 2.0.0-3
- updated to 2.0.0 Maintenance release 1
* Tue Jul 11 2006 Rick Stout <zipsonic[AT]gmail.com> - 2.0.0-1
- upgraded to 2.0.0
- removed renderextension patch as it is unnecessary
- cleaned up spec file
* Tue Jun 13 2006 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-11
- fixed documentation directory problems BZ#194964
* Sat Jun 10 2006 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-10
- added Source11 to filter find-provides from showing libraries that should not
  be provided to the system. BZ#194652
* Wed Jun 07 2006 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-9
- added Dist tag
- fixed macro/variable inconsistencies
- added requires: post and postun for policycoreutils
* Tue Jun 06 2006 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-8
- adapting spec for fedora-extras
- excluding x86_64 arch at this time. nxagent causes segfaults
* Mon May 08 2006 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-7.FC5
- added a section to %post that links /usr/X11R6/lib/X11 to /usr/share/X11
  which is needed for nxagent to function properly
* Sun May 07 2006 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-6.FC5
- added support for selinux
* Tue May 02 2006 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-5.FC5
- reenabled nxviewer
* Mon May 01 2006 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-4.FC5.2
- rebuilt for FC5
- nxviewer still disabled
* Mon Jan 30 2006 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-4.FC5
- disabled the nxviewer build because it doesn't like modular X
- updated xorg dependencies
* Tue Dec 13 2005 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-4
- updated perl script line 76 to have quotes
* Tue Dec 13 2005 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-3
- updated all components to most recent release - Maintenance 3
- removed NX-1.5.diff
* Wed Aug 31 2005 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-2
- updated nxagent to ver .90
- added patches from SuSE to update some compiler warnings and buffer overflows
* Fri Aug 12 2005 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-1
- updated nxcomp to ver .65
* Tue Jul 26 2005 Rick Stout <zipsonic[AT]gmail.com> - 1.5.0-0
- Updated to 1.5.0 final
* Mon Jul 11 2005 Rick Stout <zipsonic[AT]gmail.com> - 1.4.9.4-0
- Updated to 1.5.0 snapshot 4
* Thu Jun 30 2005 Rick Stout <zipsonic[AT]gmail.com> - 1.4.9.3-0
- reworked package for update to 1.5.0 devel snapshot 3 (1.4.9.3)
- Commented out Xtranssock patch in NX.diff (doesn't seem to be necessary)
* Mon Apr 11 2005 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.0-5
- spec cleanups
- reworked Patch1 to make it apply without arch conditional
* Mon Feb 14 2005 Rick Stout <zipsonic[AT]gmail.com> - 1.4.0-4
- updated nx-X11, nxproxy, nxcomp, nxagent and nxdesktop
- released to address X11 security concerns.
* Tue Nov 09 2004 Rick Stout <zipsonic[AT]gmail.com> - 1.4.0-3
- updated to 1.4.0 final
* Mon Oct 11 2004 Rick Stout <zipsonic[AT]gmail.com> - 1.4.0-2
- Changed naming structure to be more friendly (lowercase)
* Fri Oct 07 2004 Rick Stout <zipsonic[AT]gmail.com> - 1.4.0-1
- Updated package dependencies
* Wed Sep 29 2004 Rick Stout <zipsonic[AT]gmail.com> - 1.4.0-0
- Initial Fedora RPM release.
Updated SuSE package to work with Fedora
