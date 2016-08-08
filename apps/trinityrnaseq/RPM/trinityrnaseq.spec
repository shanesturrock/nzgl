%define debug_package %{nil}

Name:		trinityrnaseq
Version:	2.2.0
Release:	1%{?dist}
Summary:	Provides software targeted to the reconstruction of full-length transcripts and alternatively spliced isoforms from Illumina RNA-Seq data.
Group:		Applications/Engineering
License:	BSD Modified
URL:		http://trinityrnaseq.sourceforge.net
Source0:	trinityrnaseq_%{version}.tar.gz
Patch0:		write_partitioned_trinity_cmds.pl.patch
Patch1:		run_Trinity_edgeR_pipeline.pl.patch
Patch2:		run_Trinity_from_samples_file.pl.patch
Requires:	java-1.6.0
Obsoletes:	trinityrnaseq_r20140717
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
Requires:	bowtie rsem
AutoReqProv:	no

%description
Trinity, developed at the Broad Institute and the Hebrew University of
Jerusalem, represents a novel method for the efficient and robust de novo
reconstruction of transcriptomes from RNA-seq data. Trinity combines three
independent software modules: Inchworm, Chrysalis, and Butterfly, applied
sequentially to process large volumes of RNA-seq reads.

%prep
%setup -q
# %setup -q -n %{name}_r%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
# Fix perl shebangs
find . -type f -name '*.pl' | xargs sed 's=/usr/local/bin/perl=/usr/bin/perl=g' --in-place
# Fix Trinity script
find . -type f -name 'Trinity' | xargs sed 's/\"$FindBin::RealBin\";/\"\/usr\/libexec\/trinityrnaseq\";/g' --in-place
%build
make %{?_smp_mflags}
make plugins %{?_smp_mflags}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{perl_vendorarch}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/Butterfly
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/Chrysalis

install -m 0755 Trinity %{buildroot}/%{_bindir}

install -m 0644 Butterfly/Butterfly.jar %{buildroot}/%{_libexecdir}/%{name}/Butterfly

install -m 0755 Inchworm/bin/cigar_tweaker %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin/cigar_tweaker
install -m 0755 Inchworm/bin/FastaToDeBruijn %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin/FastaToDeBruijn
install -m 0755 Inchworm/bin/inchworm %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin/inchworm
install -m 0755 Inchworm/bin/pull_reads_with_kmers %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin/pull_reads_with_kmers
install -m 0755 Inchworm/bin/fastaToKmerCoverageStats %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin/fastaToKmerCoverageStats

install -m 0755 Chrysalis/checkLock %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/checkLock
install -m 0755 Chrysalis/MakeDepend %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/MakeDepend
install -m 0755 Chrysalis/JoinTransByPairs %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/JoinTransByPairs
install -m 0755 Chrysalis/TranscriptomeFromVaryK %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/TranscriptomeFromVaryK
install -m 0755 Chrysalis/IsoformAugment %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/IsoformAugment
install -m 0755 Chrysalis/RunButterfly %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/RunButterfly
install -m 0755 Chrysalis/Chrysalis %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/Chrysalis
install -m 0755 Chrysalis/QuantifyGraph %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/QuantifyGraph
install -m 0755 Chrysalis/BreakTransByPairs %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/BreakTransByPairs
install -m 0755 Chrysalis/GraphFromFasta %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/GraphFromFasta
install -m 0755 Chrysalis/ReadsToTranscripts %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/ReadsToTranscripts
install -m 0755 Chrysalis/CreateIwormFastaBundle %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/CreateIwormFastaBundle

