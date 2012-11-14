%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name gcrma

Summary: Background Adjustment Using Sequence Information
Name: R-gcrma
Version: 2.28.0
Release: 1%{?dist}
License: LGPL
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel > 2.6.0, R-affy >= 1.23.2, R-affyio >= 1.13.3, R-Biobase, R-Biostrings >= 2.11.32
Requires: R-core > 2.6.0, R-affy >= 1.23.2, R-affyio >= 1.13.3, R-Biobase, R-Biostrings >= 2.11.32

%description
Background adjustment using sequence information

%prep
%setup -q -n %{short_name}

%build
#No build, R CMD INSTALL takes care of all of it

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d %{buildroot}%{Rlibdir}
%{__Rbinary} CMD INSTALL -l %{buildroot}%{Rlibdir} .
%{__rm} -f %{buildroot}%{Rlibdir}/R.css

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc DESCRIPTION
%dir %{Rlibdir}/%{short_name}
%{Rlibdir}/%{short_name}/*

%changelog
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-gcrma-2.28.1-1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-gcrma-2.24.1-1.el5
- Upgrade for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-gcrma-2.20.0-1.el5
- Upgrade to 2.20
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-gcrma-2.18.0-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-gcrma-2.18.0-1.el5
- Updated to 2.18
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-gcrma-2.16.0-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-gcrma-2.16.0-1.el5
- Initial build. Does not update search database

