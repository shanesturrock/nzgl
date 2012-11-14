%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name simpleaffy

Summary: Very simple high level analysis of Affymetrix data
Name: R-simpleaffy
Version: 2.32.0
Release: 1%{?dist}
License: GPL version 2 or later
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel, R-affy, R-Biobase, R-gcrma, R-genefilter, R-XML
Requires: R-core, R-affy, R-Biobase, R-gcrma, R-genefilter

%description
Provides high level functions for reading Affy .CEL
files, phenotypic data, and then computing simple things with
it, such as t-tests, fold changes and the like. Makes heavy
use of the affy library. Also has some basic scatter plot
functions and mechanisms for generating high resolution
journal figures

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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-simpleaffy-2.32.0.el5
- Update to upstream (for R 2.15)
* Tue Oct 11 2011 Alec Mann <alec@bioss.ac.uk> - R-simpleaffy-2.28.0-1.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-simpleaffy-2.24.0-1.el5
- Upgrade to 2.24
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-simpleaffy-2.22.0-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-simpleaffy-2.22.0-1.el5
- Upgraded for 2.22
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-simpleaffy-2.20.0-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-simpleaffy-2.20.0-1.el5
- Initial build. Does not update search database

