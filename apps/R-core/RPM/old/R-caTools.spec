%global packname  caTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14
Release:          1%{?dist}
Summary:          Tools: moving window statistics, GIF, Base64, ROC AUC, etc.

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-bitops 

Requires:         R-MASS R-rpart R >= 3.0.0
BuildRequires:    R-devel tex(latex) R-bitops

BuildRequires:   R-MASS R-rpart R >= 3.0.0

%description
Contains several basic utility functions including: moving (rolling,
running) window statistic functions, read/write for GIF and ENVI binary
files, fast calculation of AUC, LogitBoost classifier, base64
encoder/decoder, round-off error free sum and cumsum, etc.

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
#%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
#%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs/*


%changelog
* Mon Apr 8 2013 Shane Sturrock <shane@biomatters.com> 1.14-1
- Upstream update build against R-3.0.0
* Mon Aug 13 2012 Carl Jones <carl@biomatters.com> 1.13-1
- initial package for Fedora
