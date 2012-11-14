%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name statmod
%define upstream_ver 1.4.14

Summary: Statistical Modelling
Name: R-statmod
Version: 1.4.14
Release: 1%{?dist}
License: LGPL (>= 2)
Group: Applications/Libraries
URL: http://cran.r-project.org/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://cran.r-project.org/src/contrib/%{short_name}_%{upstream_ver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel
Requires: R-core

%description
Various statistical modeling functions including growth
curve comparisons, limiting dilution analysis, mixed linear
models, heteroscedastic regression, Tweedie family generalized
linear models, the inverse-Gaussian distribution and Gauss quadrature.

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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-statmod-1.4.14-1.el5
- Update to upstream (for R 2.15)
* Tue Oct 11 2011 Alec Mann <alec@bioss.ac.uk> - R-statmod-1.4.11-1.el5
- Initial build (for R 2.13)

