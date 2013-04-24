%global packname  RUnit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.26
Release:          2%{?dist}
Summary:          R Unit test framework

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils R-methods 


BuildRequires:    R-devel >= 3.0.0 tex(latex) R-utils R-methods



%description
R functions implementing a standard Unit Testing framework, with
additional code inspection and report generation tools

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
sed 's=%{buildroot}==g' --in-place %{buildroot}/usr/lib64/R/library/RUnit/html/checkFuncs.html

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/share/*
%{rlibdir}/%{packname}/unitTests/*
%{rlibdir}/%{packname}/examples/*


%changelog
* Tue Apr 24 2013 Shane Sturrock <shane@biomatters.com> 0.4.26-2
- Rebuild for R-3
* Mon Aug 13 2012 Carl Jones <carl@biomatters.com> 0.4.26-1
- initial package for Fedora
