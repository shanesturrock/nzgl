Name:		bismark
Version:	0.16.3
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
install -m 0755 coverage2cytosine %{buildroot}/%{_bindir}
install -m 0755 bismark2report %{buildroot}/%{_bindir}
install -m 0644 bismark_sitrep.tpl %{buildroot}/%{_bindir}
install -m 0755 bismark_genome_preparation %{buildroot}/%{_bindir}
install -m 0755 deduplicate_bismark %{buildroot}/%{_bindir}
install -m 0755 bismark2summary %{buildroot}/%{_bindir}
install -m 0755 bismark2bedGraph %{buildroot}/%{_bindir}
install -m 0755 bam2nuc %{buildroot}/%{_bindir}
install -m 0755 bismark_methylation_extractor %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Bismark_alignment_modes.pdf Bismark_User_Guide.pdf license.txt RELEASE_NOTES.txt 
#%doc Bismark_User_Guide.pdf license.txt RELEASE_NOTES.txt RRBS_Guide.pdf

%{_bindir}/bam2nuc
%{_bindir}/bismark
%{_bindir}/bismark2bedGraph
%{_bindir}/bismark2report
%{_bindir}/bismark2summary
%{_bindir}/bismark_genome_preparation
%{_bindir}/bismark_methylation_extractor
%{_bindir}/bismark_sitrep.tpl
%{_bindir}/coverage2cytosine
%{_bindir}/deduplicate_bismark

%changelog
*Wed Jul 27 2016 Shane Sturrock <shane@biomatters.com> - 0.16.3-1
- Bismark: Essential fixes (2 in total) to address a bug for Bowtie 2
  alignments where reads that should be considered ambiguous were incorrectly
assigned to the first alignment thread. These errors had crept in during
releases 0.16.0 and 0.16.2). More info available on Github
- Bismark: Added support for large Bowtie (1) index files ending in .ebwtl
  which had been added in Bowtie v1.1.0
- Changed the Shebang in all scripts of the Bismark suite to #!/usr/bin/env
  perl instead of #!/usr/bin/perl
- deduplicate_bismark: Does now bail with a useful error message when the input
  files are empty
- bismark_genome_preparation: Added new option '--genomic_composition' so that
  the genomic composition can be calculated and written right at the genome
  preparation stage rather than by using bam2nuc
- bam2nuc: Now also calculates a fold coverage for the various
  (di-)nucleotides. The changes in the nucleotide_stats text file are also
  picked up and plotted by bismark2report
- bam2nuc: Added a new option '--genomic_composition_only' to just process the
  genomic sequence without requiring any data files
- bismark2summary: Added option -o/--basename FILENAME to specify a certain
  filename. If not specified the name will remain
  bismark_summary_report.txt/html
- bismark2summary: Added documentation and the options '--help' and '--version'
  to be consistent with the rest of Bismark
- bismark2summary: Added option '--title STRING' to give the HTML report a
  different title

*Tue Apr 29 2016 Shane Sturrock <shane@biomatters.com> - 0.16.1-1
- Bismark: Removed a rogue warn/sleep statement for PE/Bowtie2 mode that had
  crept in during the last release...

*Thu Apr 21 2016 Shane Sturrock <shane@biomatters.com> - 0.16.0-1
- Bismark: File endings .fastq | .fq | .fastq.gz | .fq.gz are now removed from
  the output file (unless they were specified with --basename) in a bid to
  reduce the length of the already long file names
- Bismark: Enabled the new option --dovetail (which will be turned on by
  default for --pbat libraries) which will now allow dovetailing reads to be
  reported
- Bismark: Changed the behaviour of corner cases where several non-directional
  alignments could have existed for the very same position but to different
  strands so that now the best alignment trumps the weaker one. As an example: 
  If you relaxed the alignment criteria of a given alignment to allow ~60 
  mismatches for PE alignment we did find an alignment to the OT strand with a 
  combined AS of -324, but there also was an alignment to the CTOB strand with 
  and AS of 0 (perfect alignment). The CTOB now trumps the OT alignment, and 
  the methylation information information is now reported for the bottom strand
- New module: bismark2summary accepts Bismark BAM files as input. It will then
  try to identify Bismark reports, and optionally deduplication reports or
  methylation extractor (splitting) reports automatically based the BAM file
  basename. It produces a tab delimited overview table (.txt) as well as a
  graphical HTML report. Examples can be found at Bismark Summary Report and
  Bismark Summary Report (.txt)
- The new Bismark module bam2nuc calculcates the average mono- and
  di-nucleotide coverage of libraries and compares this to the genomic average
  composition. bam2nuc can be called straight from within Bismark (option
  --nucleotide_coverage) or run stand-alone. bam2nuc creates a
  ...nucleotide_stats.txt file that is also automatically detected by
  bismark2report and incorporated into the HTML report
- bismark_sitrep.tpl: Removed an extra function call in bismark_sitrep.tpl so
  that the M-bias 2 plot is drawn once the M-bias 1 plot has finished drawing
  (parallel processing could with certain browsers and data may have resulted in
  a white spaceholder only)
- Methylation extractor: Altering the file path handling of coverage2cytosine
  and bismark2bedGraph also required some changes in the methylation extractor
- bismark2bedGraph: Input file path handling has been completely reworked. The
  output file which can be specified as -o output.bedGraph now has to be a
  single file name and mustn't contain any path information. A particular output
  folder may be specified with -dir /any/path/
- bismark2bedGraph: Addressing the file path handling issue also fixed a
  similar issue with the option --remove_spaces when -o had been specified
