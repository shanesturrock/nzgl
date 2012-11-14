%global packname  org.Hs.eg.db
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.7.1
Release:          2%{?dist}
Summary:          Genome wide annotation for Human

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-AnnotationDbi 
Requires:         R-methods R-AnnotationDbi 
Requires:         R-annotate  R-IRanges
BuildRequires:    R-devel tex(latex) R-methods R-AnnotationDbi
BuildRequires:    R-methods R-AnnotationDbi 
BuildRequires:   R-annotate R-IRanges

%description
Genome wide annotation for Human, primarily based on mapping using Entrez
Gene identifiers.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
#%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
#%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
#%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/extdata/org.Hs.eg.sqlite


%changelog
* Wed Aug 22 2012 Carl Jones <carl@biomatters.com> 2.7.1-2
- Fix build deps
* Mon Aug 13 2012 Carl Jones <carl@biomatters.com> 2.7.1-1
- initial package
