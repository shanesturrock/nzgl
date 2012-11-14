%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name affyQCReport

Summary: QC Report Generation for affyBatch objects
Name: R-affyQCReport
Version: 1.36.0
Release: 1%{?dist}
License: LGPL version 2 or newer
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel, R-affy, R-affyPLM, R-Biobase >= 1.13.16, R-genefilter, R-RColorBrewer, R-simpleaffy, R-xtable, R-XML
Requires: R-core, R-affy, R-affyPLM, R-Biobase >= 1.13.16, R-genefilter, R-RColorBrewer, R-simpleaffy, R-xtable

%description
This package creates a QC report for an AffyBatch object.
The report is intended to allow the user to quickly assess the quality
of a set of arrays in an AffyBatch object

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
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> 1.36.0-1
- New upstream release
* Tue Aug 21 2012 Carl Jones <carl@biomatters.com> 1.34.0-2
- Fix build deps

* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-affyQCReport-1.34.0-1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-affyQCReport-1.30.0-1.el5
- Upgrade for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-affyQCReport-1.26.0-1.el5
- Upgrade to 1.26
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-affyQCReport-1.24.0-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affyQCReport-1.24.0-1.el5
- Upgrade to 1.24
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affyQCReport-1.22.0-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-affyQCReport-1.22.0-1.el5
- Initial build. Does not update search database

