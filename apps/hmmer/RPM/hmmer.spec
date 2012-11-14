Name:           hmmer
Version:        3.0
Release:        5%{?dist}
Summary:        Profile HMM software for protein sequence analysis

Group:          Applications/Engineering
License:        GPLv3
URL:            http://hmmer.janelia.org
Source0:        http://selab.janelia.org/software/hmmer3/3.0/hmmer-3.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Profile hidden Markov models (profile HMMs) can be used to do sensitive
database searching using statistical descriptions of a sequence family's
consensus.  HMMER is a freely distributable implementation of profile HMM
software for protein sequence analysis.


%prep
%setup -q

# Need to 'fix' an old perl script
sed -i '/^require/d;/Getopts/d' easel/devkit/sqc


%build
%configure
make %{?_smp_mflags}


%check
make check


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
for f in documentation/man/*.man; do
  cp -p $f $RPM_BUILD_ROOT%{_mandir}/man1/`basename $f .man`.1
done


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYRIGHT LICENSE README RELEASE-NOTES Userguide.pdf tutorial/
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Fri Jul 20 2012 Christian Iseli <Christian.Iseli@unil.ch> - 3.0-5
- Fix build failure due to old (perl4) code in the test suite

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Christian Iseli <Christian.Iseli@licr.org> - 3.0-1
- New upstream version 3.0
- License is now GPLv3
- configure defaults to multi-threaded
- make install now uses DESTDIR
- copy manpages (rule missing in Makefile, apparently)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-9
- Rebuild for F-11
- Change URL and Source0 links to new location

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3.2-8
- Autorebuild for GCC 4.3

* Thu Aug 16 2007 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-7
 - Fix License tag to GPLv2+.

* Tue Sep 05 2006 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-6
 - Rebuild for FC 6.

* Wed Feb 15 2006 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-5
 - Minor spec cleanup.  Rebuild for FE 5.

* Fri Dec 23 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-4
 - Rebuild with gcc-4.1.

* Mon Aug 08 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-3
 - Removed altivec switch for ppc: apparently, it only works using Apple's
   GCC compiler.

* Sat Aug 06 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-2
 - Fix spec file according to review.

* Fri Aug 05 2005 Christian Iseli <Christian.Iseli@licr.org> - 2.3.2-1
 - Create spec file.
