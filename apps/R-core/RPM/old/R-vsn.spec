%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name vsn

Summary: Variance stabilization and calibration for microarray data
Name: R-vsn
Version: 3.24.0
Release: 1%{?dist}
License: Artistic-2.0
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel, R-affy >= 1.23.4, R-Biobase >= 2.5.5, R-limma
Requires: R-core, R-affy >= 1.23.4, R-Biobase >= 2.5.5, R-limma

%description
The package implements a method for normalising microarray intensities,
both between colours within array, and between arrays. The method uses a 
robust variant of the maximum-likelihood estimator for the stochastic model of
microarray data described in the references (see vignette).
The model incorporates data calibration (a.k.a. normalization), a model for
the dependence of the variance on the mean intensity, and a
variance stabilizing data transformation. Differences between
transformed intensities are analogous to "normalized
log-ratios". However, in contrast to the latter, their
variance is independent of the mean, and they are usually more
sensitive and specific in detecting differential transcription

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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-vsn-3.24.0-1.el5
- Update to upstream (for R 2.15)
* Tue Oct 11 2011 Alec Mann <alec@bioss.ac.uk> - R-vsn-3.20.0-1.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-vsn-3.16.0-1.el5
- Upgrade to 3.16
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-vsn-3.14.0-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-vsn-3.14.0-1.el5
- Upgraded to 3.14
* Fri Jul 3 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-vsn-3.12.0-2.el5
- Correction to Summary line
* Thu Jun 25 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-vsn-3.12.0-1.el5
- Initial build. Does not update search database

