%global packname  preprocessCore
%global Rvers     2.11.0

Name:             R-%{packname}
Version:          1.18.0
Release:          2%{?dist}
Summary:          A collection of pre-processing functions

Group:            Applications/Engineering 
License:          LGPLv2+  
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Source1:          preprocessCore_license
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-core >= %{Rvers}
BuildRequires:    R-devel >= %{Rvers} tex(latex) R-methods 

%package           devel
Summary:           Development files for %{name}        
Group:             Development/Libraries
Requires:          %{name}%{?_isa} = %{version}-%{release} 


%description
A library of core preprocessing routines

%description    devel
The %{name}-devel  package contains Header and libraries files for
developing applications that use %{name}

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir}/R/library 
R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

## Keep the headers of place for the -devel
## see: https://www.redhat.com/archives/fedora-r-devel-list/2009-March/msg00001.html

install -m 664 -p %{SOURCE1}  %{buildroot}%{_libdir}/R/library/%{packname}

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
#i386 arch
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/preprocessCore_license
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/help

%files          devel
%defattr(-,root,root,-)
%{_libdir}/R/library/%{packname}/include/

%changelog
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 pingou <pingou@pingoured.fr> 1.18.0-1
- Update to version 1.18.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Tom Callaway <spot@fedoraproject.org> 1.16.0-2
- rebuild for R 2.14.0

* Thu Nov 03 2011 pingou <pingou@pingoured.fr> 1.16.0-1
- Update to version 1.16.0

* Wed Jun 22 2011 pingou <pingou@pingoured.fr> 1.14.0-1
- Update to version 1.14.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 1.12.0-1
- Update to version 1.12.0

* Sat Jun 05 2010 pingou <pingou@pingoured.fr> 1.10.0-1
- Update to version 1.10.0
- Update source0 and URL to a more stable form
- Update R and BR to R-core and R-devel
- Update to R-2.11.0

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.8.0-1
- Update to 1.8.0
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0
- Fix BR tex(latex)

* Tue Aug 04 2009 pingou <pingou@pingoured.fr> 1.6.0-2
- Add the file preprocessCore_license which contains the mail from upstream regarding the license

* Sat Aug 01 2009 pingou <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora
