Summary:	Sequence assembler for very short reads
Name:		velvet
Version:	1.2.09
Release:	1%{?dist}
License:	GPLv3
Group:		Applications/Engineering
URL:		http://www.ebi.ac.uk/~zerbino/velvet/ 
Source:		http://www.ebi.ac.uk/~zerbino/velvet/velvet_%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	zlib-devel
AutoReqProv:	no

%description
Velvet is a de novo genomic assembler specially designed for short read
sequencing technologies, such as Solexa or 454, developed by Daniel Zerbino and
Ewan Birney at the European Bioinformatics Institute (EMBL-EBI), near
Cambridge, in the United Kingdom.

Velvet currently takes in short read sequences, removes errors then produces
high quality unique contigs. It then uses paired-end read and long read
information, when available, to retrieve the repeated areas between contigs. 

This package builds the sequencespace and colorspace versions of Velvet.

%prep
%setup -q -n %{name}-%{version}

%build
make
make color
# Fix perl shebangs
find . -type f -name '*.pl' | xargs sed 's=/usr/local/bin/perl=/usr/bin/perl=g' --in-place

%install
%{__rm} -rf %{buildroot}
%{__install} -m 0755 -d %{buildroot}%{_bindir}
%{__install} -m 0755 velvetg %{buildroot}%{_bindir}
%{__install} -m 0755 velveth %{buildroot}%{_bindir}
%{__install} -m 0755 velvetg_de %{buildroot}%{_bindir}
%{__install} -m 0755 velveth_de %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS.txt ChangeLog LICENSE.txt README.txt contrib/ *.pdf
%{_bindir}/*

%changelog
* Tue May 07 2013 Shane Sturrock <shane@biomatters.com> - 1.2.09-1
- New upstream release.
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 1.2.08-1
- New upstream release.
* Wed Aug 01 2012 Carl Jones <carl@biomatters.com> - 1.2.07-2
- Fix perl shebangs
- Ignore perl::Bio deps for contrib/ scripts

* Wed Aug 01 2012 Carl Jones <carl@biomatters.com> - 1.2.07-1
- Initial package.