- coverage2cytosine: Changed zcat for gunzip -c when reading a gzipped coverage
  file. This should avoid some Mac platforms crashing because zcat invariably
  requires a file to end in the .Z (which it doesn't...)
- coverage2cytosine: Changed the way in which the coverage input file is handed
  over from the methylation_extractor to coverage2cytosine (previously the path
  information might have been part of the file name, but instead it will now be
  only part of the -dir output_directory option

*Thu Feb 11 2016 Sidney Markowitz <sidney@biomatters.com> - 0.15.0-2
- Bismark
  - Added missing commands: bismark2bedGraph coverage2cytosine
      deduplicate_bismark bismark2report
*Fri Feb 05 2016 Shane Sturrock <shane@biomatters.com> - 0.15.0-1
- Bismark
  - Added option --se/--single_end <list>. This sets single-end mapping mode
    explicitly giving a list of file names as <list>. The filenames may be
    provided as a comma , or colon :-separated list.
  - Added option --genome_folder <path/to/genome> as alternative to supplying
    the genome as the first argument.
  - Added an option --rg_tag to print an @RG header line as well as and RG:Z:
    tag to each read. The ID and SAMPLE fields default to 'SAMPLE', but can be
    specified manually with --rg_id or --rg_sample.
  - Added new option --ambig_bam for Bowtie2-mode only, which writes out a
    single alignment for sequences with multiple alignments to a special file
    ending in .ambiguous.bam. The alignments are in Bowtie2 format and do not 
    any contain Bismark specific entries such as the methylation call etc. 
    These ambiguous BAM files are intended to be used as coverage estimators 
    for variant callers. Works for single-end and paired-end alignments in 
    single or multi-core mode.
  - Added the new options --cram and --cram_ref to Bismark for both paired- and
    single-end alignments in single or multi-core mode. This option requires
    Samtools version 1.2 or higher. A genome FastA reference may be supplied 
    as a single file with the option --cram_ref; if this is not specified the 
    file is derived from the reference FastA file(s) used for the Bismark run, 
    and written to the file Bismark_genome_CRAM_reference.mfa into the output 
    directory.
- deduplicate_bismark
  - Added better handling of cases when the input file was empty (died for
    percentage calculation instead of calling it N/A)
  - Added a note mentioning that Read1 and Read2 of paired-end files are
    expected to follow each other in two consecutive lines and possibly require
    name-sorting prior to deduplication. Also added a check that reads the 
    first 100000 lines to see if the file appears to have been sorted and bail 
    out if this is true.
- methylation extractor
  - Added support for CRAM files (this option requires Samtools version 1.2 or
    higher) bismark2bedGraph
  - Changed the way gzip compressed input files are handled when using the UNIX
    sort command (i.e. with --scaffolds/--gazillion or without --ample_memory
    coverage2cytosine
  - Added option --gzip to compress output files. This currently only works for
    the default CpG_report and CX_report output files (and thus not with the
    option --gc or --split_files. The option --gzip is now also passed on from 
    the bismark_methylation_extractor.
  - Added a check to bail if no information was found in the coverage file,
    e.g. if a wrong file path for a .cov.gz file had been specified
- bismark_genome_preparation
  - Added process handling to the child processes.

*Fri Aug 21 2015 Shane Sturrock <shane@biomatters.com> - 0.14.5-1
- deduplicate_bismark
  - Changed all instances of literal calls of 'samtools' calls to 
    '$samtools_path'.

*Thu Aug 20 2015 Shane Sturrock <shane@biomatters.com> - 0.14.4-1
- Bismark
  - Input files specified with filepath information for FastA files
    are now handled properly in --multicore runs (this was fixed only
    for FastQ files in the previous patch).
  - Changed the FLAG values of paired-end alignments to the CTOT or
    CTOB strands so that reads can be properly displayed in SeqMonk
    when imported as BAM files. This change affects only paired-end
    alignments in --pbat or --non_directional mode. In detail we simply
    swapped the Read 1 and Read 2 FLAG values round so reads now resemble
    xactly concordant read pairs to the OT and OB strands.  Note that
    results produced by the methylation extractor or further downstream of
    that are not affected by this change.
  - Changed the default mode of operation to --bowtie2. Bowtie (1) alignments 
    may still be chosen using the option --bowtie1.
  - Unmapped (option --unmapped) and ambiguous (option --ambiguous) files
    are now written out as gzip compressed files so they don't have to be
    gzipped manually every single time.
- Bismark Genome Preparation
  - Changed the execution of the genome indexing of the parent process to
    system() rather than an exec() call since this seemed to lead to
    interesting faults when run in a pipeline setting.
  - Changed the default indexing mode to --bowtie2. Bowtie (1) indexing is
    still available via the option --bowtie1.
- bismark2bedGraph
  - The coverage (.cov) and bedGraph (.bedGraph) files are now written out
    as gzip compressed files so you don't have to gzip them manually every
    single time.
- coverage2cytosine
  - Added a new option --gc_context to reprocess the genome and find
    methylation in GpC context. This might be useful for certain
    applications where GpC methylases had been deployed. The output format
    is exactly the same as for the normal CpG report, and only positions
    covered by at least one read are reported. A coverage file will also
    be written out.
- deduplicate_bismark
  - Removed redundant close() statements so there shouldn't be any warning
    messages popping up again.

*Thu May 07 2015 Shane Sturrock <shane@biomatters.com> - 0.14.3-1
- Bismark:
  - Changed the renaming settings for paired-end files so that 'sam' within 
    the filename no longer gets renamed to 'bam' (e.g. smallsample.sam -> 
    smallbample.sam).
  - Input files specified with filepath information are now handled properly 
    in --multicore runs. 
  - The --multicore option currently requires the files to be in BAM format, 
    so specifying --sam at the same time is disallowed.
- Methylation Extractor:
  - Another bug fix for the same issue as in 0.14.1 that had crept in the 
    0.14.2 release.
- coverage2cytosine:
  - Changed the option --merge_CpG so that CGs starting at position 1 are not 
    considered (since the 3-base sequence context of the bottom strand C at 
    position 2 can not be determined)

* Wed Apr 08 2015 Sidney Markowitz <sidney@biomatters.com> - 0.14.2-1
- Bismark: 
  - Fix cleaning up stage in a --multicore run when --gzip had been
    specified as well
  - Fix handling of files in a --multicore run when the input files had
    been specified including file path information
  - Disabled option -B/--basename used with --multicore, to be fixed later
- Methylation Extractor
  - Fix bug with position adjustment of paired-end reads when the reads
    should have been trimmed from their 3' ends (option --ignore_3prime)
- deduplicate_bismark
  - Remove newlines from read conversion tag

* Mon Mar 09 2015 Shane Sturrock <shane@biomatters.com> - 0.14.0-1
- Bismark: 
  - Finally added parallelization to the Bismark alignment step using the 
    option '--muticore int' which sets the number of parallel instances of 
    Bismark to be run concurrently. At least in this first distribution this 
    is achieved by forking the Bismark alignment step very early on so that 
    each individual Spawn of Bismark (SoB?) processes only every n-th 
    sequence (n being set by --multicore). Once all processes have completed, 
    the individual BAM files, mapping reports, unmapped or ambiguous FastQ 
    files are merged into single files in very much the same way as they would 
    have been generated running Bismark conventionally with only a single 
    instance. If system resources are plentiful this is a viable option to 
    speed up the alignment process (we observed a near linear speed increase 
    for up to --multicore 8 tested so far). However, please note that a 
    typical Bismark run will use several cores already (Bismark itself, 2 or 
    4 threads of Bowtie/Bowtie2, Samtools, gzip etc...) and ~10-16GB of memory 
    depending on the choice of aligner and genome. WARNING: Bismark Parallel 
    (BP?) is resource hungry! Each value of --multicore specified will 
    effectively lead to a linear increase in compute and memory requirements, 
    so --multicore 4 for e.g. the GRCm38 mouse genome will probably use ~20 
    cores and eat ~40GB or RAM, but at the same time reduce the alignment 
    time to ~25-30%. You have been warned...
  - Changed the default output to BAM. SAM output may be requested using the 
    option --sam
  - No longer generates a piechart (.png) with the alignment stats. 
    bismark2report generates a much nicer report anyway
- Methylation Extractor
  - To detect paired-end alignment mode from the @PG header line, white 
    spaces before and after -1 and -2 are now required. In some instances 
    files containing e.g. -1-2 in their filename might previously have been 
    identified as paired-end incorrectly
- deduplicate_bismark
  - To detect paired-end alignment mode from the @PG header line, white spaces 
    before and after -1 and -2 are now required
  - Added option --version so that Clusterflow can report a version number
- bismark2bedGraph
  - Fixed path handling for cases where the input files were given with path 
    information and an output directory had been specified as well
- coverage2cytosine
  - Fixed a typo in the shebang which prevented coverage2cytosine from running

* Mon Jan 12 2015 Shane Sturrock <shane@biomatters.com> - 0.13.1-1
- Bismark Genome Preparation
  - Added a check for unique chromosome names to the Bismark indexer to avoid 
    disappointments later.
- Bismark Methylation Extractor
  - Added a new option --mbias_off, which processes the files as normal but 
    does not write out any M-bias files. This option is meant for users who 
    run the methylation extractor two times, the first time to figure out 
    whether there is a bias that needs to be removed, and the second time 
    using the --ignore options, but without overwriting the already existent 
    M-bias reports.
  - Fixed a bug for the M-bias reports when the option --multicore was used, 
    in which case only the numbers of one core were used to constuct the 
    report. Now every different thread writes out an individual M-bias table, 
    and once the methylation extraction has completed all these individual 
    files are merged into a single, cumulative table as it should be.
  - Added closing statements for the BAM in disguise filehandle.
- bismark2bedGraph
  - Deferred removal of the input file path information a little so that 
    specifying file paths doesn't prevent bismark2bedGraph from finding the 
    input files anymore.
  - If the specified output directory doesn't exist it will be created for you.
  - Changed the way scaffolds are sorted (with --gazillion specified) to 
    -k3,3V (this was done following a suggestion by Volker Brendel, Indiana 
    University: "The -k3,3V sort option is critical when the sequence names 
    are numbered scaffolds (without left-buffering of zeros). Omit the V, and 
    things go very wrong in the tallying of reads.")
- coverage2cytosine
  - Added a new option --merge_CpG that will post-process the genome-wide 
    report to write out an additional coverage file which has the top and 
    bottom strand methylation evidence pooled into a single CpG dinucleotide 
    entity. This may be the desirable input format for some downstream 
    processing tools such as the R-package bsseq (by K.D. Hansen). An example 
    would be: 

    genome-wide CpG report (old)
           gi|9626372|ref|NC_001422.1|     157     +       313     156     CG
           gi|9626372|ref|NC_001422.1|     158     -       335     156     CG

    merged CpG evidence coverage file (new)
           gi|9626372|ref|NC_001422.1|     157     158     67.500000       648     312

    This option is currently experimental, and only works if CpG context only 
    and a single genome-wide report were specified (i.e. it doesn't work with 
    the options --CX or --split_by_chromosome).
  - Changed the processing of not-covered chromosomes so that they are sorted 
    and not processed randomly. This should make runs more reproducible.

* Thu Oct 02 2014 Shane Sturrock <shane@biomatters.com> - 0.13.0-1
- Bismark
  - Fixed renaming issue for SAM to BAM files (which would have replaced any 
    occurrence of sam in the file name, e.g. sample1_... instead of the file 
    extension .sam).
- Methylation Extractor
  - Added new option '--multicore <int>' to set the number of cores to
    be used for the methylation extraction process. If system resources
    are plentiful this is a viable option to speed up the extraction
    process (we observed a near linear speed increase for up to 10 cores
    used). Please note that a typical process of extracting a BAM file and
    writing out '.gz' output streams will in fact use ~3 cores per value
    of --multicore <int> specified (1 for the methylation extractor
    itself, 1 for a Samtools stream, 1 for GZIP stream), so --multicore 10
    is likely to use around 30 cores of system resources. This option has
    no bearing on the bismark2bedGraph or genome-wide cytosine report
    processes. 
  - Added two new options '--ignore_3prime <INT>' (for single-end
    alignments and Read 1 of paired-end alignments) and
    '--ignore_3prime_r2 <INT>' (for Read 2 of paired-end alignments) to
    remove positions that display a methylation call bias from the 3' end
    of reads.	     
  - The option --no_overlap is now the default for paired-end data. One
    may explicitly choose to include overlapping data with the option
    '--include_overlap'.
  - The splitting report will now be written out by default (option --report).
  - In paired-end mode, read-pairs which had been skipped because either
    read was shorter than a specified (very high) value of '--ignore' or
    '--ignore_r2' will now have the information of the other read
    extracted if it meets the length criteria (if applicable). Thanks to
    Andrew Dei Rossi for contributing a patch.
- bismark2bedGraph
  - Fixed the location of the sorting directory which could have failed if
    an output directory had been specified.

* Tue Jul 22 2014 Shane Sturrock <shane@biomatters.com> - 0.12.5-1
- Bismark: Added one more check to improve the ambiguous alignment
  detection. In more detail this adds a check whether the current
  ambiguous alignment is worse than the best alignment so far, in which
  case the sequence does not get flagged as ambiguous. Thanks to Ashwath
  Kumar for spotting these issues). 
* Tue Jul 22 2014 Shane Sturrock <shane@biomatters.com> - 0.12.4-1
- Bismark: Improved the way ambiguous alignments are handled in Bowtie 2
  mode. Previously, sequences were classified as ambiguously aligning as
  soon as a sequence produced several equally good alignments within the
  same alignment thread. Under certain circumstances however there may
  exist equally good alignments within the same alignment thread, but
  the sequence might have a better (unique) alignment in another thread.
  Such a unique alignment will now trump the ambiguous alignment as it
  should
- Bismark: Got rid of 2 warning messages of MD-tag information for reads
  containing deletions (Bowtie 2 mode only) which accidentally made it
  through to the release
- Bismark: Added '-x' to the invocation of Bowtie 2 for FastA sequences
  so that it works again (It used to work previously only because Bowtie
  2 did not check it properly and automatically used bowtie2-align-s,
  but now it does check...) 
- Methylation Extractor: Line endings are now chomped at an earlier
  stage so that interfering with the optional fields in the Bismark BAM
  file doesn't break the methylation extractor (e.g. reordering of
  optional tags by Picard)

* Thu Jun 26 2014 Sidney Markowitz <sidney@biomatters.com> - 0.12.3-1
- bismark: Replaced the XX-tag field (base-by-base mismatches to the
  reference, excluding indels) by an MD:Z: field that now properly
  reflects mismatches as well as indels.
- bismark: Fixed the hemming distance value (NM:i: field) for reads
  containing insertions (Bowtie 2 mode only), which was previously
  offset by the number of insertions in the read.
- bismark2bedGraph: Changed '--zero_based' option of the methylation
  extractor and bismark2bedGraph to write out an additional coverage
  file (ending in .zero.cov) which uses the UCSC zero-based,
  half-open standard.
- bismark2bedGarph: Changed the requirement of CpG context files to
  start with CpG... (from CpG_...).

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
