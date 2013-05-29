%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name limma

Summary: Data analysis, linear models and differential expression for microarray data.
Name: R-limma
Version: 3.16.5
Release: 2%{?dist}
License: LGPL
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel >= 3.0.0
Requires: R-core >= 3.0.0

%description
Data analysis, linear models and differential expression for microarray data.

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
* Wed May 29 2013 Simon Buxton <simon@biomatters.com> - 3.16.5-2
- New upstream release
* Mon May 20 2013 Simon Buxton <simon@biomatters.com> - 3.16.4-2
- Rebuild for R 3.0.0 of new upstream release
* Fri May 03 2013 Shane Sturrock <shane@biomatters.com> - 3.16.3-2
- Rebuild for R 3.0.0 of new upstream release
* Tue Apr 30 2013 Shane Sturrock <shane@biomatters.com> - 3.16.2-2
- Rebuild for R 3.0.0 of new upstream release
* Wed Apr 24 2013 Shane Sturrock <shane@biomatters.com> - 3.16.1-2
- Rebuild for R 3.0.0
* Tue Apr 09 2013 Shane Sturrock <shane@biomatters.com> - 3.16.1-1
- New upstream release
* Mon Dec 03 2012 Carl Jones <carl@biomatters.com> - 3.14.1-3
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 3.14.1-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 3.12.3-1
- New upstream release
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-limma-3.12.1-1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-limma-3.8.3-1.el5
- upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-limma-3.4.3-1.el5
- upgrade to 3.4
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-limma-3.2.1-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-limma-3.2.1-1.el5
- Updated for 3.2
* Wed May 6 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-limma-2.18.0-1.el5
- Updated for 2.18.0
* Tue Sep 30 2008 David Nutter <davidn@bioss.ac.uk> - R-bioconductor-limma-2.14.7-1.el5
- Initial build. Does not update search database

