%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name xtable
%define upstream_ver 1.7-0

Summary: Base functions for R
Name: R-xtable
Version: 1.7.0
Release: 1%{?dist}
License: GPL
Group: Applications/Libraries
URL: http://cran.r-project.org/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://cran.r-project.org/src/contrib/%{short_name}_%{upstream_ver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel
Requires: R-core

%description
Coerce data to LaTeX and HTML tables

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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-xtable-1.7.0-1.el5
- Update to upstream (for R 2.15)
* Tue Oct 11 2011 Alec Mann <alec@bioss.ac.uk> - R-xtable-1.5.6-2.el5
- Upgraded for R 2.13
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-xtable-1.5.6-1.el5
- Renamed without -cran
* Wed Dec 10 2009 Alec Mann <alec@bioss.ac.uk> - R-cran-xtable-1.5.6-1.el5
- Updated for 1.5-6
* Fri Jun 26 2009 Alec Mann <alec@bioss.ac.uk> - R-cran-xtable-1.5-5.el5
- Initial build. Does not update search database

