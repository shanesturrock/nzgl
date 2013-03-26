Name:		picard
Version:	1.88
Release:	1%{?dist}
Summary:	Java utilities to manipulate SAM files

Group:		Applications/Engineering
License:	MIT
URL:		http://picard.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}-tools-%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

Requires:	java >= 1:1.6.0
Requires:	jpackage-utils

%define __jar_repack 0

%description

Picard comprises Java-based command-line utilities that manipulate SAM
files, and a Java API (SAM-JDK) for creating new programs that read
and write SAM files. Both SAM text format and SAM binary (BAM) format
are supported.

%prep
%setup -q -n %{name}-tools-%{version}

mv ../snappy-java-1.0.3-rc3.jar .

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_javadir}/%{name}

cp *.jar %{buildroot}%{_javadir}/%{name}

cp snappy-java-1.0.3-rc3.jar %{buildroot}%{_javadir}/%{name}

mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)

%{_javadir}/%{name}/*

%changelog
* Wed Mar 27 2013 Shane Sturrock <shane@biomatters.com> - 1.88-1
- New upstream release

* Mon Mar 18 2013 Shane Sturrock <shane@biomatters.com> - 1.87-1
- New upstream release

* Mon Mar 04 2013 Shane Sturrock <shane@biomatters.com> - 1.86-1
- New upstream release

* Mon Feb 11 2013 Carl Jones <carl@biomatters.com> - 1.85-1
- New upstream release

* Wed Jan 15 2013 Carl Jones <carl@biomatters.com> - 1.84-1
- New upstream release

* Tue Jan 08 2013 Carl Jones <carl@biomatters.com> - 1.83-1
- New upstream release

* Thu Dec 20 2012 Carl Jones <carl@biomatters.com> - 1.82-1
- New upstream release

* Wed Dec 05 2012 Carl Jones <carl@biomatters.com> - 1.81-1
- New upstream release
* Thu Nov 22 2012 Carl Jones <carl@biomatters.com> - 1.80-1
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 1.79-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 1.77-1
- New upstream release

* Wed Aug 01 2012 Carl Jones <carl@biomatters.com> - 1.74-1
- Rename package to picard
- Bump to 1.74

* Tue Aug 23 2011 Adam Huffman <bloch@verdurin.com> - 1.50-2
- change to picard-tools-bin

* Thu Aug 11 2011 Adam Huffman <bloch@verdurin.com> - 1.50-1
- initial version

