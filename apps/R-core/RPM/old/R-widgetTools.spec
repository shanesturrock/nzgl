%global packname  widgetTools
%global Rversion  2.11.0

Name:             R-%{packname}
Version:          1.34.0
Release:          2%{?dist}
Summary:          Bioconductor tools to support tcltk widgets

Group:            Applications/Productivity
License:          LGPLv2+
URL:              http://bioconductor.org/packages/release/bioc/html/widgetTools.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch

Requires:         R-core >= %{Rversion}
BuildRequires:    R-devel >= %{Rversion}, tcl-devel, tk-devel, tex(latex)

%description
This package contains tools to support the construction of tcltk widgets.

This library is part of the bioconductor (bioconductor.org) project

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

# PDF doesn't need to be executable
chmod -x %{packname}/inst/doc/widget.pdf

%check
# Can't run this. It says we need Biobase. Biobase really needs this, and tkWidgets to run its check.
# %{_bindir}/R CMD check %{packname}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
#%{_datadir}/R/library/%{packname}
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/doc
%doc %{_datadir}/R/library/%{packname}/html
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
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
- Fix url to more stable version
- Remove requires(post/postun) since there is no post/postun anymore

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.24.0-1
- Update to 1.24.0
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0
- Fix BR tex(latex)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 pingou <pingou@pingoured.fr> 1.22.0-1
- Update to Bioconductor 2.4 and R-2.9.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.18.0-1
- Update to version 1.18.0 for R >= 2.8.0

* Tue May 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.16.0-3
- Change in Source1

* Tue May 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.16.0-2
- Change in Source1
- Change in the url

* Tue May 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.16.0-1
- Update to version 1.16.0

* Sat Feb 09 2008 Pingou <pingoufc4@yahoo.fr> 1.15.0-3
- Correct typo error on the URL

* Tue Jan 08 2008 Pingou <pingoufc4@yahoo.fr> 1.15.0-2
- Change BR

* Mon Oct 08 2007 Pingou <pingoufc4@yahoo.fr> 1.15.0-1 
- Update to bioconductor 2.1 

* Tue Jul 10 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-12
- Add the requires on R

* Thu Jul 05 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-11
- Change in the post 

* Thu Jul 05 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-10
- Put the man pages as doc
- Correction on the post and postun macro (to fit with the new
R packaging guidelines)

* Tue Jul 03 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-9
- Test on the postun

* Tue Jul 03 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-8
- Change in the files section to add the dir

* Sun Jul 01 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-7
- Change in the files section

* Sat Jun 30 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-6
- Mark the html file as doc file

* Wed Jun 27 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-5
- Remove the DESCRIPTION file in /R/library

* Tue Jun 26 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-4
- Change _libdir to _datadir as it is a noarch package

* Mon Jun 25 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-3
- Change de %%doc to avoid redundancy

* Wed May 23 2007 Pingou <pingoufc4@yahoo.fr> 1.12.0-2
- Submitting to Fedora Extras

* Wed May 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.12.0-1
- initial package for Fedora
