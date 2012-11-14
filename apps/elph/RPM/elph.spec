Name:           elph
Version:        1.0.1
Release:        9%{?dist}
Summary:        Tool to find motifs in a set of DNA or protein sequences

Group:          Applications/Engineering
License:        Artistic clarified
URL:            http://www.cbcb.umd.edu/software/ELPH/
Source0:        ftp://ftp.cbcb.umd.edu/pub/software/elph/ELPH-1.0.1.tar.gz
Patch0:         %{name}-chris.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
ELPH is a general-purpose Gibbs sampler for finding motifs in a set of
DNA or protein sequences. The program takes as input a set containing
anywhere from a few dozen to thousands of sequences, and searches
through them for the most common motif, assuming that each sequence
contains one copy of the motif.


%prep
%setup -q -n ELPH
%patch0 -p 1 -b .chris


%build
make -C sources %{?_smp_mflags} \
  CFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti -D_REENTRANT"


%check


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 sources/elph $RPM_BUILD_ROOT/%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYRIGHT LICENSE README Readme.ELPH VERSION
%{_bindir}/elph


%changelog
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Christian Iseli <Christian.Iseli@licr.org> - 1.0.1-4
- Rebuild for F-11

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.1-3
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Christian Iseli <Christian.Iseli@licr.org> 1.0.1-2
 - Fix License tag.

* Thu Feb 22 2007 Christian Iseli <Christian.Iseli@licr.org> 1.0.1-1
 - Import in Fedora devel.

* Fri Feb  9 2007 Christian Iseli <Christian.Iseli@licr.org> 1.0.1-0
 - Create spec file.
