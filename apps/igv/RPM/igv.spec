Name:		igv
Version:	2.1.29
Release:	1%{?dist}
Summary:	Integrative Genomics Viewer
Group:		Applications/Engineering
License:	LGPL
URL:		http://www.broadinstitute.org/igv/home
Source0:	http://www.broadinstitute.org/igv/projects/downloads/IGVDistribution_%{version}.zip
Source1:	igv
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/igv
/usr/share/java/igv/lib/*.jar
/usr/share/java/igv/igv.jar

%changelog
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
