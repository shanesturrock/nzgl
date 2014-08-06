%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name annotate

Summary: Annotation for microarrays
Name: R-annotate
Version: 1.34.1
Release: 2%{?dist}
License: Artistic-2.0
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel, R-AnnotationDbi >= 0.1.15, R-Biobase, R-DBI, R-xtable, R-XML, R-IRanges
Requires: R-core, R-AnnotationDbi >= 0.1.15, R-Biobase, R-DBI, R-xtable

%description
Using R enviroments for annotation

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
* Mon Aug 13 2012 Carl Jones <carl@biomatters.com> R-annotate-1.34.1-2
- Fix BuildRequires

* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-annotate-1.34.1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-annotate-1.30.1-1.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-annotate-1.26.0-2.el5
- Upgrade to 1.26
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-annotate-1.24.0-2.el5
- Renamed without -bioconductor
* Mon Feb 8 2010 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-annotate-1.24.0-2.el5
- Added xtable to "Requires:" list
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-annotate-1.24.0-1.el5
- Updated for 1.24
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-annotate-1.22.0-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-annotate-1.22.0-1.el5
- Initial build. Does not update search database

