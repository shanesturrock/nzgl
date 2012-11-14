%global packname  gdata
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.11.0
Release:          1%{?dist}
Summary:          Various R programming tools for data manipulation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-gtools 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-gtools 


%description
Various R programming tools for data manipulation

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
rm -rf %{buildroot}%{rlibdir}/%{packname}/perl/
rm -rf %{buildroot}%{rlibdir}/%{packname}/bin/

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
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests/*
#%{rlibdir}/%{packname}/bin/*
%{rlibdir}/%{packname}/data/*
#%{rlibdir}/%{packname}/perl/*
%{rlibdir}/%{packname}/xls/*



%changelog
* Mon Aug 13 2012 Carl Jones <carl@biomatters.com> 2.11.0-1
- initial package for Fedora
