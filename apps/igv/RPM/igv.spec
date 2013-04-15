Name:		igv
Version:	2.3.0
Release:	1%{?dist}
Summary:	Integrative Genomics Viewer
Group:		Applications/Engineering
License:	LGPL
URL:		http://www.broadinstitute.org/igv/home
Source0:	http://www.broadinstitute.org/igv/projects/downloads/IGVDistribution_%{version}.zip
Source1:	igv
Source2:	igv.desktop
Source3:	igv-icons.tar.gz
Requires:	java-1.6.0 dejavu-sans-fonts dejavu-sans-mono-fonts dejavu-serif-fonts
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	ant

%description
The Integrative Genomics Viewer (IGV) is a high-performance visualization tool for interactive exploration 
of large, integrated genomic datasets. It supports a wide variety of data types, including array-based and 
next-generation sequence data, and genomic annotations.

%prep
%setup -q -n IGVDistribution_%{version}

%build
/usr/bin/ant -Dinclude.libs=true

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_javadir}/%{name}/lib
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}
install -m 0644 igv.jar %{buildroot}/%{_javadir}/%{name}
install -m 0644 lib/*.jar %{buildroot}/%{_javadir}/%{name}/lib

# Icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/
tar xf %{SOURCE3} -C %{buildroot}%{_datadir}/icons/hicolor/

# .desktop
mkdir -p %{buildroot}%{_datadir}/applications/
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet /usr/share/icons/hicolor
fi

%files
%defattr(-,root,root,-)
/usr/bin/igv
/usr/share/java/igv/lib/*.jar
/usr/share/java/igv/igv.jar
/usr/share/icons/hicolor/*
/usr/share/applications/igv.desktop

%changelog
* Tue Apr 16 2013 Shane Sturrock <shane@biomatters.com> - 2.3.0-1
- New upstream release

* Wed Mar 25 2013 Shane Sturrock <shane@biomatters.com> - 2.2.13-1
- New upstream release

* Wed Mar 20 2013 Shane Sturrock <shane@biomatters.com> - 2.2.12-1
- New upstream release

* Mon Mar 18 2013 Shane Sturrock <shane@biomatters.com> - 2.2.11-1
- New upstream release

* Mon Mar 11 2013 Simon Buxton <simon@biomatters.com> - 2.2.9-0
- New upstream release

* Mon Mar 04 2013 Shane Sturrock <shane@biomatters.com> - 2.2.8-0
- New upstream release

* Thu Feb 21 2013 Carl Jones <carl@biomatters.com> - 2.2.6-0
- New upstream release

* Thu Feb 07 2013 Carl Jones <carl@biomatters.com> - 2.2.5-2
- Update .desktop file

* Tue Jan 29 2013 Carl Jones <carl@biomatters.com> - 2.2.5-1
- New upstream release

* Wed Jan 23 2013 Carl Jones <carl@biomatters.com> - 2.2.4-3
- Run gtk-update-icon-cache after install to enable desktop icons
- Fix icon paths

* Wed Jan 23 2013 Carl Jones <carl@biomatters.com> - 2.2.4-2
- Add icons, .desktop file

* Wed Jan 15 2013 Carl Jones <carl@biomatters.com> - 2.2.4-1
- New upstream release

* Mon Jan 13 2013 Carl Jones <carl@biomatters.com> - 2.2.3-1
- New upstream release

* Tue Jan 08 2013 Carl Jones <carl@biomatters.com> - 2.2.2-1
- New upstream release

* Thu Dec 20 2012 Carl Jones <carl@biomatters.com> - 2.2.0-1
- New upstream release

* Thu Dec 13 2012 Carl Jones <carl@biomatters.com> - 2.1.30-1
- New upstream release
* Fri Dec 07 2012 Carl Jones <carl@biomatters.com> - 2.1.29-1
- New upstream release
* Wed Nov 14 2012 Carl Jones <carl@biomatters.com> - 2.1.28-1
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 2.1.27-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 2.1.24-1
- New upstream release

* Fri Aug 8 2012 Carl Jones <carl@biomatters.com> - 2.1.21-4
- Fix Java paths

* Wed Aug 1 2012 Carl Jones <carl@biomatters.com> - 2.1.21-3
- Fix font deps

* Wed Aug 1 2012 Carl Jones <carl@biomatters.com> - 2.1.21-3
- Include profile.d/igv.sh

* Wed Aug 1 2012 Carl Jones <carl@biomatters.com> - 2.1.21-1
- Initial build.
