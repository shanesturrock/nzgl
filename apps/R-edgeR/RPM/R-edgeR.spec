%global packname  edgeR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.2.4
Release:          2%{?dist}
Summary:          Empirical analysis of digital gene expression data in R

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-limma R >= 3.0.0

Requires:         R-MASS R-statmod R-splines 
BuildRequires:    R-devel >= 3.0.0
BuildRequires:    tex(latex) R-methods R-limma

BuildRequires:    R-MASS R-statmod R-splines 

%description
Differential expression analysis of RNA-seq and digital gene expression
profiles with biological replication.  Uses empirical Bayes estimation and
exact tests based on the negative binomial distribution.  Also useful for
differential signal analysis with other types of genome-scale count data.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data/*
%{rlibdir}/%{packname}/libs/edgeR.so

%changelog
* Wed Jul 17 2013 Shane Sturrock <shane@biomatters.com> 3.2.4-2
- Rebuild against R-3.0.0 for testing repo
* Mon Apr 22 2013 Shane Sturrock <shane@biomatters.com> 3.2.3-2
- Rebuild against R-3.0.0 for testing repo
* Mon Apr 22 2013 Shane Sturrock <shane@biomatters.com> 3.2.3-1
- New upstream release
* Tue Apr 16 2013 Shane Sturrock <shane@biomatters.com> 3.2.2-1
- New upstream release
* Tue Apr 09 2013 Shane Sturrock <shane@biomatters.com> 3.2.1-1
- New upstream release
* Mon Apr 08 2013 Shane Sturrock <shane@biomatters.com> 3.2.0-1
- New upstream release
* Tue Jan 08 2013 Carl Jones <carl@biomatters.com> 3.0.8-1
- New upstream release

* Mon Dec 17 2012 Carl Jones <carl@biomatters.com> 3.0.7-1
- New upstream release
* Tue Dec 11 2012 Carl Jones <carl@biomatters.com> 3.0.6-1
- New upstream release
* Fri Dec 07 2012 Carl Jones <carl@biomatters.com> 3.0.5-1
- New upstream release
* Fri Nov 16 2012 Carl Jones <carl@biomatters.com> 3.0.4-1
- New upstream release
* Wed Nov 14 2012 Carl Jones <carl@biomatters.com> 3.0.3-1
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> 3.0.2-1
- New upstream release
* Thu Aug 30 2012 Carl Jones <carl@biomatters.com> 2.6.12-1
- New upstream release
* Mon Aug 13 2012 Carl Jones <carl@biomatters.com> 2.6.10-1
- initial package for Fedora
