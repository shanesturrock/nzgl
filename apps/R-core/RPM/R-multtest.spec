%define debug_package %{nil}
%define __Rbinary %{_bindir}/R
%define Rlibdir %{_libdir}/R/library
%define short_name multtest

Summary: Resampling-based multiple hypothesis testing
Name: R-multtest
Version: 2.12.0
Release: 1%{?dist}
License: LGPL
Group: Applications/Libraries
URL: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
Source0: http://www.bioconductor.org/packages/2.10/bioc/src/contrib/%{short_name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: R-devel >= 2.9.0, R-Biobase
Requires: R-core >= 2.9.0, R-Biobase

%description
Non-parametric bootstrap and permutation resampling-based
multiple testing procedures (including empirical Bayes methods) for
controlling the family-wise error rate (FWER), generalized family-wise
error rate (gFWER), tail probability of the proportion of false
positives (TPPFP), and false discovery rate (FDR).  Several choices of
bootstrap-based null distribution are implemented (centered, centered
and scaled, quantile-transformed). Single-step and step-wise methods
are available. Tests based on a variety of t- and F-statistics
(including t-statistics based on regression parameters from linear and
survival models as well as those based on correlation parameters) are
included.  When probing hypotheses with t-statistics, users may also
select a potentially faster null distribution which is multivariate
normal with mean zero and variance covariance matrix derived from the
vector influence function.  Results are reported in terms of adjusted
p-values, confidence regions and test statistic cutoffs. The procedures
are directly applicable to identifying differentially expressed genes in
DNA microarray experiments.

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
* Wed Jul 11 2012 David Nutter <davidn@bioss.ac.uk> R-multtest-2.12.0-1.el5
- Update to upstream (for R 2.15.1)
* Mon Oct 10 2011 Alec Mann <alec@bioss.ac.uk> - R-multtest-2.8.0-1.el5
- Upgraded for R 2.13
* Tue Jun 8 2010 Alec Mann <alec@bioss.ac.uk> - R-multtest-2.4.0-1.el5
- Upgrade to 2.4
* Wed Mar 24 2010 Alec Mann <alec@bioss.ac.uk> - R-multtest-2.2.0-1.el5
- Renamed without -bioconductor
* Wed Dec 9 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-multtest-2.2.0-1.el5
- Updated for 2.2.0
* Wed May 6 2009 Alec Mann <alec@bioss.ac.uk> - R-bioconductor-multtest-2.0.0-1.el5
- Updated for 2.0.0
* Tue Sep 30 2008 David Nutter <davidn@bioss.ac.uk> - R-bioconductor-multtest-1.22.0-1.el5
- Initial build. Does not update search database

