%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name affyPLM

Summary: Methods for fitting probe-level models
Name: R-affyPLM
Version: 1.32.0
Release: 2%{?dist}
License: GPL version 2 or newer
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel, R-affy >= 1.11.0, R-Biobase, R-gcrma, R-preprocessCore >= 1.5.1, R-zlibbioc, R-preprocessCore-devel
Requires: R-core, R-affy >= 1.11.0, R-Biobase, R-gcrma, R-preprocessCore >= 1.5.1

%description
A package that extends and improves the functionality of
the base affy package. Routines that make heavy use of
compiled code for speed. Central focus is on implementation of
methods for fitting probe-level models and tools using these
models. PLM based quality assessment tools.

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
* Mon Aug 13 2012 Carl Jones <carl@biomatters.com> - R-affyPLM-1.32.0-2
- Fix BuildRequires

* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-affyPLM-1.32.0-1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-affyPLM-1.28.5-1.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-affyPLM-1.24.0-1.el5
- Upgraded to 1.24
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-affyPLM-1.22.0-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affyPLM-1.22.0-1.el5
- Updated to 1.22
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affyPLM-1.20.0-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affyPLM-1.20.0-1.el5
- Initial build. Does not update search database

