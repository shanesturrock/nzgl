%global packname  bitops
%global packvers 1.0-5

Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Functions for Bitwise operations

Group:            Applications/Productivity
License:          GPLv2+
URL:              http://cran.r-project.org/web/packages/bitops/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{packvers}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         R-core, R >= 3.0.0
BuildRequires:    R-devel, tex(latex), R >= 3.0.0

%description
Functions for Bitwise operations on integer vectors.

%prep
%setup -c -q -n %{packname}
%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_libdir}/R/library/R.css

%check
%{_bindir}/R CMD check %{packname}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs

%changelog
* Mon Apr 8 2013 Shane Sturrock <shane@biomatters.com> - 1.0.5-1
- Upstream update built for R-3.0.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.4.1-6
- rebuild for R 2.14.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 08 2010 josef radinger <cheese@nosuchhost.net>
- 1.0.4.1-4
- tetex-latex -> tex(latex)

* Sat May 08 2010 josef radinger <cheese@nosuchhost.net>
- 1.0.4.1-3
- fresh build

* Fri May 07 2010 josef radinger <cheese@nosuchhost.net>
- 1.0.4.1-2
- BuildRequires latex

* Fri Apr 09 2010 josef radinger <cheese@nosuchhost.net>
- 1.0.4.1-1
- initial release
