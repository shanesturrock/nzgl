Name:		seqmonk
Version:	0.24.1
Release:	0%{?dist}
Summary:	A tool to visualise and analyse high throughput mapped sequence data
Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.bioinformatics.babraham.ac.uk/projects/seqmonk/
Source0:	http://www.bioinformatics.babraham.ac.uk/projects/seqmonk/seqmonk_v%{version}.zip
Source1:	seqmonk-icons.tar.gz
Source2:	seqmonk.desktop
Patch0:		seqmonk-classpath.patch
Requires:	java-1.6.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
SeqMonk is a program to enable the visualisation and analysis of mapped sequence data. It was written 
for use with mapped next generation sequence data but can in theory be used for any dataset which can 
be expressed as a series of genomic positions.

%prep
%setup -q -n SeqMonk
%patch0 -p0

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 seqmonk %{buildroot}/%{_bindir}
/bin/cp -r uk/ %{buildroot}/%{_javadir}/%{name}/
/bin/cp -r com/ %{buildroot}/%{_javadir}/%{name}/

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
%doc README.txt LICENSE.txt RELEASE_NOTES.txt
/usr/bin/seqmonk
/usr/share/java/seqmonk/*
/usr/share/applications/seqmonk.desktop
/usr/share/icons/hicolor/*

%changelog
* Mon Feb 25 2013 Carl Jones <carl@biomatters.com> - 0.24.1-0
- New upstream release

* Thu Jan 24 2013 Carl Jones <carl@biomatters.com> - 0.24-0
- New upstream release

* Thu Jan 24 2013 Carl Jones <carl@biomatters.com> - 0.23.1-2
- Add desktop icons, menu

* Wed Dec 12 2012 Carl Jones <carl@biomatters.com> - 0.23.1-1
- New upstream release
* Wed Dec 05 2012 Carl Jones <carl@biomatters.com> - 0.23.0-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 0.22.0-2
- Use 0.22 tarball rather than 0.21
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 0.22.0-1
- New upstream release
* Fri Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.21.0-3
- Fixed Java paths
* Fri Aug 02 2012 Carl Jones <carl@biomatters.com> - 0.21.0-2
- Move bin/seqmonk to seqmonk.
* Fri Aug 02 2012 Carl Jones <carl@biomatters.com> - 0.21.0-1
- Initial build.
