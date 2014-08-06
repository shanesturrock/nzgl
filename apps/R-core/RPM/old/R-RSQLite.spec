%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name RSQLite
%define upstream_ver 0.11.1

Summary: SQLite interface for R
Name: R-RSQLite
Version: 0.11.1
Release: 1%{?dist}
License: LGPL version 2 or later
Group: Applications/Libraries
URL: http://cran.r-project.org/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://cran.r-project.org/src/contrib/%{short_name}_%{upstream_ver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel >= 2.10.0, R-DBI >= 0.2.5
Requires: R-core >= 2.10.0, R-DBI >= 0.2.5

%description
Database Interface R driver for SQLite.
This package embeds the SQLite database engine in R and
provides an interface compliant with the DBI package.
The source for the SQLite engine (version 3.6.4) is included.

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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R--RSQLite-0.11.1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-RSQLite-0.10.0-1.el5
- upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-RSQLite-0.9-1.el5
- upgrade to 0.9
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-RSQLite-0.7-3.el5
- Renamed without -cran
* Thu Dec 10 2009 Alec Mann <alec@bioss.ac.uk> - R-cran-RSQLite-0.7-3.el5
- Updated for 0.7-3
* Fri Jun 26 2009 Alec Mann <alec@bioss.ac.uk> - R-cran-RSQLite-0.7-1.el5
- Initial build. Does not update search database

