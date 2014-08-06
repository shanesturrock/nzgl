%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name gam
%define upstream_ver 1.06.2

Summary: Generalized Additive Models
Name: R-gam
Version: 1.06.2
Release: 1%{?dist}
License: GPL-2
Group: Applications/Libraries
URL: http://cran.r-project.org/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://cran.r-project.org/src/contrib/%{short_name}_%{upstream_ver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel
Requires: R-core

%description
Functions for fitting and working with generalized
additive models, as described in chapter 7 of "Statistical
Models in S" (Chambers and Hastie (eds), 1991), and
"Generalized Additive Models" (Hastie and Tibshirani, 1990).

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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-gam-1.06.2-1.el5
- Update to upstream (for R 2.15.1)
* Tue Oct 11 2011 Alec Mann <alec@bioss.ac.uk> - R-gam-1.04.1-1.el5
- Initial build (for R 2.13)

