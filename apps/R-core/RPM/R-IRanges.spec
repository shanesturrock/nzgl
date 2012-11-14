%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name IRanges

Summary: Infrastructure for manipulating intervals on sequences
Name: R-IRanges
Version: 1.14.4
Release: 1%{?dist}
License: Artistic-2.0
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel >= 2.8.0, R-BiocGenerics
Requires: R-core >= 2.8.0, R-BiocGenerics

%description
The package provides efficient low-level and highly reusable S4
classes for storing ranges of integers, RLE vectors (Run-Length
Encoding), and, more generally, data that can be organized
sequentially (formally defined as Vector objects), as well as views
on these Vector objects.
Efficient list-like classes are also provided for storing big
collections of instances of the basic classes. All classes in
the package use consistent naming and share the same rich and
consistent "Vector API" as much as possible.

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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-IRanges-1.14.4-1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-IRanges-1.10.6-1.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-IRanges-1.6.6-1.el5
- Upgraded to 1.6
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-IRanges-1.4.9-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-IRanges-1.4.9-1.el5
- Updated for 1.4.9
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-IRanges-1.2.3-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-IRanges-1.2.3-1.el5
- Initial build. Does not update search database

