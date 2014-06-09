Name:		rsem
Version:	1.2.14
Release:	1%{?dist}
Summary:	Package for estimating gene and isoform expression levels from RNA-Seq data.
Group:		Applications/Engineering
License:	GPL
URL:		http://pages.cs.wisc.edu/~bli
Source0:	rsem-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
Requires:	samtools

%description
RSEM is a software package for estimating gene and isoform expression
levels from RNA-Seq data. The RSEM package provides an user-friendly
interface, supports threads for parallel computation of the EM
algorithm, single-end and paired-end read data, quality scores,
variable-length reads and RSPD estimation. In addition, it provides
posterior mean and 95% credibility interval estimates for expression
levels. For visualization, It can generate BAM and Wiggle files in
both transcript-coordinate and genomic-coordinate. Genomic-coordinate
files can be visualized by both UCSC Genome browser and Broad
Institute's Integrative Genomics Viewer (IGV). Transcript-coordinate
files can be visualized by IGV. RSEM also has its own scripts to
generate transcript read depth plots in pdf format. The unique feature
of RSEM is, the read depth plots can be stacked, with read depth
contributed to unique reads shown in black and contributed to
multi-reads shown in red. In addition, models learned from data can
also be visualized. Last but not least, RSEM contains a simulator.

%prep
%setup -q

%build
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 convert-sam-for-rsem %{buildroot}%{_bindir}
install -m 0755 extract-transcript-to-gene-map-from-trinity %{buildroot}%{_bindir} 
install -m 0755 rsem-calculate-expression %{buildroot}%{_bindir}
install -m 0755 rsem-control-fdr %{buildroot}%{_bindir}
install -m 0755 rsem-extract-reference-transcripts %{buildroot}%{_bindir}
install -m 0755 rsem-generate-data-matrix %{buildroot}%{_bindir}
install -m 0755 rsem-generate-ngvector %{buildroot}%{_bindir}
install -m 0755 rsem-gen-transcript-plots %{buildroot}%{_bindir}
install -m 0755 rsem-plot-model %{buildroot}%{_bindir}
install -m 0755 rsem-plot-transcript-wiggles %{buildroot}%{_bindir}
install -m 0755 rsem-prepare-reference %{buildroot}%{_bindir}
install -m 0755 rsem-preref %{buildroot}%{_bindir}
install -m 0755 rsem-run-ebseq %{buildroot}%{_bindir}
install -m 0755 rsem-synthesis-reference-transcripts %{buildroot}%{_bindir}
install -m 0755 rsem-extract-reference-transcripts %{buildroot}%{_bindir}
install -m 0755 rsem-synthesis-reference-transcripts %{buildroot}%{_bindir}
install -m 0755 rsem-preref %{buildroot}%{_bindir}
install -m 0755 rsem-parse-alignments %{buildroot}%{_bindir}
install -m 0755 rsem-build-read-index %{buildroot}%{_bindir}
install -m 0755 rsem-run-em %{buildroot}%{_bindir}
install -m 0755 rsem-tbam2gbam %{buildroot}%{_bindir}
install -m 0755 rsem-run-gibbs %{buildroot}%{_bindir}
install -m 0755 rsem-calculate-credibility-intervals %{buildroot}%{_bindir}
install -m 0755 rsem-simulate-reads %{buildroot}%{_bindir}
install -m 0755 rsem-bam2wig %{buildroot}%{_bindir}
install -m 0755 rsem-get-unique %{buildroot}%{_bindir}
install -m 0755 rsem-bam2readdepth %{buildroot}%{_bindir}
install -m 0755 rsem-sam-validator %{buildroot}%{_bindir}
install -m 0755 rsem-scan-for-paired-end-reads %{buildroot}%{_bindir}
install -m 0644 rsem_perl_utils.pm %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}

