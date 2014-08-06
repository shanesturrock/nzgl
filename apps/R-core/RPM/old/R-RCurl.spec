%global packname  RCurl
%global packver   1.95
%global packrel   4.1

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          1%{?dist}
Summary:          General network (HTTP/FTP) client interface for R
Group:            Applications/Productivity
License:          BSD
URL:              http://cran.r-project.org/web/packages/RCurl/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz
Requires:         R-core >= 3.0.0 , texlive-latex, R-bitops, R-methods
BuildRequires:    R-devel >= 3.0.0 , R-bitops, R-methods, libcurl-devel
BuildRequires:    R-Rcompression, R-XML

%description
The package allows one to compose general HTTP requests and provides convenient 
functions to fetch URIs, get & post forms, etc. and process the results 
returned by the Web server. This provides a great deal of control over the 
HTTP/FTP/... connection and the form of the request while providing a 
higher-level interface than is available just using R socket connections. 
Additionally, the underlying implementation is robust and extensive, supporting 
FTP/FTPS/TFTP (uploads and downloads), SSL/HTTPS, telnet, dict, ldap, and also 
supports cookies, redirects, authentication, etc.

%prep
%setup -c -q -n %{packname}
chmod -x RCurl/src/curl_base64.c

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

%check
# Tests attempt to use the network, which won't work in koji.
# %{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/doc/
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/CurlSSL/
%{_libdir}/R/library/%{packname}/HTTPErrors/
%{_libdir}/R/library/%{packname}/data/
%{_libdir}/R/library/%{packname}/enums/
%{_libdir}/R/library/%{packname}/examples/

%changelog
* Fri Apr 26 2013 Shane Sturrock <shane@biomatters.com> - 1.95.4.1-5
- Upstream update for R-3.0.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Tom Callaway <spot@fedoraproject.org> 1.7.0-2
- disable tests

* Thu Nov 10 2011 Tom "spot" Callaway <tcallawa@redhat.com> 1.7.0-1
- initial package for Fedora
