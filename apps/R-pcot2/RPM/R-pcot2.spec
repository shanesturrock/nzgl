%global packname  pcot2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Principal Coordinates and Hotelling's T-Square method

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grDevices R-Biobase R-amap 

Requires:         R-multtest R-hu6800.db R-KEGG.db R-mvtnorm 
BuildRequires:    R-devel tex(latex) R-grDevices R-Biobase R-amap

BuildRequires:   R-multtest R-hu6800.db R-KEGG.db R-mvtnorm 

%description
PCOT2 is a permutation-based method for investigating changes in the
activity of multi-gene networks. It utilizes inter-gene correlation
information to detect significant alterations in gene network activities.
Currently it can be applied to two-sample comparisons.

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
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
#%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Mon Apr 8 2013 Shane Sturrock <shane@biomatters.com> 1.28.0-1
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> 1.26.0-1
- New upstream release
* Mon Aug 13 2012 Carl Jones <carl@biomatters.com> 1.24.0-1
- initial package for Fedora
