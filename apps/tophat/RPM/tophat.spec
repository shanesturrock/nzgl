%define samtools_version 0.1.18

Name:		tophat
Version:	2.0.13
Release:	1%{?dist}
Summary:	A spliced read mapper for RNA-Seq
Group:		Applications/Engineering
License:	Artistic 2.0
URL:		http://tophat.cbcb.umd.edu/
Source0:	http://tophat.cbcb.umd.edu/downloads/tophat-%{version}.tar.gz
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
%setup -q

%build
LDFLAGS='-lboost_thread-mt' ./configure --prefix=/usr
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
install -m 0755 src/samtools_0.1.18 %{buildroot}%{_bindir}
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
* Fri Oct 03 2014 Shane Sturrock <shane@biomatters.com> - 2.0.13-1
- removed SAMtools as an external dependency in order to avoid incompatibility 
  issues with recent and future changes of SAMtools and its code library (an 
  older, stable SAMtools version is now packaged with TopHat)
- fixed a few code compatibility issues when compiling on OSX 10.9

* Fri Jul 04 2014 Sidney Markowitz <sidney@biomatters.com> - 2.0.12-1
- Fix from upstream to accommodate changed option in new version of bowtie2

* Wed Jun 11 2014 Sidney Markowitz <sidney@biomatters.com> - 2.0.11-2
- NZGL patch to accommodate changed option in new version of bowtie2

* Wed Mar 05 2014 Shane Sturrock <shane@biomatters.com> - 2.0.11-1
- Version 2.0.11 is a maintenance release with the following simple fix:
  This version is compatible with Bowtie2 v2.2.1, although it does not 
  support a 64-bit Bowtie2 index yet.

* Fri Nov 15 2013 Shane Sturrock <shane@biomatters.com> - 2.0.10-1
- Improved support for adding unpaired reads to PE reads in the same TopHat2 
  run (please see the manual entry for this usage). This includes reporting 
  separate counts for the additional unpaired reads and making sure that the 
  SAM flags in the output files reflect the paired or unpaired origin of the 
  reads.
- Added the possibility to run TopHat just for the purpose of preparing the 
  transcriptome index files (please see the manual entry for this special 
  usage).
- The input read files can have different file formats, as TopHat now 
  autodetects the FASTA/FASTQ format of each input file.
- Fixed a bug that could sometimes incorrectly rename the reads in the output 
  alignments.
- The stats in align_summary.txt now reflect the reported mappings under the 
  constraints of the provided Tophat options, instead of reflecting the 
  internally detected alignments. As such, the number of reads with multiple 
  mappings may appear to be incorrectly reported if the user provided options 
  that directly affect the reporting of such multiple mapppings.
- Fixed a bug that caused TopHat to fail when bowtie1 and pre-filtering options
  were used together.

* Fri Aug 30 2013 Shane Sturrock <shane@biomatters.com> - 2.0.10-1
- New upstream release - no changelog

* Mon Jul 01 2013 Shane Sturrock <shane@biomatters.com> - 2.0.9-1
- New upstream release

* Wed May 15 2013 Shane Sturrock <shane@biomatters.com> - 2.0.8b-1
- New upstream release fixing bowtie version check errors

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
