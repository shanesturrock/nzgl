%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name RColorBrewer
%define upstream_ver 1.0-5

Summary: ColorBrewer palettes
Name: R-RColorBrewer
Version: 1.0.5
Release: 3%{?dist}
License: GPL
Group: Applications/Libraries
URL: http://cran.r-project.org/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://cran.r-project.org/src/contrib/%{short_name}_%{upstream_ver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel >= 3.0.0
Requires: R-core >= 3.0.0

%description
Provides palettes for drawing nice maps shaded according to a variable.

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
* Fri Apr 26 2013 Shane Sturrock <shane@biomatters.com> 1.0.5-3
- Rebuild for R 3.0.0
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-RColorBrewer-1.0.5-2.el5
- Rebuild for R 2.15
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-RColorBrewer-1.0.5-2.el5
- Upgraded for R 2.13
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-RColorBrewer-1.0.2-2.el5
- Renamed without -cran
* Wed Dec 16 2009 Alec Mann <alec@bioss.ac.uk> - R-cran-RColorBrewer-1.0.2-2.el5
- Rebuilt with R 2.10
* Fri Mar 13 2009 Alec Mann <alec@bioss.ac.uk> - R-cran-RColorBrewer-1.0.2-1.el5
- Initial build. Does not update search database

