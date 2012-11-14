%define ver 1.1.2
%define rel 484

Summary:	fastq-processing utilities
Name:		ea-utils
Version:	%{ver}.%{rel}
Release:	1%{dist}
URL:		https://code.google.com/p/ea-utils/
Source:		http://ea-utils.googlecode.com/files/%{name}.%{ver}-%{rel}.tar.gz
License:	MIT
Group:		Applications/Engineering
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	bamtools
BuildRequires:	sparsehash-devel
BuildRequires:	zlib-devel

%description
Utilities for processing fastq files, stitching paired-end reads,
demultiplexing paired-end in-sync, adapter-trimming & skew removal.

%prep
%setup -q -n %{name}.%{ver}-%{rel}

%build
make PREFIX=%{buildroot}/%{_prefix}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 fastq-join %{buildroot}%{_bindir}/fastq-join
install -m 0755 fastq-clipper %{buildroot}%{_bindir}/fastq-clipper
install -m 0755 fastq-mcf %{buildroot}%{_bindir}/fastq-mcf
install -m 0755 fastq-multx %{buildroot}%{_bindir}/fastq-multx
install -m 0755 fastq-stats %{buildroot}%{_bindir}/fastq-stats
install -m 0755 sam-stats %{buildroot}%{_bindir}/sam-stats
install -m 0755 varcall %{buildroot}%{_bindir}/varcall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/fastq-join
%{_bindir}/fastq-clipper
%{_bindir}/fastq-mcf
%{_bindir}/fastq-multx
%{_bindir}/fastq-stats
%{_bindir}/sam-stats
%{_bindir}/varcall

%changelog
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 1.1.2.484-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 1.1.2.469-1
- New upstream release
* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 1.1.2.408-1
- New upstream release
- Build against new sparsehash-devel package
