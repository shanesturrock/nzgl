%define debug_package %{nil}

Name:		STAR
Version:	2.5.2b
Release:	1%{?dist}
Summary:	Tool for handing RNA-seq alignment
Group:		Applications/Engineering
License:	GPL
URL:		https://code.google.com/p/rna-star/
SOURCE:		STAR-2.5.2b.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
STAR aligns RNA-seq reads to a reference genome using uncompressed suffix 
arrays.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 bin/Linux_x86_64_static/STAR %{buildroot}%{_bindir}
install -m 0755 bin/Linux_x86_64_static/STARlong %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
/usr/bin/STAR
/usr/bin/STARlong

%changelog
* Fri Sep 30 2016 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 2.5.2b-1
- Fixed a problem with --outSAMmultNmax 1 not working for transcriptomic
  output.
- Fixed a bug with chimeric BAM output for --chimOutType WithinBAM option.
- Fixed a bug that could cause non-stable BAM sorting if the gcc qsort is
  unstable.
- Fixed a bug with causing seg-faults when combining --twopassMode Basic
  --outSAMorder PairedKeepInputOrder .
- Fixed a problem with SAM header in cases where reference sequences are added
  at the mapping stage.

* Tue Feb 17 2015 Shane Sturrock <shane@biomatters.com> - 2.3.0e-2
- CentOS 7 compatibility

* Thu Apr 10 2014 Shane Sturrock <shane@biomatters.com> - 2.3.0e-1
- STAR can use annotations in the form of GTF and GFF3 files with 
  --sjdbGTFfile /path/to/annotation/file
  GFF3 requires --sjdbGTFtagExonParentTranscript Parent
- Input files can be processed (e.g. uncompressed) with 
  --readFilesCommand /UncompressCommand/. For example,
  --readFilesIn Read1.gz Read2.gz --readFilesCommand zcat will take gzipped 
  files and uncompress them on the fly.
- Multiple input files can be specified separated by comma:
  --readFilesIn A.read1,B.read1,C.read1 A.read2,B.read2,C.read2
- Output alignments (Aligned.out.sam) can be filterted by the same 
  criteria (outSJfilter* options) as the junctions in the SJ.out.tab file 
  using --outFilterType BySJout. This is useful to remove from 
  Aligned.out.sam spurious alignments with junctions supported by too few 
  reads, junctions with large gaps or non-canonical junctions.
- --outSJfilterIntronMaxVsReadN Gmax1 Gmax2 Gmax3 ...  specifies max allowed 
  gap for junctions supported by 1,2,3... reads (for SJ.out.tab) file. This 
  is useful to remove large gap junctions supported by too few reads.
- Multi-mapping read counts per junction are output into column 8 of 
  SJ.out.tab
- Unmapped reads can be output into separate .fastq (.fasta) files with
  --outReadsUnmapped Fastx.
- Quality scores in the SAM output can be transformed with 
  --outQSconversionAdd. For example, --outQSconversionAdd -31 will transform 
  Sanger+64 into Sanger+33 representation.
- The default shared memory option is changed to --genomeLoad NoSharedMemory.
  This is a safer and more compatible mode. If you want to revert to 
  previous version default, please use --genomeLoad LoadAndKeep
- SAM output is compatible with Picard tools.
