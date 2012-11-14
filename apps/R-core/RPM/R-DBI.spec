%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name DBI
%define upstream_ver 0.2-5

Summary: R Database Interface
Name: R-DBI
Version: 0.2.5
Release: 3%{?dist}
License: LGPL (version 2 or later)
Group: Applications/Libraries
URL: http://cran.r-project.org/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://cran.r-project.org/src/contrib/%{short_name}_%{upstream_ver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel
Requires: R-core

%description
A database interface (DBI) definition for
communication between R and relational database management
systems.  All classes in this package are virtual and need
to be extended by the various R/DBMS implementations.


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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-DBI-0.2.5-3.el5
- Rebuild for R 2.15
* Tue Oct 11 2011 Alec Mann <alec@bioss.ac.uk> - R-DBI-0.2.5-2.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-DBI-0.2.5-1.el5
- Upgrade to 0.2.5
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-DBI-0.2-5.el5
- Renamed without -cran
* Wed Dec 16 2009 Alec Mann <alec@bioss.ac.uk> - R-cran-DBI-0.2-5.el5
- Rebuilt with R 2.10
* Fri Jun 26 2009 Alec Mann <alec@bioss.ac.uk> - R-cran-DBI-0.2-4.el5
- Initial build. Does not update search database

