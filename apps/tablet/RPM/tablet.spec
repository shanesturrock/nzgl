Name:		tablet
Version:	1.13.12.13
Release:	1%{?dist}
Summary:	Lightweight, high-performance graphical viewer for next generation sequence assemblies and alignments.
Group:		Applications/Engineering
License:	BSD Modified
URL:		http://bioinf.scri.ac.uk/tablet/index.shtml
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.gz
Source2:	%{name}.desktop
Patch0:		%{name}-apphomefix.patch
#Patch1:		maqtoace-apphomefix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	java-1.7.0-openjdk

%description
Tablet is a lightweight, high-performance graphical viewer for next generation sequence assemblies and alignments.

%prep
%setup -q  -n Tablet
%patch0 -p0
#%patch1 -p0

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_javadir}/%{name}

install -m 0755 %{name} %{buildroot}/%{_bindir}
#install -m 0755 maqtoace %{buildroot}/%{_bindir}
/bin/cp -r lib/ %{buildroot}/%{_javadir}/%{name}
/bin/cp -r .install4j/ %{buildroot}/%{_javadir}/%{name}

# Icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/
tar xf %{SOURCE1} -C %{buildroot}%{_datadir}/icons/hicolor/

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
%doc docs/*
/usr/bin/tablet
#/usr/bin/maqtoace
/usr/share/java/tablet/*
/usr/share/java/tablet/.install4j/*
/usr/share/applications/tablet.desktop
/usr/share/icons/hicolor/*

%changelog
* Mon Dec 16 2013 Shane Sturrock <shane@biomatters.com> - 1.13.12.13-1
- New upstream release

* Thu Aug 01 2013 Shane Sturrock <shane@biomatters.com> - 1.13.07.31-1
- New upstream release

* Mon May 20 2013 Simon Buxton <simon@biomatters.com> - 1.13.05.17-1
- New upstream release

* Fri May 03 2013 Shane Sturrock <shane@biomatters.com> - 1.13.05.02-1
- New upstream release

* Tue Apr 23 2013 Shane Sturrock <shane@biomatters.com> - 1.13.04.22-1
- New upstream release

* Thu Feb 07 2013 Carl Jones <carl@biomatters.com> - 1.12.12.05-4
- Fix .desktop file 

* Thu Jan 24 2013 Carl Jones <carl@biomatters.com> - 1.12.12.05-3
- Fix desktop icons path

* Thu Jan 24 2013 Carl Jones <carl@biomatters.com> - 1.12.12.05-2
- Add desktop icons

* Thu Dec 06 2012 Carl Jones <carl@biomatters.com> - 1.12.12.05-1
- New upstream release
* Thu Sep 05 2012 Carl Jones <carl@biomatters.com> - 1.12.08.29-1
- Add Requries: java-1.7.0

* Thu Sep 05 2012 Carl Jones <carl@biomatters.com> - 1.12.08.29-1
- New upstream release

* Fri Aug 03 2012 Carl Jones <carl@biomatters.com> - 1.12.03.26-3
- Add app_home patch for /usr/bin/tablet and /usr/bin/maqtoace

* Fri Aug 03 2012 Carl Jones <carl@biomatters.com> - 1.12.03.26-2
- Fix Java paths.

* Fri Aug 03 2012 Carl Jones <carl@biomatters.com> - 1.12.03.26-1
- Initial build.
