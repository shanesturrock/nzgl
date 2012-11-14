%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name affy

Summary: Methods for Affymetrix Oligonucleotide Arrays
Name: R-affy
Version: 1.34.0
Release: 2%{?dist}
License: LGPL version 2 or newer
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel, R-affyio, R-Biobase, R-preprocessCore, R-BiocInstaller, R-preprocessCore-devel
Requires: R-core, R-affyio, R-Biobase, R-preprocessCore, R-BiocInstaller

%description
The package contains functions for exploratory oligonucleotide array analysis.
The dependance to tkWidgets only concerns few convenience functions.
'affy' is fully functional without it

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
* Mon Aug 20 2012 Carl Jones <carl@biomatters.com> R-affy-1.34.0-2
- Fix build deps

* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-affy-1.34.0-1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-affy-1.30.1-1.el5
- Upgrade for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-affy-1.26.1-1.el5
- Upgrade to 1.26
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-affy-1.24.1-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affy-1.24.2-1.el5
- Update to 1.24.2
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affy-1.22.0-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affy-1.22.0-1.el5
- Initial build. Does not update search database

