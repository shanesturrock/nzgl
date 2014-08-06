%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name Biostrings

Summary: String objects representing biological sequences, and matching algorithms
Name: R-Biostrings
Version: 2.24.1
Release: 1%{?dist}
License: Artistic-2.0
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel >= 2.8.0, R-IRanges >= 1.10.2
Requires: R-core >= 2.8.0, R-IRanges >= 1.10.2

%description
Memory efficient string containers, string matching algorithms,
and other utilities, for fast manipulation of large
biological sequences or set of sequences

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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-Biostrings-2.24.1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-Biostrings-2.20.2-1.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-Biostrings-2.16.2-1.el5
- Upgrade to 2.16
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-Biostrings-2.14.8-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-Biostrings-2.14.8-1.el5
- Updated to 2.14
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-Biostrings-2.12.7-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-Biostrings-2.12.7-1.el5
- Initial build. Does not update search database

