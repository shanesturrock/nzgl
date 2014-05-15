Name:		bismark
Version:	0.12.2
Release:	1%{?dist}
Summary:	A tool to map bisulfite converted sequence reads and determine cytosine methylation states.
Group:		Applications/Engineering
License:	GNU GPL v3
URL:		http://www.bioinformatics.babraham.ac.uk/projects/bismark/
Source0:	http://www.bioinformatics.babraham.ac.uk/projects/bismark/bismark_v%{version}.tar.gz
Requires:	bowtie
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

Bismark is a program to map bisulfite treated sequencing reads to a genome of
interest and perform methylation calls in a single step. The output can be
easily imported into a genome viewer, such as SeqMonk, and enables a researcher
to analyse the methylation levels of their samples straight away.

%prep
%setup -q -n %{name}_v%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 bismark %{buildroot}/%{_bindir}
install -m 0755 bismark_genome_preparation %{buildroot}/%{_bindir}
install -m 0755 bismark_methylation_extractor %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Bismark_User_Guide.pdf license.txt RELEASE_NOTES.txt
%{_bindir}/bismark
%{_bindir}/bismark_genome_preparation
%{_bindir}/bismark_methylation_extractor

%changelog
* Thu May 15 2014 Shane Sturrock <shane@biomatters.com> - 0.12.2-1
- Bismark: Added support for the new 64-bit index files for very large
  genomes in Bowtie 2 mode. The large genome indexes (ending in .bt2l
  instead of .bt2 for small genomes) are generated automatically by
  bismark_genome_preparation and work just as well in the Bismark
  alignment step
- Bismark: Fixed a bug that would omit the name of the second last
  chromomome from the SAM header if the genome had been supplied as
  Multi-FastA file. Everything else, including the alignments, would
  have been unaffected by this glitch
- Bismark: When the option '--basename' is specified, SE amibiguous file
  names now feature an underscore in their file name. Also, the pie
  chart file names are now derived from the the basename
- Methylation Extractor: Introduced a length check when the options
  --ignore or --ignore_r2 were set to ensure that only reads that are
  long enough are being processed

* Wed Apr 30 2014 Shane Sturrock <shane@biomatters.com> - 0.12.1-1
- Bismark: Added calculation of MAPQ values for SAM/BAM output generated
  with Bowtie 2 for both single-end and paired-end mode. The calculation
  is implemented like in Bowtie 2 itself. Mapping quality values are
  still unavailable for alignments performed with Bowtie and retain a
  value of 255 throughout 
- Bismark: Fixed an uninitialised value warning for PE alignments with
  Bowtie 2 that occurred whenever Read 2 aligned to the very start of a
  chromosome (this only affected the warning itself and had no impact on
  any results) 
- coverage2cytosine: all chromosomes or scaffolds are now processed
  irrespective of whether they were covered in the sequencing experiment
  or not. Previously, CpG/cytosine reports for genomes with lots of
  small scaffolds that were not covered by any reads might have had a
  variable number of lines between experiments

* Wed Apr 09 2014 Shane Sturrock <shane@biomatters.com> - 0.11.1-1
- The option --pbat now also works for use with Bowtie 2, in both
  single-end and paired-end mode. The only limitation to that is that it
  only works with FastQ files and uncompressed temporary files.
- Changed the order the @SQ lines are written out to the SAM/BAM header
  from random to the same order they are being read in from the genomes
  folder (or the order of the files in which they occur within a
  multi-FastA file).
- Included a new option -B/--basename <basename> for output files
  instead of deriving these names from the input file. --basename takes
  precedence over the option --prefix.
- Unmapped or ambiguous files now end in .fq or.fa for FastA or FastQ
  files, respectively (instead of .txt files).
- Methylation extractor
  - The methylation extractor willl no longer attempt to delete unused
    files if --mbias_only was speficied.
  - Added a test to see if a file that does not end in .bam is in fact a
    BAM file, and if this succeeds open the file using Samtools view.

* Thu Nov 28 2013 Shane Sturrock <shane@biomatters.com> - 0.10.1-1
- Bismark methylation extractor: The methylation extractor does now detect 
  automatically whether Bismark alignment file(s) were run in single-end or 
  paired-end mode. The automatic detection can be overridden by manually 
  specifying -s or -p and this option is only available for SAM/BAM files
- bismark2bedGraph: When run in stand-alone mode, the coverage file will 
  replace 'bedGraph' as the file ending with 'bismark.cov'. If the output 
  filename is anything other than 'bedGraph', '.bismark.cov' will be appended 
  to the filename
- bismark2bedGraph: When run in stand-alone mode, '--counts' will be enabled 
  by default for the coverage output
- bismark2bedGraph: Added a new option '--scaffolds/--gazillion' for users 
  working with unfinished genomes sporting tens or even hundreds of thousands 
  of scaffolds/contigs/chromosomes. Such a large number of reference sequences 
  frequently resulted in errors with pre-sorting reads to individual chromosome
  files because of the operating system's limitation of the number of 
  filehandles that can be written to at any one time (typically this limit is 
  anything between 128 and 1024 filehandles; to find out this limit on Linux, 
  type: ulimit -a). To bypass the limitation of open filehandles, the option 
  '--scaffolds' does not pre-sort methylation calls into individual chromosome 
  files. Instead, all input files are temporarily merged into a single file 
  (unless there is only a single file), and this file will then be sorted by 
  both chromosome AND position using the UNIX sort command. Please be aware 
  that this option might take a looooong time to complete, depending on the 
  size of the input files, and the memory you allocate to this process (see 
  '--buffer_size')
