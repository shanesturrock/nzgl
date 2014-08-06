%global packname  locfit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5_8
Release:          1%{?dist}
Summary:          Local Regression, Likelihood and Density Estimation.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              None
Source0:          locfit_1.5-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-akima R-lattice 
Requires:         R-gam 
BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-akima R-lattice 
BuildRequires:   R-gam 

%description
Local regression, likelihood and density estimation.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data/*
%{rlibdir}/%{packname}/libs/*

%changelog
* Sun Aug 12 2012 Carl Jones <carl@biomatters.com> -  1.5_8-1
- initial package
