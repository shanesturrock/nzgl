%global packname  XML
%global packver   3.9
%global packrel   4
%global rlibdir   %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          2%{?dist}
Summary:          Tools for parsing and generating xml within r and s-plus

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/XML/index.html
Source0:          http://cran.at.r-project.org/src/contrib/XML_%{packver}-%{packrel}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-core R-methods R-utils 
Requires:         R-bitops 
BuildRequires:    R-devel tex(latex) R-methods R-utils R-bitops
BuildRequires:    libxml2-devel

%description
This package provides many approaches for both reading and creating XML
(and HTML) documents (including DTDs), both local and accessible via HTTP
or FTP. It also offers access to an XPath "interpreter".

%prep
%setup -q -c -n %{packname}

find -name ".svn" |xargs rm -fr
%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# No need to ship this one
rm -f %{buildroot}%{rlibdir}/%{packname}/README.windows
# Rpmlint cannot read this file
rm -f %{buildroot}%{rlibdir}/%{packname}/exampleData/dtd.zip

%check
# Do not run the check as it requires internet access (and thus breaks the build)
#%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/Docs
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/exampleData
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/libs


%changelog
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 pingou <pingou@pingoured.fr> 3.9.4-1
- Update to version 3.9.4

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 3.4.3-2
- rebuild for R 2.14.0

* Thu Nov 03 2011 pingou <pingou@pingoured.fr> 3.4.3-1
- Update to version 3.4.3

* Wed Jun 22 2011 pingou <pingou@pingoured.fr> 3.4.0-1
- Update to version 3.4.0
- Update source and URL

* Wed Feb 16 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.2.0-2
- Comment out the check section as it breaks the build

* Sat Jan 29 2011 pingou <pingou@pingoured.fr> 3.2.0-1
- initial package for Fedora
