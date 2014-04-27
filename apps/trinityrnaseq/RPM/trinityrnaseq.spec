%define tarball r20140413p1
%define debug_package %{nil}

Name:		trinityrnaseq
Version:	20140413p1
Release:	1%{?dist}
Summary:	Provides software targeted to the reconstruction of full-length transcripts and alternatively spliced isoforms from Illumina RNA-Seq data.
Group:		Applications/Engineering
License:	BSD Modified
URL:		http://trinityrnaseq.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}_%{tarball}.tar.gz
Patch0:		%{name}-rootdir.patch
Patch1:		GG_write_trinity_cmds.pl.patch
Patch2:		run_Trinity_edgeR_pipeline.pl.patch
Patch3:		Makefile.patch
Requires:	java-1.6.0
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
%setup -q -n %{name}_%{tarball}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
# Fix perl shebangs
find . -type f -name '*.pl' | xargs sed 's=/usr/local/bin/perl=/usr/bin/perl=g' --in-place

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{perl_vendorarch}
mkdir -p %{buildroot}/%{_bindir}
#mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/Butterfly
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/Chrysalis

install -m 0755 Trinity %{buildroot}/%{_bindir}

#install -m 0644 Butterfly/Butterfly.jar %{buildroot}/%{_javadir}/%{name}
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

/bin/cp -r PerlLib/* %{buildroot}/%{perl_vendorarch}

/bin/cp -r util %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r trinity-plugins %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r Analysis %{buildroot}/%{_libexecdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/ README Release.Notes
/usr/bin/Trinity
#/usr/share/java/%{name}/Butterfly.jar
/usr/libexec/%{name}/*
%{perl_vendorarch}/*

%changelog
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
