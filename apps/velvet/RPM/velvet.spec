Summary:	Sequence assembler for very short reads
Name:		velvet
Version:	1.2.10
Release:	4%{?dist}
License:	GPLv3
Group:		Applications/Engineering
URL:		http://www.ebi.ac.uk/~zerbino/velvet/ 
Source:		http://www.ebi.ac.uk/~zerbino/velvet/velvet_%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	zlib-devel libgomp
AutoReqProv:	no
Patch0:		Makefile.patch

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
%setup -q -n %{name}_%{version}
%patch0 -p0

%build
make 'OPENMP=8'
make 'OPENMP=8' color
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
* Tue Apr 08 2014 Shane Sturrock <shane@biomatters.com> - 1.2.10-4
- Increase CATEGORIES to 4 and OPENMP to 8
* Tue Aug 06 2013 Shane Sturrock <shane@biomatters.com> - 1.2.10-3
- Bump up MAXKMERLENGTH to 255 for MiSeq users
* Fri Aug 02 2013 Shane Sturrock <shane@biomatters.com> - 1.2.10-2
- Recompile with openMP support
* Tue Jun 11 2013 Simon Buxton <simon@biomatters.com> - 1.2.10-1
- New upstream release.
* Tue May 07 2013 Shane Sturrock <shane@biomatters.com> - 1.2.09-1
- New upstream release.
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 1.2.08-1
- New upstream release.
* Wed Aug 01 2012 Carl Jones <carl@biomatters.com> - 1.2.07-2
- Fix perl shebangs
- Ignore perl::Bio deps for contrib/ scripts

* Wed Aug 01 2012 Carl Jones <carl@biomatters.com> - 1.2.07-1
- Initial package.
