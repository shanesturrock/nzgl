%define packname  DynDoc
%define Rversion  2.10.0

Name:             R-%{packname}
Version:          1.34.0
Release:          2%{?dist}
Summary:          Functions for dynamic documents

Group:            Applications/Productivity
License:          Artistic 2.0
URL:              http://bioconductor.org/packages/release/bioc/html/DynDoc.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch

Requires:         R-core >= %{Rversion}
Requires(post):   R-core >= %{Rversion}
Requires(postun): R-core
BuildRequires:    R-devel >= %{Rversion} tex(latex)

%description
A set of functions to create and interact with dynamic documents and 
vignettes.

%prep
%setup -c -q -n %{packname}

%build

%install
%{__rm} -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/R/library
R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library

# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css


%check
%{_bindir}/R CMD check %{packname}

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, -)
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/help


%changelog
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 pingou <pingou@pingoured.fr> 1.34.0-1
- Update to version 1.34.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> 1.32.0-2
- rebuild for R 2.14.0

* Thu Nov 03 2011 pingou <pingou@pingoured.fr> 1.32.0-1
- Update to version 1.32.0

* Wed Jun 22 2011 pingou <pingou@pingoured.fr> 1.30.0-1
- Update to version 1.30.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 26 2010 pingou <pingou@pingoured.fr> 1.28.0-1
- Update to version 1.28.0

* Tue May 11 2010 pingou <pingou@pingoured.fr> 1.26.0-1
- Update to version 1.26.0
- Update url and source0 to more stable link
- Requires R-core instead of R
- Requires tex(latex)

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.24.0-1
- Update to 1.24.0
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 pingou <pingou@pingoured.fr> 1.22.0-1
- Update to Bioconductor 2.4 and R-2.9.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.20.0-1
- Update to version 1.20.0 for R >= 2.8.0

* Wed Jun 25 2008 Pingou <pingoufc4@yahoo.fr> 1.18.0-2
- Change the url

* Fri May 02 2008 Pingou <pingoufc4@yahoo.fr> 1.18.0-1
- Update to bioconductor 2.2

* Mon Oct 08 2007 Pingou <pingoufc4@yahoo.fr> 1.17.0-1
- Update to bioconductor 2.1

* Wed Aug 29 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-5
-Change the license tag

* Fri Jul 13 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-4
- Change in the BR and R to fit the guidelines

* Tue Jul 10 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-3
- Change _libdir to _datadir as it is a noarch package
- Change in the files section to mark the folder
- Change in the post and postun section to fit with the packaging guidelines
- Change in the prep section to fit with the packaging guidelines

* Wed May 23 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-2
- Submitting to Fedora Extras

* Wed May 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.14.0-1
- initial package for Fedora
