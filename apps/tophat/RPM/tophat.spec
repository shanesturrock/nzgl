%define samtools_version 0.1.18

Name:		tophat
Version:	2.0.8
Release:	0%{?dist}
Summary:	A spliced read mapper for RNA-Seq
Group:		Applications/Engineering
License:	Artistic 2.0
URL:		http://tophat.cbcb.umd.edu/
Source0:	http://tophat.cbcb.umd.edu/downloads/tophat-%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/samtools/samtools-%{samtools_version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	boost >= 1.47
BuildRequires:	boost-devel >= 1.47
BuildRequires:	boost-thread >= 1.47
BuildRequires:	boost-jam >= 1.47
BuildRequires:	boost-math >= 1.47
BuildRequires:	boost-random >= 1.47
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
Requires:	bowtie2

%description

TopHat is a fast splice junction mapper for RNA-Seq reads. It aligns
RNA-Seq reads to mammalian-sized genomes using the ultra
high-throughput short read aligner Bowtie, and then analyzes the
mapping results to identify splice junctions between exons.

TopHat is a collaborative effort between the University of Maryland
Center for Bioinformatics and Computational Biology and the University
of California, Berkeley Departments of Mathematics and Molecular and
Cell Biology.

%prep
%setup -q -a 1

%build
cd samtools-%{samtools_version}
make %{_smp_mflags}
mkdir -p %{_tmppath}/bamlib/include/bam
mkdir -p %{_tmppath}/bamlib/lib
/bin/cp *.h %{_tmppath}/bamlib/include/bam
/bin/cp *.a %{_tmppath}/bamlib/lib
cd ..
LDFLAGS='-lboost_thread-mt' ./configure --prefix=/usr --with-bam=%{_tmppath}/bamlib
# Do not build if smp_mflags used
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/bam2fastx %{buildroot}%{_bindir}
install -m 0755 src/bam_merge %{buildroot}%{_bindir}
install -m 0755 src/bed_to_juncs %{buildroot}%{_bindir}
#install -m 0755 src/closure_juncs %{buildroot}%{_bindir}
install -m 0755 src/contig_to_chr_coords %{buildroot}%{_bindir}
install -m 0755 src/fix_map_ordering %{buildroot}%{_bindir}
install -m 0755 src/gtf_juncs %{buildroot}%{_bindir}
install -m 0755 src/gtf_to_fasta %{buildroot}%{_bindir}
install -m 0755 src/juncs_db %{buildroot}%{_bindir}
install -m 0755 src/long_spanning_reads %{buildroot}%{_bindir}
install -m 0755 src/map2gtf %{buildroot}%{_bindir}
install -m 0755 src/prep_reads %{buildroot}%{_bindir}
install -m 0755 src/sam_juncs %{buildroot}%{_bindir}
install -m 0755 src/segment_juncs %{buildroot}%{_bindir}
install -m 0755 src/sra_to_solid %{buildroot}%{_bindir}
install -m 0755 src/tophat %{buildroot}%{_bindir}
install -m 0755 src/tophat2 %{buildroot}%{_bindir}
install -m 0755 src/tophat-fusion-post %{buildroot}%{_bindir}
install -m 0755 src/tophat_reports %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING AUTHORS LICENSE THANKS
%{_bindir}/*

%changelog
* Mon Feb 25 2013 Carl Jones <carl@biomatters.com> - 2.0.8-0
- New upstream release

* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 2.0.7-1
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 2.0.6-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 2.0.5-1
- New upstream release
* Fri Aug 09 2012 Carl Jones <carl@biomatters.com> - 2.0.4-3
- Fix license details
- Fix Requires 
* Fri Aug 09 2012 Carl Jones <carl@biomatters.com> - 2.0.4-2
- Fix compilation issues
* Fri Aug 03 2012 Carl Jones <carl@biomatters.com> - 2.0.4-1
- New upstream release
* Thu Aug 11 2011 Adam Huffman <bloch@verdurin.com> - 1.3.1-1
- initial version