%changelog
* Tue Jun 10 2014 Shane Sturrock <shane@biomatters.com> - 1.2.14-1
- Changed RSEM's behaviors for building Bowtie/Bowtie 2 indices. In
  'rsem-prepare-reference', '--no-bowtie' and '--no-ntog' options are
  removed. By default, RSEM does not build either Bowtie or Bowtie 2
  indices. Instead, it generates two index Multi-FASTA files,
  'reference_name.idx.fa' and 'reference_name.n2g.idx.fa'. Compared to
  the former file, the latter one in addition converts all 'N's into
  'G's. These two files can be used to build aligner indices for
  customized aligners. In addition, 'reference_name.transcripts.fa' does
  not have poly(A) tails added. To enable RSEM build Bowtie/Bowtie 2
  indices, '--bowtie' or '--bowtie2' must be set explicitly. The most
  significant benefit of this change is that now we can build Bowtie and
  Bowtie 2 indices simultaneously by turning both '--bowtie' and
  '--bowtie2' on. Type 'rsem-prepare-reference --help' for more
  information 
- If transcript coordinate files are visualized using IGV,
  'reference_name.idx.fa' should be imported as a genome (instead of
  'reference_name.transcripts.fa'). For more information, see the third
  subsection of Visualization in 'README.md' - Modified RSEM perl
  scripts so that RSEM directory will be added in the beginning of the
  PATH variable. This also means RSEM will try to use its own samtools
  first
- Added --seed option to set random number generator seeds in
  'rsem-calculate-expression'  
- Added posterior standard deviation of counts as output if either
  '--calc-pme' or '--calc-ci' is set
- Updated boost to v1.55.0
- Renamed makefile as Makefile
- If '--output-genome-bam' is set, in the genome BAM file, each
  alignment's 'MD' field will be adjusted to match the CIGAR string
- 'XS:A:value' field is required by Cufflinks for spliced alignments.
  If '--output-genome-bam' is set, in the genome BAM file, first each
  alignment's 'XS' filed will be deleted. Then if the alignment is an
  spliced alignment, a 'XS:A:value' field will be added accordingly
- Added instructions for users who want to put all RSEM executables
  into a bin directory (see Compilation & Installation section of
  'README.md')

* Wed May 28 2014 Shane Sturrock <shane@biomatters.com> - 1.2.13-1
- Allowed users to use the SAMtools in the PATH first and enabled RSEM to find 
  its executables via a symbolic link. 
- Changed the behavior of parsing GTF file. Now if a GTF line's feature is 
  not "exon" and it does not contain a "gene_id" or "transcript_id" attribute, 
  only a warning message will be produced (instead of failing the RSEM).

* Mon Mar 31 2014 Shane Sturrock <shane@biomatters.com> - 1.2.12-1
- Enabled allele-specific expression estimation. 
- Added '--calc-pme' option for 'rsem-calculate-expression' to calculate 
  posterior mean estimates only (no credibility intervals). 
- Modified the shebang line of RSEM perl scripts to make them more portable. 
- Added '--seed' option for 'rsem-simulate-reads' to enable users set the seed 
  of random number generator used by the simulation. 
- Modified the transcript extraction behavior of 'rsem-prepare-reference'. For 
  transcripts that cannot be extracted, instead of failing the whole script, 
  warning information is produced. Those transcripts are ignored.

* Mon Feb 17 2014 Shane Sturrock <shane@biomatters.com> - 1.2.11-1
- Enabled RSEM to use Bowtie 2 aligner (indel, local and discordant alignments 
  are not supported yet)
- Changed option names '--bowtie-phred33-quals', '--bowtie-phred64-quals' and 
  '--bowtie-solexa-quals' back to '--phred33-quals', '--phred64-quals' and 
  '--solexa-quals' 
* Mon Feb 03 2014 Shane Sturrock <shane@biomatters.com> - 1.2.10-1
- Fixed a bug which will lead to out-of-memory error when RSEM computes ngvector for EBSeq.
* Mon Jan 13 2014 Shane Sturrock <shane@biomatters.com> - 1.2.9-1
- Fixed a compilation error problem in Mac OS. 
- Fixed a problem in makefile that affects 'make ebseq'. 
- Added 'model_file_description.txt', which describes the format and meanings 
  of file 'sample_name.stat/sample_name.model'. 
- Updated samtools to version 0.1.19.
* Mon Nov 25 2013 Shane Sturrock <shane@biomatters.com> - 1.2.8-1
- Provided a more detailed description for how to simulate RNA-Seq data using 'rsem-simulate-reads'. 
- Provided more user-friendly error message if RSEM fails to extract transcript sequences due to 
  the failure of reading certain chromosome sequences.
* Wed Oct 02 2013 Shane Sturrock <shane@biomatters.com> - 1.2.7-1
- Initial build.
