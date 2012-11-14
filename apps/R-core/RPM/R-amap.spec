%global packname  amap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.7
Release:          1%{?dist}
Summary:          Another Multidimensional Analysis Package

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



Requires:         R-Biobase 
BuildRequires:    R-devel tex(latex) 

BuildRequires:   R-Biobase 

%description
Tools for Clustering and Principal Component Analysis (With robusts
methods, and parallelized functions).

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
%{rlibdir}/%{packname}/data/*
%{rlibdir}/%{packname}/libs/*
%{rlibdir}/%{packname}/demo/*
%{rlibdir}/%{packname}/exec/*
%{rlibdir}/%{packname}/po/*

%changelog
* Mon Aug 13 2012 Carl Jones <carl@biomatters.com> 0.8.7-1
- initial package for Fedora
