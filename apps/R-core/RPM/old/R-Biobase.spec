%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name Biobase

Summary: Base functions for Bioconductor
Name: R-Biobase
Version: 2.20.0
Release: 1%{?dist}
License: Bioconductor
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.12/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.12/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel >= 3.0.0, R-BiocGenerics >= 0.6.0
Requires: R-core >= 3.0.0, R-BiocGenerics >= 0.6.0

%description
Functions that are needed by many other packages or which replace R functions.

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
* Wed Apr 24 2013 Shane Sturrock <shane@biomatters.com> R-Biobase-2.20.0-1
- Update to upstream (for R 3.0.0)
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-Biobase-2.16.0-1.el5
- Update to upstream (for R 2.15)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-Biobase-2.16.0-1.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-Biobase-2.8-0-1.el5
- Upgrade to 2.8
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-Biobase-2.6-1-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-Biobase-2.6.1-1.el5
- Updated for 2.6.1
* Wed May 6 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-Biobase-2.4.1-1.el5
- Updated for 2.4.1
* Tue Sep 30 2008 David Nutter <davidn@bioss.ac.uk> - R-bioconductor-Biobase-2.2.1-1.el5
- Initial build. Does not update search database

