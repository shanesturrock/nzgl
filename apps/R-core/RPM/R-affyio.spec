%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name affyio

Summary: Tools for parsing Affymetrix data files
Name: R-affyio
Version: 1.24.0
Release: 1%{?dist}
License: LGPL version 2 or newer
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel, R-zlibbioc
Requires: R-core, R-zlibbioc

%description
Routines for parsing Affymetrix data files based upon file format information.
Primary focus is on accessing the CEL and CDF file formats.

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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-affyio-1.24.0.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-affyio-1.20.0-1.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-affyio-1.16.0-1.el5
- Upgraded to 1.16
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-affyio-1.14.0-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affyio-1.14.0-1.el5
-Upgraded to 1.14
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affyio-1.12.0-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affyio-1.12.0-1.el5
- Initial build. Does not update search database

