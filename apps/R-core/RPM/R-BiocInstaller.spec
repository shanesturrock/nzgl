%global packname  BiocInstaller
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Install/Update Bioconductor and CRAN Packages

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core >= 3.0.0

Requires:         R-RUnit R-BiocGenerics >= 0.6.0
BuildRequires:    R-devel >= 3.0.0 tex(latex) 
BuildRequires:	  R-RUnit R-BiocGenerics >= 0.6.0

%description
Install4/updates Bioconductor and CRAN packages

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
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/scripts/biocLite.R
%{rlibdir}/%{packname}/unitTests/test_BiocUpgrade.R
%{rlibdir}/%{packname}/unitTests/test_biocinstallRepos.R

%changelog
* Wed Apr 24 2013 Shane Sturrock <shane@biomatters.com> 1.10.0-1
- Updates for R-3.0.0
* Mon Aug 20 2012 Carl Jones <carl@biomatters.com> 1.4.7-1
- initial package
