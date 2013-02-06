Name:           glimmer
Version:        3.02b
Release:        1%{?dist}
Summary:        System for finding genes in microbial DNA

Group:          Applications/Engineering
License:        Artistic clarified
URL:            http://www.cbcb.umd.edu/software/glimmer
Source0:        http://www.cbcb.umd.edu/software/glimmer/glimmer302b.tar.gz
#Patch0:         glimmer-chris.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       elph

%description
Glimmer is a system for finding genes in microbial DNA, especially the genomes
of bacteria, archaea, and viruses. Glimmer (Gene Locator and Interpolated
Markov ModelER) uses interpolated Markov models (IMMs) to identify the coding
regions and distinguish them from noncoding DNA.


%prep
%setup -q -n glimmer3.02
#%patch0 -p1 -b .chris
rm -f sample-run/g3-*
sed -i "s+/fs/szgenefinding/Glimmer3/bin+%{_libexecdir}/glimmer3+" scripts/g3-*
sed -i "s+/fs/szgenefinding/Glimmer3/scripts+%{_datadir}/glimmer3+" scripts/g3-*
sed -i "s+/nfshomes/adelcher/bin/elph+%{_bindir}/elph+" scripts/g3-*
sed -i "s/@ if/if/" src/c_make.gen


%build
make -C src %{?_smp_mflags} CXXFLAGS="$RPM_OPT_FLAGS"


%check


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/glimmer3
mkdir -p $RPM_BUILD_ROOT%{_datadir}/glimmer3
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 scripts/g3-* $RPM_BUILD_ROOT/%{_bindir}
install -m 755 bin/[a-su-z]* $RPM_BUILD_ROOT%{_libexecdir}/glimmer3
install -m 755 scripts/*.awk $RPM_BUILD_ROOT%{_datadir}/glimmer3
ln -s ../libexec/glimmer3/glimmer3 $RPM_BUILD_ROOT/%{_bindir}/glimmer3


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE glim302notes.pdf sample-run
%{_bindir}/*
%{_datadir}/glimmer3/
%{_libexecdir}/glimmer3/


%changelog
* Thu Feb 07 2013 Carl Jones <carl@biomatters.com> - 3.02b-1
- New upstream release

* Wed Dec 12 2012 Carl Jones <carl@biomatters.com> - 3.02a-1
- New upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-9
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Christian Iseli <Christian.Iseli@licr.org> - 3.02-5
- Update patch for gcc-4.4

* Mon Feb 23 2009 Christian Iseli <Christian.Iseli@licr.org> - 3.02-4
- Rebuild for F-11

* Tue Jan 16 2008 Christian Iseli <Christian.Iseli@licr.org> - 3.02-3
 - Add patch to port to gcc-4.3.

* Wed Aug 22 2007 Christian Iseli <Christian.Iseli@licr.org> - 3.02-2
 - Fix License tag.

* Thu Feb 22 2007 Christian Iseli <Christian.Iseli@licr.org> - 3.02-1
 - Import in Fedora devel.

* Fri Feb  9 2007 Christian Iseli <Christian.Iseli@licr.org> - 3.02-0
 - Create spec file.
