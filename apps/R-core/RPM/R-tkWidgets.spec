%global packname  tkWidgets
%global Rversion  2.11.0

Name:             R-%{packname}
Version:          1.34.0
Release:          2%{?dist}
Summary:          Widgets to provide user interfaces from bioconductor

Group:            Applications/Productivity
License:          Artistic 2.0
URL:              http://bioconductor.org/packages/release/bioc/html/tkWidgets.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch

Requires:         R-widgetTools R-DynDoc R-core >= %{Rversion}
BuildRequires:    R-devel >= %{Rversion} tcl-devel tk-devel R-widgetTools R-DynDoc tex(latex)

%description
Widgets to provide user interfaces. tcltk should have been installed for 
the widgets to run.

This package is a part of the bioconductor (bioconductor.org) project

%prep
%setup -c -q -n %{packname}

%build

%install
%{__rm} -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/R/library ; R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library

# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css


%check
# like R-widgetTools, the check says it needs Biobase, but Biobase needs tkWidgets.
# %{_bindir}/R CMD check %{packname}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{_datadir}/R/library/%{packname}
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/doc
%doc %{_datadir}/R/library/%{packname}/html
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/R
%{_datadir}/R/library/%{packname}/Meta
%{_datadir}/R/library/%{packname}/help
%{_datadir}/R/library/%{packname}/testfiles

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
- Fix url to a more stable form
- Fix R to R-core
- Fix description (a bit long)
- Remove R post/postun

* Sat Nov 21 2009 pingou <pingou@pingoured.fr> 1.24.0-1
- Update to 1.24.0
- Remove %%post and %%postun
- Adapt %%files to R-2.10.0
- Fix BR tex(latex)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 pingou <pingou@pingoured.fr> 1.22.0-1
- Update to Bioconductor 2.4 and R-2.9.0
- Uses global instead of define
- Change the license from LGPLv2+ to Artistic 2.0

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.20.0-1
- Update to 1.20.0 for R >= 2.8.0

* Tue Jun 25 2008 pingou <pingoufc4-at-yahoo.fr> 1.18.0-2
- Change urls

* Tue May 27 2008 pingou <pingoufc4-at-yahoo.fr> 1.18.0-1
- Update to version 1.18.0

* Tue Jan 08 2008 Pingou <pingoufc4@yahoo.fr> 1.16.0-2
- Change on the BR

* Mon Oct 08 2007 Pingou <pingoufc4@yahoo.fr> 1.16.0-1 
- Update to bioconductor 2.1 

* Wed Oct 03 2007  Pingou <pingoufc4@yahoo.fr> 1.14.0-6
- Change in the Requires

* Sun Aug 05 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-5
- Add the Requires(post) and Requires(postun)

* Tue Jul 10 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-4
- Change in the files post and postun to correct the noarch structure
- Change int the post and postun to fit with the packaging guidelines
- Change in the files section to mark the folder

* Mon Jun 24 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-3
- Change de %%doc to avoid redundancy

* Wed May 23 2007 Pingou <pingoufc4@yahoo.fr> 1.14.0-2
- Submitting to Fedora Extras

* Wed May 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.14.0-1
- initial package for Fedora
