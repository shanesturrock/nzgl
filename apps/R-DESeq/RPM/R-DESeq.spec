%global packname  DESeq
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.1
Release:          1%{?dist}
Summary:          Differential gene expression analysis based on the negative binomial distribution

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-locfit 
Requires:         R-genefilter R-geneplotter R-methods R-MASS R-XML R-IRanges

BuildRequires:    R-devel tex(latex) R-Biobase R-locfit R-XML R-IRanges
BuildRequires:    R-genefilter R-geneplotter R-methods R-MASS 


%description
Estimate variance-mean dependence in count data from high-throughput
sequencing assays and test for differential expression based on a model
using the negative binomial distribution

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/extra/
%{rlibdir}/%{packname}/libs/
%{rlibdir}/%{packname}/scripts/*


%changelog
* Mon Aug 26 2013 Shane Sturrock <shane@biomatters.com> 1.12.1-1
- New upstream release, no info on why
* Mon Apr 8 2013 Shane Sturrock <shane@biomatters.com> 1.12.0-1
- New upstream release
* Mon Mar 18 2013 Shane Sturrock <shane@biomatters.com> 1.10.1-1
- New upstream release
* Wed Aug 29 2012 Carl Jones <carl@biomatters.com> 1.9.11-1
- New upstream release
* Wed Aug 22 2012 Carl Jones <carl@biomatters.com> 1.8.3-2
- Fix build deps
* Mon Aug 13 2012 Carl Jones <carl@biomatters.com> 1.8.3-1
- initial package 