/bin/cp -r PerlLib/* %{buildroot}/%{perl_vendorarch}

/bin/cp -r util %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r trinity-plugins %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r Analysis %{buildroot}/%{_libexecdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README Changelog.txt
/usr/bin/Trinity
/usr/libexec/%{name}/*
%{perl_vendorarch}/*

%changelog
* Tue Aug 09 2016 Shane Sturrock <shane@biomatters.com> - 2.2.0-1
- Butterfly update: bugfix related to polynucleotide runs.
- util/SAM_nameSorted_to_uniq_count_stats.pl: count fragments instead of reads.
- util/abundance_estimates_to_matrix.pl: will output a matrix even if only a
  single sample is specified. Also, now can take a --samples_file containing a
  list of the target files to build the matrix from.
- util/align_and_estimate_abundance.pl: added support for salmon
- sample_data/test_align_and_estimate_abundance/: added examples and tests for
  single-end and paired-end abundance estimation

* Wed Oct 19 2015 Shane Sturrock <shane@biomatters.com> - 2.1.1-1
- Memory is divided among the samtools threads.
- The Trinity contig identifiers for genome-guided assemblies are now formatted
  correctly (as compared to v2.1.0).
- We now run a check to ensure that the number of fastq records being converted
  to fasta by fastools matches (sanity check).

* Wed Sep 30 2015 Shane Sturrock <shane@biomatters.com> - 2.1.0-1
- Abundance estimation: added support for kallisto and using TPMs now instead
  of FPKMs for downstream analyses.
- DE analysis: added support for Limma/Voom and ROTS, dropped support for
  DESeq(1) while keeping DESeq2. For edgeR w/o bio reps, user must define
  dispersion parameter.
- Minimal changes to the assembler, minor bug fixes, tackled most github
  'issues' from last release.
- Trinity documentation was reorganized, revised, and moved to the wiki format.

* Wed Sep 23 2015 Shane Sturrock <shane@biomatters.com> - 2.0.6-1
- Trinity v2.0 includes a number of significant changes as outlined
  below:
 - Logistics:
   - Trinity moves to github, with the new website location at:
     http://trinityrnaseq.github.io
   - User support now occurs through the google group:
     https://groups.google.com/forum/#!forum/trinityrnaseq-users
 - Software:
   - Trinity assembly now operates in two distinct phases (1):
     clustering reads and (2) assembly of reads. The phase (1) read
     clustering phase can be done by de novo read clustering (default) or
     in a genome-guided way (given a coordinate-sorted bam file). Phase (2)
     involves executing the complete Trinity process on each cluster of
     reads. For the de novo read clustering phase, existing Trinity
     components are used (Inchworm and Chrysalis), but that process will
     likely be replaced by an alternative mechanism in some future release.
     However, Inchworm and Chrysalis will continue to be core components of
     the Trinity assembly process (phase 2).
   - the Butterfly algorithm has been extensively revised to better
     integrate long read support and to improve on the assembly of
     complex isoforms, particularly those containing internally repetitive
     sequences.
- Numerous minor changes and differences in usage - see web
  documentation. Most notable changes are:
  - Trinity --max_memory instead of --JM, and simpler usage for the
    genome-guided method, which requires that the user provide a
    coordinate-sorted bam file with parameter: --genome_guided_bam.
  - if you have error-corrected pacbio reads, you can incorporate them
    with the Trinity --long_reads parameter. Note, however, if you
    have strand-specific RNA-Seq, you'll need to be sure to first reorient
    your pacbio reads so that they are sense strand oriented (we do not
    have an automated process to do that yet). Also, note that this new
    feature continues to be experimental and additional work is underway
    to fully demonstrate the added value from incorporating the long read
    data.
- v2.0.6
  - patch - had to 'autoconf --install' for the Inchworm build
- v2.0.5
  - Performance-related patch.
  - Files containing reads to assemble are now properly being fanned
    out across a number of directories and files, instead of
    inadvertently co-localizing them all in a single directory.
    Performance improvements should be observed in the context of large
    data sets.
- v2.0.4
  - Trimmomatic symlink set w/ capital T
  - additional testing built in
  - use parallel samtools always (not just w/ v1.1, silly!)
  - runtime latest-version checking added
- v2.0.3
  - Bugfix to Butterfly that accounts for rare edge-cases resulting in
    fatal error: DAG contains a cycle
  - Jellyfish is now only used in the initial stage-1 of Trinity (read
    clustering phase), and Inchworm does the kmer counting in stage-2
    (the assembly phase). This results in much faster runtimes,
    particularly on small data sets.
  - Trinity is much less verbose, especially in stage-2
  - Matt MacManes updated the Trimmomatic settings to those defined as
    optimal for trinity assembly.

* Tue Aug 05 2014 Shane Sturrock <shane@biomatters.com> - r20140717-1
run_DE_analysis.pl
    - added '--contrasts' to specify the DE comparisons to perform.
    - added support for DESeq2
abundance_estimates_to_matrix.pl
    - use check.names=F so as to allow for dashes and other characters that 
      R doesn't typically like in column headers.
IRKE.cpp
    - set hard limit on max recursion for tie breaking.
Butterfly:
    - transcript length normalization in EM algorithm.
    - EM should now be correct, in addition to useful.
    - added  --READ_END_PATH_TRIM_LENGTH <int> min length of read terminus 
      to extend into a graph node for it to be added to the pair path node 
      sequence. (default: 0)
Trinity
    - genome guided process errors out on failed gmap alignment via 
      'set -o pipefail'
Plugins
    - reorgnized, include tarballs for various plugins and untar-gz them 
      and build as part of Trinity make
    - updated to Jellyfish2
    - re-incorporating RSEM in plugins, updated to R-2.15, maintaining 
      compatibility with plugin-version.
    - updated TransDecoder to 20140704 version
    - fastool updated, includes bugfix regarding pair /1 or /2 identification 
      w/ certain linux distros
    - removed coreutils, using the 'sort' utility installed on users machine, 
      leverages parallel version if available.
    - updated to Trimmomatic-v0.32

* Wed Jun 11 2014 Sidney Markowitz <sidney@biomatters.com> - 20140413p1-2
- update options in call to rsem-prepare-reference for new version rsem 1.2.14

* Mon Apr 28 2014 Shane Sturrock <shane@biomatters.com> - 20140413p1-1
- bugfix to trimmomatic_SE processing
- added checkpoint for trimming operation / resume-level support' Trinity 

* Wed Apr 16 2014 Shane Sturrock <shane@biomatters.com> - 20140413-1
Trinity (was Trinity.pl)
    - incorporated auto-trimmomatic
    - incorporated auto-normalization
Fastool:
    - exit with non-zero on error, write error msgs to stderr.
Inchworm:
    - parallel inchworm assembly introduced via openMP
fastaToKmerCoverageStats:
    - dont stop processing on empty read sequence, only on eof() /silly/
      LSF,SGE,SLURM incorporation
    - replaces the need for users to build custom adapters. Use an ultra-simple 
      config file instead.
    - updated HTC modules to cache successfully completed commands during the 
      run, and to perform better file management.
    - thanks to Jean-Marc Lassance for the SLURM support integration.
Butterfly:
    - better handling of PE info in defining extension support criteria 
      (look-back, define path requirement [A...E], require A,E in supporting 
      path + compatibility with growing path).
    - at end of butterfly, use EM to rank isoforms, report only those that 
      contain unique read content as output in order of ranking.
    - ParaFly and CuffFly modes overhaul, removing contained aligments from 
      DAG due to inherrent transitivity-breaking property, treat PE as SE to 
      avoid uncertain compatibilities and transitivity-breaking situations.
    - added ParaFlyUnique method for experimental use.
    - new Fasta accession format:  c\d+_g\d+_i\d+  (c=component, g=gene, 
      i=isoform)  (use combination of c+g to define 'gene')
    - in the path description in the fasta header, identify nodes in X 
      structures that are unresolved by read paths as '@node_id@!'
Expression Estimates:
    - support both RSEM and eXpress, and bowtie1&2
    - use: util/align_and_estimate_abundance.pl to generate alignments 
      (bowtie1 or bowtie2) and estimate abundance (RSEM or eXpress) 
    - use: util/abundance_estimates_to_matrix.pl to construct count, and 
      TMM-normalized fpkm matrices

* Mon Jan 20 2014 Shane Sturrock <shane@biomatters.com> - 20131110-1
Butterfly:
    - convert gapped-pairpaths into single pairpaths where internally
      traversed nodes can be imputed as unambiguous (bhaas).
    - first introduction of PasaFly and CuffFly modes for transcript
      reconstruction:
      - PasaFly: an implementation of the PASA transcript
        reconstruction algorithm in the context of reference-free
        transcriptome graphs. Each PairPath is repr esented within a
        reconstructed transcript that is maximally supported by compatible
        PairPaths. (bhaas) 
      - CuffFly: an implementation of the Cufflinks transcript
        reconstruction algorithm in the context of reference-free
        transcriptome graphs.  The minimum num ber of transcripts are
        reconstructed to reflect the sets of compatible PairPaths. (Maria
        Rodgriguez (MIT), Po-Ru Loh (MIT), Brian Haas (Broad), and Moran 
        Yassour (Broad).
    - transcript reduction occurs after all paths have been reconstructed, 
      instead of also during reconstruction.
    - removed the max_paths_per_node, replaced by 
      max_number_of_paths_per_node_init, max_number_of_paths_per_node_extend, 
      and max_number_of_paths_per_pasa_node.
    - an extended_triplet mode (enacted by default under Trinity.pl, and 
      disabled by the earlier --no_triplet_lock) applies further constraints 
      to the paths allowed to be extended, excluding those that conflict with 
      paths of overlapping reads.

Trinity.pl: 
    - default for  --bflyHeapSpaceMax set to 10G instead of 20G (bhaas)
    - Added parameters --PasaFly and --CuffFly to invoke the new alternative
      Butterfly reconstruction modes. (bhaas)

jellyfish:  
    - Use jellyfish merge to build a single kmer db from which the kmers and 
      counts are then emitted, instead of emitting kmers from the kmer 
      partition files.  Done for both Trinity.pl and read normalization 
      process. (bhaas)
    - Report kmer count histogram. (bhaas)

Chyrsalis:
    - ReadsToTranscripts:  convert read sequences to uppercase before doing 
      mapping to components. (bhaas)

Makefile:   
    - set inchworm and chrysalis to inchworm_target and chrysalis_target, 
      since inchworm and chrysalis were being confused with the named 
      directories in the base installation on some hardware (some mac os) 
      (bhaas)

analyze_diff_expr.pl:  
    - back to median centering expression values per transcript before gene 
      clustering. (bhaas)

util/normalize_by_kmer_coverage.pl:
    - report the number of reads stochastically selected and the number that 
      are excluded as likely aberrant. (bhaas)
    - the --max_pct_stdev  default is now 200 (instead of 100), which defines 
      fewer reads as aberrant, flagging only the extreme outliers. (bhaas)
    
util/TrinityStats.pl:
    - include additional stats, including: mean trans len, median trans len, 
      and %GC. (bhaas)

trinity-plugins/Transdecoder
    - updated to release 11-10-2013

* Wed Oct 02 2013 Shane Sturrock <shane@biomatters.com> - 20130814-1
- Trinity.pl
  - The --full_cleanup option will only purge output directories generated by 
- Trinity during that run.
  - now properly exit(0) under --no_run_butterfly
  - added the '--no_bowtie' parameter to skip bowtie-based read mapping 
    during the chrysalis scaffolding stage
- DE-analysis:
  - Analysis/DifferentialExpression/R/manually_define_clusters.R  
    :bugfix, now retains compatibility with related DE scripts.
  - Analysis/DifferentialExpression/analyze_diff_expr.pl 
    :green-to-red instead of red-to-green, and use quantiles to set up 
    color scaling
  - Analysis/DifferentialExpression/run_TMM_normalization_write_FPKM_matrix.pl 
    : auto-change '-' to '.' chars in column headers
  - Analysis/DifferentialExpression/run_DE_analysis.pl  in the sample A vs. B 
    comparisons, sample A name is now consistentely lexically < B.
- Genome-guided Trinity:
  - util/SAM_to_frag_coords.pl :improved compatibility with SE reads
    - genome-guided Trinity has improved recovery from earlier failures on 
      re-run.
    - deprecated inchworm_accession_incrementer.pl, replaced with: 
      GG_trinity_accession_incrementer.pl  (using GG${num}|comp...  for 
      identifiers, where GG$num|comp\d+ corresponds to gene/component 
      identifier.
- Inchworm:
  - added developer-specific options for examining importance of various steps 
    (sorting, tie-breaking)
  - reverted kmer sorting to using pair<kmer,abundance> instead of sorting 
    iterators
    - pruned kmers remain in hashtable but zeroed out
    - inchworm fasta header extended to include coverage and extension info.
    - improved developer documentation
    - now properly recognize jaccard-clipped inchworm contig accessions in 
      bowtie output in prep for Chrysalis clustering 
      (util/scaffold_iworm_contigs.pl)
- Chrysalis:
  - fewer output files prepped: single components output file and iworm bundles
    fasta file  (so ~half total files)
  - FastaToDebruijn: generates de Bruijn graphs from single iworm bundles fasta
    file, uses OMP for parallelization
  - now introducing 'util/partition_chrysalis_graphs_n_reads.pl' to prep the 
    many files for chrysalis::quantifyGraph and Butterfly
- Trinotate:
  - revised database schema, store gene/transcript info, expression data, 
    and no longer Trinity-exclusive (more generally useful).
  - incorporated web-gui for annotation and expression navigation and analysis
  - can store/report multiple blast hits
  - ** relocated Trinotate and TrinotateWeb to http://trinotate.sf.net  **
- RSEM_util/run_RSEM_align_n_estimate.pl
  - can use gzipped read files as input.
  - can set output directory via --output_dir
  - look for RSEM utilities via PATH setting. No longer bundling the full RSEM 
    software as it's better for users to always obtain the la test version 
    separately.
- ReadNormalization:
  - in PE mode, can use disordered seqs if given the '--PE_reads_unordered' 
    parameter to script 'util/normalize_by_kmer_coverage.pl'
  - added sample test runner at:  sample_data/test_InSilicoReadNormalization
  - fastaToKmerCoverageStats.cpp: using 'unsigned int' rather than 'int', 
    and error-out on negative mean, tackle larger data sets.
  - run jellyfish at min kmer cov = 2 and have fastaToKmerCoverageStats 
    identify 'missing' kmers as coverage 1, huge memory reduction in the 
    process.
  - no longer set min kmer coverage as an option. It's now fixed at 2 due to 
    the above.
- util/SAM_nameSorted_to_uniq_count_stats.pl
  - bugfix, now properly count improper pairs as compared to left-only or 
    right-only read alignments.
* Mon Feb 18 2013 Shane Sturrock <shane@biomatters.com> - 20130225-1
- New upstream release
* Mon Feb 18 2013 Shane Sturrock <shane@biomatters.com> - 20130216-1
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 20121005-1
- New upstream release
* Tue Sep 04 2012 Carl Jones <carl@biomatters.com> - 20120608-6
- Include Analysis/
* Tue Sep 04 2012 Carl Jones <carl@biomatters.com> - 20120608-5
- Move Butterfly.jar into libexec
* Tue Sep 04 2012 Carl Jones <carl@biomatters.com> - 20120608-4
- Fix ROOTDIR in Trinity.pl
- Include utils/ and trinity-plugins

* Fri Aug 10 2012 Carl Jones <carl@biomatters.com> - 20120608-3
- Move binaries to libexec
- Patch Trinity.pl so it finds the correct binaries

* Fri Aug 10 2012 Carl Jones <carl@biomatters.com> - 20120608-2
- Fix paths

* Mon Aug 06 2012 Carl Jones <carl@biomatters.com> - 20120608-1
- Initial build.
