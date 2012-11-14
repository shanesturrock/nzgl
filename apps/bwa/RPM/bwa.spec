Name:           bwa
Version:        0.6.2
Release:        1%{?dist}
Summary:        Burrows-Wheeler Alignment tool

Group:          Applications/Engineering
License:        GPLv3
URL:            http://bio-bwa.sourceforge.net/
Source0:        http://downloads.sourceforge.net/bio-%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  zlib-devel

%description

BWA is a program for aligning sequencing reads against a large
reference genome (e.g. human genome). It has two major components, one
for read shorter than 150bp and the other for longer reads.

%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1

install -m 0755 bwa %{buildroot}/%{_bindir}
install -m 0755 solid2fastq.pl %{buildroot}/%{_bindir}
install -m 0755 qualfa2fq.pl %{buildroot}/%{_bindir}

install -m 0644 bwa.1 %{buildroot}/%{_mandir}/man1/bwa.1

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING NEWS 
%{_mandir}/man1/%{name}.1*
%{_bindir}/bwa
%{_bindir}/qualfa2fq.pl
%{_bindir}/solid2fastq.pl


%changelog
* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.6.2-1
- New upstream release

* Thu Feb 17 2011 Adam Huffman <bloch@verdurin.com> - 0.5.9-1
- new upstream release 0.5.9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Adam Huffman <bloch@verdurin.com> - 0.5.8c-1
- upstream bugfix release

* Tue Jul 20 2010 Adam Huffman <bloch@verdurin.com> - 0.5.8a-1
- new upstream release

* Sat May 29 2010 Adam Huffman <bloch@verdurin.com> - 0.5.7-2
- fix source URL
- install manpage
- fix cflags

* Fri May 28 2010 Adam Huffman <bloch@verdurin.com> - 0.5.7-1
- initial version