- bismark2bedGraph: Added a new option '--ample_memory'. Using this option will 
  not sort chromosomal positions using the UNIX sort command, but will instead 
  use two arrays to sort methylated and unmethylated calls, respectively. This 
  may result in a faster sorting process for very large files, but this comes 
  at the cost of a larger memory footprint (as an estimate, two arrays of the 
  length of the largest human chromosome 1 (~250 million bp) consume around 
  16GB of RAM). Note however that due to the overhead of creating and looping 
  through huge arrays this option might in fact be *slower* for small-ish files 
  (up to a few million alignments). Note also that this option is not currently 
  compatible with options '--scaffolds/--gazillion'. This option still needs 
  some efficiency testing as to when it actually makes sense to use it, but it 
  produces identical results to the default sort option. Thanks to Yi-Shiou 
  Chen for contributing this twist
- deduplicate_bismark: The deduplication script does now detect automatically 
  whether a Bismark alignment file was run in single-end or paired-end mode 
  (this happens separately for every file analysed). The automatic detection 
  can be overridden by manually specifying -s or -p and this option is only 
  available for SAM/BAM files
- bismark2report: Specifying a single file for each of the optional reports 
  does now will now work as intended, instead of being skipped
- coverage2cytosine: Added some counting and statements to indicate when the 
  run finished successfully (it proved to be difficult to follow the report 
  process for a genome with nearly half a million scaffolds...)
* Thu Oct 17 2013 Shane Sturrock <shane@biomatters.com> - 0.10.0-1
- Bismark - The option --prefix <some.prefix> does now also work for the C->T and G->A 
  transcribed temporary files to allow multiple instances of Bismark to be run on the same 
  file in the same folder (e.g. using Bowtie and Bowtie 2 or some stricter and laxer 
  parameters concurrently).
- Bismark Genome Preparation - Made a couple of changes to make the genome preparation fully 
  non-interactive. This means that the path to the genome folder and to Bowtie (1/2) have to 
  be specified up front (for Bowtie (1/2) it is otherwise assumed that it is in the PATH). 
  Furthermore, already existing bisulfite indices in the target folder will be overwritten 
  and the user is no longer prompted if he agrees to this. We got rid of this because 
  creating a second index (Bowtie 1 as well as 2) in the same folder in non-interactive 
  mode got stuck in loops asking whether it is alright to proceed or not, generating 
  therabyte sized log files without ever starting doing anything useful...).
- Methylation extractor - The methylation extractor will now delete unused methylation 
  context files (e.g. CTOT and CTOB files for a directional library). I finally got round to 
  implementing this after having to delete manually thousands of files containing the header 
  line only...
- bismark2bedGraph - Dropped the option -k3,3 from the sort command to result in a dramatic 
  speed increase while sorting. This option had been used previously to enable sorting by 
  chromosome in addition to position, but should no longer be needed because the files are 
  being read in sorted by chromosome already.  This module does now produces these two 
  output files: 
    (1) A bedGraph file, which now contains a header line: 'track type=bedGraph' The 
        genomic start coords are 0-based, the end coords are 1-based.
    (2) A coverage file ending in .cov. This file replaces the former 'bedGraph --counts' 
        file and is required to proceed with the subsequent step to generate a genome-wide 
        cytosine report (the module doing this has been renamed to coverage2cytosine to 
        reflect this file name change. 
- coverage2cytosine - Changed the name of this module from 'bedGraph2cytosine' to 
  'coverage2cytosine' to reflect the change that this module now requires the methylation 
  coverage file produced by the bismark2bedGraph module, ending in .cov (this coverage file 
  replaces the former "bedGraph --counts" output). Previously, the cytosine report would 
  always report every C position in any context, even though the default should have 
  reported CpG positions only. This has now been fixed.
- bismark2report - Changed the behavior of this module to automatically find all Bismark 
  mapping reports in the current working directory, and to try and work out whether the 
  optional reports are present as well (i.e. deduplication, splitting and M-bias reports). 
  This uses the file basename and will fail if the files have been renamed at any stage. 
  Specifying file names using the individual options takes precedence over the automatic 
  detection.
- deduplicate_bismark - Renamed the rather long deduplication script to this slightly 
  shorter one. Also added some filehandle closing statements that might have caused 
  buffering issues under certain circumstances.

* Mon Aug 26 2013 Shane Sturrock <shane@biomatters.com> - 0.9.0-2
- Peter Stockwell confirms this works for him so putting into stable repo

* Mon Aug 19 2013 Shane Sturrock <shane@biomatters.com> - 0.9.0-1
- New upstream release - release notes don't say why, put into testing repo

* Mon Jul 29 2013 Shane Sturrock <shane@biomatters.com> - 0.8.3-1
- New upstream release

* Fri Jul 26 2013 Shane Sturrock <shane@biomatters.com> - 0.8.2-1
- New upstream release

* Wed Jul 17 2013 Shane Sturrock <shane@biomatters.com> - 0.8.1-1
- New upstream release

* Mon Jul 15 2013 Shane Sturrock <shane@biomatters.com> - 0.8.0-1
- New upstream release

* Mon Mar 18 2013 Shane Sturrock <shane@biomatters.com> - 0.7.9-1
- New upstream release

* Mon Mar 4 2013 Shane Sturrock <shane@biomatters.com> - 0.7.8-1
- New upstream release

* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 0.7.7-1
- New upstream release

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.7.6-1
- New upstream release

* Wed Jul 24 2012 Carl Jones <carl@biomatters.com> - 0.7.5-1
- Initial build.
