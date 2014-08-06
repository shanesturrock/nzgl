%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name AnnotationDbi

Summary: Annotation Database Interface
Name: R-AnnotationDbi
Version: 1.18.1
Release: 2%{?dist}
License: Artistic-2.0
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel, R-Biobase, R-DBI, R-RSQLite, R-IRanges
Requires: R-core, R-Biobase, R-DBI, R-RSQLite

%description
Provides user interface and database connection code
for annotation data packages using SQLite data storage

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
* Mon Aug 20 2012 Carl Jones <carl@biomatters.com> R-AnnotationDbi-1.18.1-2
- Fix build deps for EL6
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-AnnotationDbi-1.18.1-1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-AnnotationDbi-1.14.1-1.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-AnnotationDbi-1.10.1-1.el5
- Upgrade to 1.10
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-AnnotationDbi-1.8.1-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-AnnotationDbi-1.8.1-1.el5
- Correction to Summary line
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-AnnotationDbi-1.6.1-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-AnnotationDbi-1.6.1-1.el5
- Initial build. Does not update search database

