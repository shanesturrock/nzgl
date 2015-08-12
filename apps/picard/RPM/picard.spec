Name:		picard
Version:	1.138
Release:	1%{?dist}
Summary:	Java utilities to manipulate SAM files

Group:		Applications/Engineering
License:	MIT
URL:		http://picard.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}-tools-%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

Requires:	java >= 1:1.6.0
Requires:	jpackage-utils

%define __jar_repack 0

%description

Picard comprises Java-based command-line utilities that manipulate SAM
files, and a Java API (SAM-JDK) for creating new programs that read
and write SAM files. Both SAM text format and SAM binary (BAM) format
are supported.

%prep
%setup -q -n %{name}-tools-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_javadir}/%{name}

cp *.jar %{buildroot}%{_javadir}/%{name}

mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)

%{_javadir}/%{name}/*

%changelog
* Thu Aug 13 2015 Shane Sturrock <shane@biomatters.com> - 1.138-1
- fix HistogramWidth in InsertSizeMetricCollector
- added a utility function to get the log of a list of doubles.
- Updated docs on gatk-tools-java usage
- Fixing previous mistake with scheme logic
- Add support for sequential FASTQ files in SamToFastq using the
  USE_SEQUENTIAL_FASTQS option.  Sometimes we have the Fastq records for a one
  end of a read in multiple files with the suffix <prefix>_001.fastq,
  <prefix>_002.fastq, ..., <prefix>_XYZ.fastq, and we want to treat them all 
  as one file.
- Fixed bug that caused BedToIntervalList to flip strand of all features with 
  a strand field. Also fixed the test case so that it correctly tests that the
  strand doesn't flip!
- Updated GenotypeConcordance so that it doesn't fail when trying to use
  indexes on tabix indexed VCFs.

* Wed Jul 29 2015 Shane Sturrock <shane@biomatters.com> - 1.137-1
- Fixed up more BED tests for moving SAM version to 1.5
- Modified BedToIntervalList to accept other dictionary files
- Added ability to pass argument to ViewSam for an interval file that
  the output will be restricted to.  This does not support both the
  in-line intervals as well as interval file that the GATK -L command
  supports.  Unit test added to verify records from a given SAM are
  matched with overlapping intervals file, and no others are output.
  Updated existing TODOs to make use of PicardCommandLine rather than
  direct calls into ViewSam class within unit tests.
- Added better error messaging for corrupt bcl.gz files
- Fixed the output of scattering intervals to be .interval_list
- Fixed a small bug in IntervalListTool where in some cases bases were
  not accounted for in the total count (this can lead to non-uniform
  intervalLists in the scatter)
- Removed an erroneous Exception that was thrown when the intervals were
  not uniformly enough sized. We cannot guarantee that they will be
  uniformly sized...
- Fixed -1 error that was causing the last IntervalList to be double the
  size of all the others
- Added a dockerfile to picard
- Adding a tool SimpleMarkDuplicatesWithMateCigar that uses the new
  HTSJDK DuplicateSetIterator
- Disabled reference download
- Added support for creating tabix indexes.
- Removed default implementation of FeatureCodec.canDecode to enforce
  implementation in concrete classes
- Re-factored tests to test all SAM format versions based on acceptable
  versions in SAMFileHeader
- Added enum describing SAM FLAG (for gui/ menu / etc... )
- Added new SAM tags as of v1.5
- Changes to accommodate v1.5 of the SAM file specification.
  Updated version references in SamFileHeader.java,
  ValidateSamFileTest.java, and test files. Added test to
  ValidateSamFileTest which runs validation on the new test file
  test_samfile_version_1pt5.bam which contains reads with the new
  options of v1.5: the 0800 SUPPLEMENTARY flag and the SA:Z optional
  field.
- Fixed for incorrect return value in Genotype.getAnyAttribute()
- Added unit tests for validation methods in VariantContext
- Added 'checkError' in VariantContextWriter interface. Motivation: when
  Output stream is an interrupted PrintStream.
- Added getAttributeAsList in CommonInfo and VariantContext / fix indent

* Wed Jul 15 2015 Shane Sturrock <shane@biomatters.com> - 1.136-1
- Added the normalized minimum coverage over a target to the per-target 
  output

* Wed Jul 01 2015 Shane Sturrock <shane@biomatters.com> - 1.135-1
- Change to allow callers to request the non-indexed reader(s) from the 
  reference sequence file factory, and for the reference sequence file 
  walker to use the non-indexed reader since it is much more efficient for 
  a linear traversal.  See issue #269.
- Made several metrics classes serializable
- Added CollectRnaSeqMetrics to CollectMultipleMetrics
- Allow the generation of charts using the r script within the picard.jar 
  itself
- Fixed bugs in CollectMultipleMetrics where it will notify a user if 
  reference sequence is not specified but is needed. Also removes 
  CollectGcBiasMetrics from the list of default programs.
- Implementing a few wording changes after discussion with Nils
- Minor change to BedToIntervalList to make sorting and uniquing optional 
  vs. the prior behaviour of always sorting and uniquing the intervals.

* Mon Jun 15 2015 Shane Sturrock <shane@biomatters.com> - 1.134-1
- Picard changes:
  - Don't ignore strand when comparing Genes.
  - CollectGcBiasMetrics as a MultiLevelCollector; Added to Collect Multiple 
    Metrics. Tests included. Updated R Script to output multiple levels. 
    Default level of collection is All Reads and Library.
  - Fix test for zero-length exon.
  - The exons are closed intervals, so the test was rejecting an exon of 
    length 1.
- HTSJDK Changes 
  - Modified SAMLineParser to only invoke SAMRecord.isValid() if 
    ValidationStringency is set to something other than SILENT. Speeds up the 
    parsing of SAM (not BAM) text files when validaiton stringency is silent.
  - Pass isRef to Allele.acceptableAlleleBases() in 
    AbstractVCFCodec.checkAllele()

* Tue Jun 02 2015 Shane Sturrock <shane@biomatters.com> - 1.133-1
 - Modify GenotypeConcordance to explicitly require that the VCF files be 
   indexed if an interval file is specified
 - Add spanning deletions Allele to Alle.create() doc
 - Add wouldBeStarAllele(), Ns can be REF or ALT
 - adding unit tests for unmapped reads with and without SEQ/QUAL fields.
 - code format and imports organized according to intellij style
 - merged htsjdk.samtools.cram.structure with v3
 - merged htsjdk.samtools.cram.io with v3
 - merged htsjdk.samtools.cram.lossy with v3
 - merged htsjdk.samtools.cram.ref with v3
 - merged htsjdk.samtools.cram.encoding with v3
 - merged htsjdk.samtools.cram.build with v3
 - merged htsjdk.samtools.cram.index with v3
 - added deps and CRC32 files to git; minor fixes in cram/build and slice 
   classes
 - added  cram/digest package and code format/import to cram package
 - fixed CramFileWriter test to pass; added swing inspector for CRAM files;
 - minor updates and moved index and inspector stuff to another project
 - removed cram.mask package as unused; moved CRC32 streams to io package
 - javadoc and cleanup in cram.io.Bit*putStream API
 - cram.io package and CRAM Block class reworked: clean up, re-format, 
   ITF8 and LTF8 tests;
 - Cram container IO separated from CramIO; CramHeader and versioning re-worked
 - relaxed assert tests for original vs restored roundtrip of SAM records 
   while writing CRAM.
 - added support for SAM supplementary 0x800 bit flag
 - rebased and added SubsMatrix tests
 - Allow comment lines in liftover chain files.
 - Issue #196 - fixes a bug which causes an overflow in the CIGAR when a BAM 
   file is parsed that contains a read that spans a very large intron. The bug 
   is caused by the use of an arithmetic (>>) rather than a logical (>>>) 
   right shift operator in BinaryCigarCodec.binaryCigarToCigarElement(). This 
   fix substitutes the logical for the arithmetic operator, and implements a 
   test which reads the sample BAM file (containing a single record) that 
   exposed the bug and compares the indexing bin field with the computed 
   indexing bin field. If the two fields are different, an error is thrown.
 - Issue #181 - deletes the deprecated OldDbSNPFeature and OldDbSNPCodec 
   classes, along with the test class OldDbSNPCodecTest.
 - Javadoc formatting improvements for htsjdk.variant.* packages
 - Fixed some formatting issues in Javadoc comments
 - Fixed Javadoc formatting in htsjdk.variant package and subpackages.
 - Adding an ability to iterate through duplicate sets using a 
   DuplicateSetIterator.
 - Added tests for supplemental, secondary and unmapped reads.
 - Buffering writes to tribble index files
 - Reduced size of getSubsequenceAt() internal buffer if the default buffer 
   size is larger than length of the subsequence requested. This significantly 
   improves performance when requesting many small subsequences.
 - Removed 2s idle thread delay when closing asynchronous SAM writer
 - Fix catastrophic bug in VCFHeader that caused newly-added header lines to 
   be silently dropped
 - Split by char to remove some hard limits in AbstractVCFCodec
 - Fix bug in VCFHeader that caused newly-added header lines to be silently 
   dropped
 - There was a nasty bug in VCFHeader that caused newly-added header lines
   to only be added to type-specific lookup tables and not to the master list
   of header lines. This meant that new lines got silently dropped when writing
   a modified VCFHeader back out via VCFWriter.
 - Fixed the issue and added comprehensive unit tests for 
   VCFHeader.addMetaDataLine(), as well as a VCFWriter test to ensure new 
   header lines get persisted.
 - Also attempted to improve documentation and method naming a bit in an
   effort to avoid future bugs like this. Eg., there was a method 
   "loadVCFVersion()" that actually REMOVED the vcf version lines!
 - Remove pre-allocation of fixed-size arrays in AbstractVCFCodec
   - use a String.split-like function that just works for char delimiters
   - explain why String.split is not used (performance issues because
     regexes are used unnecessarily in some version of Java)
   - tests to show equvalent function to String.splt and roundtripping
     with ParsingUtils.join
   - fixes Issue #229
 - Added checks to adding an interval to an IntervalList: contig must be in 
   header. Note that one could still forcefully modify the underlying 
   dictionary, so the protection is only partial.
 - Removed protection code from the "padding" function since now contig 
   should be in header

* Mon May 11 2015 Shane Sturrock <shane@biomatters.com> - 1.131-1
- Change to IntervalListTools to use the new padded() methods in IntervalList.
- New CLP Position-based Downsampling. this method is supposed to permit 
  downsampling that mimics closely what would happen were you to sequence 
  less after downsampling one needs to re-run MarkDuplicates. Mate-pairs are 
  preserved (of course!)
- Also included is a simpler PhysicalLocation class which works like the one 
  in MarkDuplicates but is divorced from the read-ends concept and also uses 
  int rather than shorts for the x and y coordinates (within the tile) thus 
  doesn't overflow on HiSeqX like the MarkDuplicates one does.
- Make method public so that a sequence dictionary can be created 
  programmatically without having to write, then read a file.
- Changes to enable MergeBamAlignment to output in query name order without 
  sorting first into coordinate and then back again into coordinate. The only 
  caveat is that if outputting query name order then neither NM or UQ are 
  calculated (similar to the behaviour if no reference sequence is provided).
- Adding a tool that collects per-sample and aggregate (spanning all samples) 
  metrics from the provided VCF file.
- Add a new method for scattering intervals whereby we try to estimate the
  sizes of interval lists that have not been created. This should produce
  a more balanced set of interval lists, while fixing the maximum number
  of scatters.
- Fix NPE when nonstandard bases are found
- Fixing GcBias - double counting total clusters
- Add support for reading data from Google Genomics implementation of GA4GH 
  API

* Wed Apr 08 2015 Sidney Markowitz <sidney@biomatters.com> - 1.130-1
- Add command line support for setting @RG-PG and @RG-PM in FastqToSam and
  AddOrReplaceReadGroups
- Fixed typo in output filename
- Fix build file to expand lib jars before packaging the picard CLP jar.
  Fixes snappy integration.
- Tool to liftover, sort and index a VCF in a single pass.
- Added ability to taken an interval list and split into finer intervals
  based on band multiples to allow for finer granularity of scattering
- Modified IntervalListTools so that if scattering we do the sorting and
  unification up front (and not in the scatter method).
  This was important for BREAK_BANDS_AT_MULTIPLES_OF where the unique
  in scatter was re-merging broken adjacent intervals.
- Interval list file in scattered directories NOT broken up into multiples.
- Adding needed build modifications for sonatype publishing
- Changed CollectGcBiasMetrics to work as a SinglePassSam
- New tool for quantifying artifacts

* Tue Feb 24 2015 Shane Sturrock <shane@biomatters.com> - 1.129-1
- Enable file source for Bam Index creation.
- Separate out the actual work for FastqToSam so an outside caller can
  directly pass in FastqReaders
- A recent change to the command line parsing causes problems with scala
  based CLPs. In cases where the new system fails, fall back to the original
  system
- Allow tools to work with GA4GH resources specified via urls. This first
  batch includes AddOrReplaceReadGroups, MarkDuplicates and ViewSam.
- HTSJDK changes
  - removing SAMRecord.setAlignmentEnd it throws unsupported operation
    exception
  - adding getResourceDescription() to SamReader
  - fixed issue 155: CRAMFileWriter injects slice refMD5 now; added slice
    refMD5 check into CRAMIterator, for now only error message is show.
  - Made ReadTag.buf ThreadLocal. Fixes
    https://github.com/samtools/htsjdk/issues/153

* Wed Jan 14 2015 Shane Sturrock <shane@biomatters.com> - 1.128-1
- Refactoring CollectWgsMetrics in order to be able to easily create
  CollectRawWGSMetrics.
- Create RawWGSMetrics by overriding some default option values and
  repackaging the metrics class.
- Moved CollectIlluminaSummaryMetrics (will be deleted eventually)
- Fixed some test files.
- Removed the buggy CLP CollectIlluminaSummaryMetrics.java and its test
- Modified CommandLineParser class (and test) to fix overridable option
  fields
- Modified PicardCommandLine class
  - allow --list-commands to print all available commands to STDOUT
  - allow colors to be disabled with -Dpicard.cmdline.color_status=false
- Modified Interval List Tool to add functionality so that it can use VCF
  as a source for intervals
- Modified VCFConstants - removing GATK-specific constants
- Added test (SamSpecInTest) to check min/max values for i tag in SAM/BAM
- Added input validation functions that can deal with both file and URL
inputs, in preparation for allowing GA4GH resources as inputs into Picard
tools.
- Made static methods in TextCigarCodec and BinaryCigarCodec
- isCRAMFile moved to SamStreams. Use readBytes instead of dis readFully
- Fixed race condition in SAMFileWriterImpl  where synchronouslyClose()
  would be called multiple times if AbstractAsyncWriter.close() called twice
  simultaneously
- Enhancements to VCFFileReader:
  - Added functionality so that fromVCF can create an intervalList with or
    without filtered variants (defaulting to without, as currently)
  - Added functionality to fromVCF so that the intervals will end at the
    END value from the info field (if available).
- Make SortingVariantContextWriter public.
  - Currently, the only way to access this functionality is through
    VariantContextWriterFactory.sortOnTheFly,
    but VariantContextWriterFactory is deprecated.

* Wed Dec 17 2014 Shane Sturrock <shane@biomatters.com> - 1.127-1
- CRAM file support
- Make parseOptionsFile public, with a little more control over behavior.
- SamReader conversion of Picard public.
- Added common argument for reference fasta to support CRAM input/output.
- Reference fasta should be optional.
- Use SamReaderFactory makeDefault with reference sequence whenever possible 
  to allow for CRAM support.
- Added read group tag option, resolves #108 #114
- Various aesthetic tweaks for HTML doc generation.
- Fixed Faked Filter files.  Need them to be of size one element for the
  faked filter file to have the same number of elements as other faked types.

* Thu Dec 04 2014 Shane Sturrock <shane@biomatters.com> - 1.126-1
- Fixed error in FilterFileFaker.  Changed cluster count in faked filter
  file to be 0.  Added unit test to test for readability of faked files.
- Modified FastqToSam to strip the "/2" when using
  STRIP_UNPAIRED_MATE_NUMBER
- Modified ViewSam.  Added option to show only the header or only the
  records.

* Fri Nov 21 2014 Shane Sturrock <shane@biomatters.com> - 1.125-1
- Add new statistic 'Specificity' to GenotypeConcordance tool
- Removed some sun.reflect imports from codebase

* Tue Nov 04 2014 Shane Sturrock <shane@biomatters.com> - 1.124-1
- Change Picard Command Line Programs to ALL execute from single JAR
  This makes a fundamental change to how we run Picard.  We now have a
  single JAR (command line program), rather than multiple JAR (one per
  tool). In this brave new world, the single command line program is given
  the the command line program name (ex. SamView) to specify which tool to
  run.  We also provide a convenient summary of all of the tools
  available.

  For the developers, we add a facility to add new command line programs
  to the single JAR, by extending the PicardCommandLine and adding the
  package name(s) for us to search for classes that extend
  CommandLineProgram.  The usage is now put in
  CommandLineProgramProperties, where we can also specify short usages
  (for the summary help message), program versions, and program groups.
  The latter is useful for grouping tools that operate on common filetypes
  or have similar function (ex. SAM/BAM).

  We made a number of new tools public, coming from our internal toolset.
  These include: BaitDesigner, CalculateReadGroupChecksum, CheckTerminatorBlock,
  CollectIlluminaBasecallingMetrics, CollectIlluminaLaneMetrics,
  CollectJumpingLibraryMetrics, CollectOxoGMetrics,
  CollectQualityYieldMetrics, CollectRrbsMetrics, GatherVcfs,
  LiftOverIntervalList, ScatterIntervalsByNs, and SplitSamByLibrary.
  These may prove useful, or not.

- Changed Output of GenotypeConcordance tool
  Additional metrics file output which contains the raw counts of contingency
  values (i.e. TP for true positives, FN for false negatives...)

- New CLP 'CollectIlluminaSummaryMetrics' to collect coverage information
  according to Illumina-defined filters.

- New CLP 'RenameSampleInVcf' to rename a sample in a VCF

- New CLP 'FilterVcf' that provides simple hard filtering functionality for
  VCFs.

- Added ability to open SamReader from string, specifying either a URL or a
  file path. This will make it easier treat INPUT parameters in Picard tools
  uniformly regardless of whether they designate a file or URL resoures.
  Url detection and decision of whether the resource is file based on url 
  based is done in SamInputResource.

- Some support for VCF v4.2 files added.
  Handles "Number=R" for INFO fileds in the header.
  Other VCF v4.2 specific additions (Eg: Source and Version fields in
  INFO header lines) are not handled, but appear to be silently ignored.
  Tested on output of samtools mpileup | bcftools call (1.0-17-gfaf4dd6,
  1.0-55-gc661821, using htslib 1.0-11-g830ea73)

- Bug fix: 'fixed the behavior of BCF2Utils.toList() when it's given an array' 
  Old version return a List with a single element, which was the provided
  array. This broke BCF writing, in particular when a FORMAT annotation used
  arrays instead of Lists
  Made toList generic, rather than returning a List<Object>
  Removed the redundant BCF2FieldEncoder.toList()
  Added unit tests

- Bug fix in Abstract AlignmentMerger
  Consider soft clipping at the ends of reads when clipping reads that
  overhang the reference

- Added a button to the explain-flags.html page.
  This button switches the flag from the value of a read, to that of its mate
  (as much as can be inferred).

* Wed Oct 22 2014 Shane Sturrock <shane@biomatters.com> - 1.123-1
- Updates to "GenotypeConcordance" Command Line Program
  - Update the genotype concordance scheme to have called variants that
    are filtered be counted as though they are missing
  - Improvement to handle 'mismatching' ref alleles for indel
- comparison conditions.
  - Changed default extension of metrics files
- Improvements to htsjdk testing
  - Cleanups regarding temporary files in tests
  - Delete index files for temp files at the end of testing, and
    do not write temp files within source directory.

* Thu Oct 09 2014 Sidney Markowitz <sidney@biomatters.com> - 1.122-1
- GenotypeConcordance (new command line program):
  - Calculates the concordance between genotype data for two samples in two
    different VCFs - one being considered the truth (or reference) the
    other being considered the call.  The concordance is broken into
    separate results sections for SNPs and indels.
    Summary and detailed statistics are reported.
    Note that for any pair of variants to compare, only the alleles for the
    samples under interrogation are considered and MNP, Symbolic, and
    Mixed classes of variants are not included.
- UpdateVcfDictionary (new command line program):
  - Updates the sequence dictionary of a VCF from another file
    (SAM, BAM, VCF, dictionary, interval_list, fasta, etc).
- VcfToIntervalList (new command line program):
  - Create an interval list from a VCF
- MarkDuplicatesWithMateCigar (new command line program):
  - A new tool with which to mark duplicates:
   This tool can replace MarkDuplicates if the input SAM/BAM has Mate CIGAR (MC)
   optional tags pre-computed (see the tools
   RevertOriginalBaseQualitiesAndAddMateCigar and FixMateInformation).
   This allows the new tool to perform a streaming duplicate
   marking routine (i.e. a single-pass).  This tool cannot be used with
   alignments that have large gaps or reference skips, which happens
   frequently in RNA-seq data.
- IntervalList:
  - Added capacity to create a simple interval list from a string
    (the name of the contig)
  - Added the capacity to subtract one interval list from another (currently
    it would only work if they were both wrapped inside a container)
- SamLocusIterator:
  - Performance optimizations gaining about 35% speed up.
- MarkDuplicates:
  - Removed unnecessary storage of a string in the Read Ends in Mark
  - Clarifed the size of ReadEndsForMarkDuplicates
- Updated the minimum number of times that the BAIT_INTERVALS
  (in CalculateHsMetrics) and TARGET_INTERVALS (in CollectTargetedMetrics)
  must be set to one.
- Moved CollectHiSeqPfFailMetrics into picard public
- Moved SAMSequenceDictionaryExtractor and tests from picard to htsjdk

* Thu Sep 25 2014 Shane Sturrock <shane@biomatters.com> - 1.121-1
- Picard:
  - Added a static function to PedFile that allows the creation of a pedFile 
    object from a Map<String,Sex>.
  - Fixed BAMRecordCodec to  recognize when qual array has been changed.
  - Added a SortVcfs CLP that will sort VCF files by contig and genomic 
    position.
  - Supplemental alignments are now considered when fixing mate information in 
    FixMateInformation and RevertOriginalBaseQualitiesAndAddMateCigar.
  - RevertSam: Added ability to use  original qualities to detect encoding 
    scheme if they are being restored. Modified SANITIZE method to convert 
    all non-Standard quality score encoding schemes to Standard. Fixed issue 
    with validation stringency not being propagated.
  - SamAlignmentMerger: Moved the test for duplicate @PG.IDs into 
    AbstractAlignmentMerger to avoid opening the unmapped SAM file twice.
  - SamToFastq: Removed redundant IOUtil.openFileForWriting() calls for the 
    fastq writers.
  - CommandLineProgram: Bugfix - the validation stringency command line 
    option is now passed to the sam reader factory
- HTSJDK:
  - Significant work was done towards making HTSJDK compatible with 
    maven-based repositories such as Maven Central and Sonatype.
  - VCFContigHeaderLine: Fixed bug in setSequenceDictionary where where 
    the assembly value of the updated contigs was not being set properly 
    in the VCF header.
  - Fixed a bug in VCFUtils.smartMergeHeaders related to contig ordering.
  - Made some useful additions to SAMTestUtil
  - In build.xml, changed htsjdk.version.property.xml to 
    htsjdk.version.properties. See https://github.com/samtools/htsjdk/issues/99
  - Replaced use of TestNG in SAMTestUtil.
  - Only return the first error when validating a SAMRecord using STRICT, 
    for increased performance.
  - Added CustomReaderFactory for plugging in external implementations of 
    SamReader capable of getting data from APIs such as Google Genomics.
  - QualityEncodingDetector: Add the option of using original quality scores 
    for determining the encoding scheme.
  - Introduced several fixes related to JDK8 in SamFileHeaderMergerTest
  - SamPairUtil: Added methods to help set mate cigars and mate information 
    given a queryname sorted iterator.  This is useful when we want to fix 
    or update the mate information, including the mate cigar.
  - IOUtil: Added methods to check for readability/writability of list of files
  - Added copyrights to some recently added classes
  - IntervalList: No longer enforce by default that intervals that will be 
    merged have the same strand
  - SamReaderFactory: Exposed a way to set the default validation stringency

* Thu Aug 27 2014 Shane Sturrock <shane@biomatters.com> - 1.119-1
- Updated AbstractOpticalDuplicateFinder to handle post-CASAVA 1.8 read
  names. Pass READ_NAME_REGEX=null to skip optical duplicate detection
  in MarkDuplicates.
- Fixed RevertSam to harmonize different quality score encoding schemes
  when the sanitize option is set.
- Modified Casava18ReadNameEncoder to correctly display filter status.
- SamPairUtil: Added the ability to set the mate cigar tag on
  supplementary alignments. Updated AbstractAlignmentMerger to set mate
  cigars when merging supplementary alignments.
- CollectWgsMetrics: Added 2 new metrics- the fraction of bases
  attaining 15X and 25X coverage respectively.
- Added a new tool, CollectBaseDistributionByCycle, that computes the
  nucleotide distribution per cycle.
- FileAppendStreamLRUCache: Added wrapping of FileOutputStreams with
  BufferedOutputStreams.
- Fixed a bug in BCF2Writer where it was double-closing the output
  stream.
- Fixed VariantContext to ignore symbolic alleles when running strict
  validation for a VCF.
- MetricsBase: Fixed a NullPointerException
- IndexStreamBuffer: Fixed a bug in which a data-exhaustion error was
  being thrown prematurely.

* Thu Jul 31 2014 Shane Sturrock <shane@biomatters.com> - 1.118-1
- Support for the 0x800 supplementary alignment flag within Picard. Tools 
  which previously only processed primary and ignored secondary alignments 
  will now ignore secondary and supplementary. MergeBamAlignment will pass 
  supplementary alignments along in the output BAM.
- Various changes have been made so that Picard programs and libraries will 
  work properly with Java 7.  However, Picard will continue to be compiled 
  with Java 6.
- Added funcitonality to .bcl-reading command line programs 
  (IlluminaBasecallsToSam, IlluminaBasecallsToFastq, and 
  ExtractIlluminaBarcodes) to better handle qualities less than 2 via 
  BclQualityEvaluationStrategy.  When an application encounters such a 
  quality score, it used to throw an exception immediately; now, it will 
  convert write a quality 1 to the underlying file (bam, fastq, etc.), and 
  at the end of reading the BCLs, it may or may not throw an exception 
  depending on the strictness of the BclQualityEvaluationStrategy.  It will 
  always log a warning message if a quality is encountered, regardless of 
  whether or not an exception is thrown.  By default the minimum acceptable 
  quality score is still 2, but it may be controlled via the command-line 
  option MINIMUM_QUALITY.
- Performance improvements for VCF I/O.
  - Deprecated AsciiLineReader; instead, use 
    LineReaderUtil.fromBufferedStream().  
  - Added new BufferedReader-like class, LongLineBufferedReader, with 
    performance improvements for longer-lined files.
  - Added an asynchronous line reader, AsynchronousLineReader, which 
    offloads the work of parsing lines into another thread.
- Configure Picard-public so that (1) IntelliJ and ant compile to different 
  places and (2) IntelliJ ignores all of the ant compile locations (so that, 
  for example, it does see all the ant .class files and think they are part 
  of the source).  This should prevent ant builds from having an effect on 
  how IntelliJ operates.

* Mon May 26 2014 Sidney Markowitz <sidney@biomatters.com> - 1.114-1
- Complete reorganization of packages.  Map of old to new package names is
  forthcoming, but the basic change is "net.sf.samtools" => "htsjdk.samtools"
  and "net.sf.picard" => "picard."
- Enable CollectTargetedPcrMetrics and CalculateHsMetrics to target multiple baitsets.
  - Both command line programs TARGET_INTERVALS argument accept multiple values.
  - CalculateHsMetrics's BAIT_INTERVALS accepts multiple values.
- Add new modes to IntervalListTools.
  - INTERVAL_SUBDIVISION, which is the default mode, and functions
    like the previous version of IntervalListTools.
  - BALANCING_WITHOUT_INTERVAL_SUBDIVISION, which emits interval lists
    without splitting them up, and sizes the output interval list sizes
    to be no smaller than the largest input interval.
- Added an ASSUME_SORTED flag to FixMateInformation to allow grouped reads
  to be analyzed directly without prior sorting.
- IlluminaBasecallsConverter: Flush sorting collections when a barcode
  within a tile has completed to avoid running out of memory
- Add SamReaderFactory as a new facility for reading from SAM files.
  - Produces SamReader objects, which are similar to SAMFileReader.
  - Deprecate SAMFileReader, as SamReaderFactory is the preferred approach to
    creating things that read SAMs.  SAMFileReader still functions as normal.
  - See SamReaderFactory's javadoc for examples of how to use it.

* Wed May 09 2014 Shane Sturrock <shane@biomatters.com> - 1.113-1
- SecondaryAlignmentFilter.java: Addition of a simple SamRecordFilter that 
  filters out secondary alignments but not supplementary records.
- Changes to SamLocusIterator to a) check the mapping quality only once per 
  sam record instead of at every base and b) add the ability to filter out 
  non-PF reads during pileup construction.
- First version of CollectWgsMetrics a program that calculates metrics for 
  evaluating whole genome shotgun sequencing experiments.
- RevertOriginalBaseQualitiesAndAddMateCigar.java: do not check for OQ when 
  we are not reverting OQs.
- VariantContextWriterBuilder.java: Require a reference dictionary for 
  Tribble index-on-the-fly but not Tabix.
- Defaults.java: adding a reference fasta to the Defaults to facilitate 
  CRAM reading/writing.
- VCFEncoder.java: Make two methods public so Hadoop-BAM can use them.
- New program ReplaceSamHeader.
- New program AddCommentsToBam.
- Optimize Illumina BCL reading.
- Fix for CheckIlluminaDirectory when the number of clusters is different 
  per tile.

* Wed Apr 23 2014 Shane Sturrock <shane@biomatters.com> - 1.112-1
- AbstractVCFCodec.java: Add ability to remap sample names for single-sample 
  vcfs to the vcf codec.
  By calling setRemappedSampleName() on an instance of a vcf codec, you 
  instruct it to replace the existing sample name in the vcf header with a 
  new value. Attempting to use this feature with multi-sample or sites-only 
  vcfs throws an error.
- Make TextTagCodec.java and TagValueAndUnsignedArrayFlag.java public
- Move BLOCK_COMPRESSED_EXTENSIONS to Tribble so all projects use the same 
  set of extensions.
- Create Tabix indices for block-compressed VCFs
- Deprecate VariantContextWriterFactory. Convert uses of 
  VariantContextWriterFactory to VariantContextWriterBuilder.

* Wed Apr 09 2014 Shane Sturrock <shane@biomatters.com> - 1.111-1
- Added more possible actions to IntervalListTools, these actions are also 
  supported by a richer IntervalList class. 
- CommandLineParser.java: Better helpdoc from enums.
- First implementation of a rapid-gather tool for BAM files (GatherBamFiles).
- Added flag to CheckIlluminaDirectory to have it create symlinks to the 
  single X Ten locs file for each tile.
- IntervalList.java: Concatenate only unique names when merging intervals.
- LineReader.java: made LineReader @closeable
- IndexFactory.java: Tabix indices are block-compressed files
- SAMTag.java: Add BC tag
- Speed up adapter-finding code, which is used in
  IlluminaBasecallsToSam, IlluminaBasecallsToFastq, and
  MarkIlluminaAdapters.  By default, adapter sequences will be truncated
  at 30 characters, and any adapter pairs that become duplicates as a
  result are folded together.  After 100 adapters have been identified
  in reads, the list of adapter candidates is pruned down to the one
  adapter pair that was most frequent among the 100 reads with adapter
  sequence found.  In small tests, this has reduced
  IlluminaBasecallsToSam execution time by about 40%.  Moreover, since
  in most cases an Illumina lane uses only one adapter pair, pruning the
  list down to one pair reduces the chance that a read will be
  incorrectly marked with an adapter pair that was not used in the lane.
  Note that for IlluminaBasecallsToSam and IlluminaBasecallsToFastq,
  there is no control over the configuration of this functionality.
  However, MarkIlluminaAdapters has new command-line options that
  control all of the above behavior.  
- release script no longer copies /picard/trunk to /picard/branches
- VariantContextWriterFactory.java: Add .gzip to BLOCK_COMPRESSED_EXTENSIONS
- CloseableIterator.java: Implement `Closeable` to facilitate 
  try-with-resources in Java 7+ projects that depend on picard.
- CheckIlluminaDirectory.java: Create lane directories for symlinks if they 
  don't exist.
- Merged nh_mate_cigar_refactoring r1775:r1889 into trunk
- VCFCompoundHeaderLine.java: Added support for VCFv4.2 Version tags in 
  header fields.
- New VariantContextWriterBuilder class and tests
- setting ADD_MATE_CIGAR to default to true in FixMateInformation and 
  MergeBamAlignment.

* Fri Mar 28 2014 Shane Sturrock <shane@biomatters.com> - 1.110-1
- NB: Buffering has been added to most file I/O.  Buffer size is controlled
  globally, by passing -Dsamjdk.buffer_size=<desired-size> to the java
  command line.  Note that the desired size must be a number of bytes, e.g.
  if 1 megabyte is desired, then the command-line option should be
  -Dsamjdk.buffer_size=1048576.  The default buffer size is 128K.  For
  software developers using SAM-JDK, buffering in general buffering is not
  added to I/O where the caller provides an InputStream or OutputStream.  It
  is assumed that the caller has decided whether or not buffering is
  appropriate.  The one exception is SAMFileReader, which is always buffered.
  Please let us know if there are places in the code that are still not
  buffered that you think should be.

- Make sure that SAM, BAM, VCF, BCF reading and writing are buffered where
  appropriate, and also that things will not fall over when
  -Dsamjdk.buffer_size=0

- Add buffering when using Snappy for temporary file I/O.

- Add support for reading, writing and on-the-fly creation of Tabix indices
  in tribble library.  Now one can request on-the-fly indexing when using
  VariantContextWriterFactory to create a block-compressed VCF.  In addition,
  lots of clean-up of the Tribble APIs.

- Fix recently-introduced bug in which SAMFileReader.query was not finding
  unmapped reads that had the coordinate of the mapped mate.

- SamPairUtil.java: Revert changes in `SamPairUtil#setMateInfo()` which
  introduced setting of the mate cigar string.

- TribbleIndexedFeatureReader.java: Lazy-load index file.

- Small change to allow MakeSitesOnlyVcf retain genotypes for one or more
  samples.  In this mode all annotations are retained from the full file as
  if making a sites only file - not recomputed from the retained samples.

- Address bugs with `ExtractIlluminaBarcodes`.  
  - Resolve hang that occured when `ExtractIlluminaBarcodes` encounters an
    exception in `main` before it finishes submitting all runnables to thread
    pool.  
  - Resolve state exception that occurs processing gzipped BCLs with buffered
    inputs.

- Add support for handling phasing metrics from the TileMetricsOut.bin file

- Adding ATTRIBUTES_TO_REMOVE option to MergeBamAlignment, so we can remove
  attributes from the incoming alignments.  This option will override
  ATTRIBUTES_TO_RETAIN when the conflict.

- Gracefully handle scenario in `MergeBamAlignment` in which a record is
  mapped completely off the end of the reference by making it unmapped.

- Added SamFileTester to facilitate creation and testing of "on the fly" SAM
  files. (examples included in CleanSamTest and MarkDuplicatesTest)

- Added the ability to pass an expected quality format to
  QualityEncodingDetector

- Bug fix: `AsynchronousLineReader` fails to propagate worker thread errors
  that aren't `Exception`s.

- moving SamPairUtil from net.sf.picard.sam to net.sf.samtools since
  SAMRecordSetBuilder depends on it

- SamFileValidator now has a method with no expected base quality format

- default quality format now enabled in ValidateSamFile

- Added flag to IlluminaBasecallsTo[Sam|Fastq] to include non-PF reads.  The
  default is true.

- Minor changes that improve the runtime of IlluminaBasecallsToSam.

- Added file faking and per tile filtering to CheckIlluminaDirectory.

- Changed to ValidateSamFile to not allow specification of quality format as
  the spec only allows a single valid quality encoding.

* Wed Mar 12 2014 Shane Sturrock <shane@biomatters.com> - 1.109-1
- Add buffering for BAM file writing.  By default this will be 128K.  Buffer 
  size can be controlled via -Dsamjdk.buffer_size=<value>.  Buffer size can 
  be controlled programmatically via SAMFileWriterFactory.setBufferSize() 
  method.
- Added MateCigar to SAMRecord as an optional Attribute ("MC")
  - Given a SAMRecord that is part of a pair, the MateCigar attribute (MC) 
    will contain the cigar string for that read's mate iff the mate is mapped.
  - Added getters (for String and Cigar) to SAMRecord.
  - Moved utility methods (getClippedAlignmentStart/End...) to SAMRecord and 
    commonified with similar methods for the Read itself.
  - Added validations to MateCigar (not present when inappropriate, matches 
    the Mate's Cigar String).
- Added the command line tool RevertOriginalBaseQualitiesAndAddMateCigar
  - meant to update a SAM/BAM to include the new Mate Cigar ("MC") optional tag.
  - additionally, allows the user to optionally revert the original base 
    qualities ("OQ" optional tag).
  - will exit early with an INFO message if the SAM/BAM already has the "MC" 
    tag, and therefore would not need to be reverted.
- MergeBamAlignment, CleanSam, RevertOriginalBaseQualitiesAndAddMateCigar: Make 
  sure that the mate CIGAR (MC) does not hang off the end of the reference.  
  If it does, clip it, the same way we do with the record's CIGAR.
- SortSam, MergeBamAlignment: Adding logging to record progress while writing 
  SAM records to disk when sorting.
- AbstractAsyncWriter.java: Handle case in which exception in writer thread is 
  not detected because queuing thread is already blocking on full queue before 
  exception occurs.
- SAMHeaderRecordComparator.java: Adding a checksum generation method for SAM 
  RG records

* Wed Feb 26 2014 Shane Sturrock <shane@biomatters.com> - 1.108-1
- Handle mix of paired and unpaired reads in MarkIlluminaAdapters, 
  MergeBamAlignment and SamToFastq.
  - Deprecated "is paired" argument in MergeBamAlignment.
  - Added "unpaired record output" argument to `SamToFastq`, which emits 
    unpaired reads to its own fastq, if set.
- Support Illumina RTA2 (i.e. NextSeq) format for all programs that use 
  IlluminaDataProviderFactory, i.e. IlluminaBasecallsToSam, 
  IlluminaBasecallsToFastq, ExtractIlluminaBarcodes, CheckIlluminaDirectory.
- Implement async I/O for writing bgzipped VCFs.  This can be enable 
  programmatically, or by passing -Dsamjdk.use_async_io=true to the java 
  command.
- BasicFastqWriter.java: Use BufferedOutputStream.  Buffer size is controlled 
  by system property samjdk.buffer_size.
- BlockCompressedInputStream.java: By default BlockCompressedInputStream wants 
  to ensure that the InputStream it is wrapping is buffered, by buffering if 
  necessary.  For certain operations it's critical that buffering not be added, 
  so added new constructor that allows the caller to force no buffering.
- libIntelDeflater.so: Mark library as not requiring executable stack.  
  Hopefully this will eliminate warnings that have been reported by some 
  users.
- Improved MarkIlluminaAdapters to clip for multiple different adapter 
  sequences in one pass and correct progress logging and metrics that were 
  only counting one read out of each pair.
- Minor change so that VCFFileReader.getSequenceDictionary() does not require 
  the VCF to be indexed.
- Changed so that the VCFReader doesn't require the presence of an index since 
  MakeSitesOnlyVcf doesn't use it anyway.
- TabixUtils.java: Added utility code to pull out the sequence dictionary from 
  a tabix index file.  Useful for quickly validating consistency of the 
  sequence dictionary.
- VariantContext.java, AbstractVCFCodec.java: Fixed a race condition causing 
  occasional errors in AD and PL fields in multithreaded mode.  Removed the 
  side-effect of decoding genotypes when calling VariantContext.toString().
- VariantContextWriterFactory.java: Identify extensions .gz, .bgz, .bgzf as 
  block-compressed vcf when writing VCF.  Add methods to create vcf, bcf, and 
  block-compressed vcf explicitly as an alternative to determining format by 
  examining file extension.
- Fixed BCF2Utils.toList() to account for the possibility that the input may 
  be an array.
- VariantContext.java: Muliple alt alleles were being returned in arbitrary 
  order from subContextFromSamples.  This change ensures original order.
- VcfFormatConverter.java: Changed the way the CREATE_INDEX option is handled 
  so that it is additive to the DEFAULT_OPTIONS and does not wipe out other 
  default options for VCF writing.
- Changed the way MakeSitesOnlyVcf handles index creation options so that it 
  respects other default VCF writing options.
- Added a new pair of options to RevertSam to allow for "Sanitizing" SAM and 
  BAM files during revert operations.  When fully reverting and sorting by 
  query mode this will optionally discard reads who's pairing information is 
  non-sensical including: a) paired reads who's mates are not present in the 
  file, b) non-paired reads that are duplicated in the file and c) reads 
  marked as paired by not having a single R1 and R2 present.
- IntervalListTools.java: Require at least one input file

* Wed Jan 29 2014 Shane Sturrock <shane@biomatters.com> - 1.107-1
- Build javadoc for variant and tribble packages as part of sourceforge 
  release.
- Fix annoying bug where in order to use SamLocusIterator as an iterator one 
  first had to call the .iterator() method on it to prime it.  Now auto-primes.
- Support writing of vcf.gz, i.e. bgzf format, but only without on-the-fly 
  index creation.
- Set buffer size of BclReader to Defaults.BUFFER_SIZE, which defaults to 
  128K and can be controlled via -Dsamjdk.buffer_size=<buffer_size>.  Previous 
  size was always 8192.
- Added nominal support for VCF4.2 headers (but just the headers)
* Wed Jan 15 2014 Shane Sturrock <shane@biomatters.com> - 1.106-1
- Added new SAMFileReader.query method that enables querying of
  multiple intervals in a single invocation.  In many cases this will be
  much more efficient than querying each interval separately, because
  due to the limitations of BAM index a query can result in many records
  read from the file that do not satisfy the query parameters.  In
  multiple query invocations, the same regions of the file may be read
  more than once, whereas with the new method each candidate region of
  the file will be read only once.
- SamLocusIterator now uses this method.  It used to be the case that
  for some inputs, having SamLocusIterator use an index was less
  efficient than a linear scan through the whole file.  It should now be
  the case that using the index will always be at least as efficient as
  a linear scan, and generally using the index will be much more
  efficient.
- Added support for processing reads with hard clips in
  MergeBamAlignment.  Implemented by transforming the hard clips to soft
  clips and adding in dummy bases and qualities when reading the aligned
  reads into memory.  This should addressed problems processing BWA MEM
  output with MergeBamAlignment.
- Fixed the handling of supplemental alignments in MergeBamAlignment.
  Previous implementation was incorrect in assuming that when reads are
  paired that each end of a pair would have the same number of
  supplemental alignments.
- PedFile.java: Conditionally allow for tabs in ped file fields
- VariantContext.java: Fixed bad 'equals' bug in VC validation where
  Integer != Integer was always returning true
- MarkDuplicates.java: Avoid asking for an array bigger than JVM
  allows if heap is huge.
- Fixed up docs for VC and Allele and added a method to remove a list
  of attributes for the VCBuilder.
- AbstractVCFCodec.java: Instead of failing badly on format field
  lists with '.'s, just ignore them.
- SamAlignmentMerger.java: Changed the iterator returned by
  getQuerynameSortedAlignedRecords() to return a header with
  SortOrder.queryname instead of coordinate.  Also added a warning log
  when SamAlignmentMerger decides it needs to re-sort the aligned reads
  into queryname order.
- BCF2FieldEncoder.java: Add BCF encoding support for Java arrays, not
  just lists.
- Fix CleanSam to handle unusual Cigar strings, and also so that it no
longer clips 1 more than necessary.
- SAMFileHeader.java: Treat SO:unknown as if it were SO:unsorted.
- Support .fna and .fna.gz as valid extensions for fasta files.

* Wed Dec 18 2013 Shane Sturrock <shane@biomatters.com> - 1.105-1
- IOUtil.java: Reverse order of two conditions in order to avoid calling 
  File.getUsableSpace for the last temp directory in the list.
- MathUtil.java: Added a method to create sequences of doubles.

* Wed Dec 04 2013 Shane Sturrock <shane@biomatters.com> - 1.104-1
- Use Intel hardware-accelerated Deflater for writing BAM files where 
  appropriate.  This is only supported on unix systems.  
  net.sf.samtools.util.zip.IntelDeflater is used instead of 
  java.util.zip.Deflater. See
  https://sourceforge.net/apps/mediawiki/picard/index.php?title=IntelDeflater
  In order to use IntelDeflater, a shared library libIntelDeflater.so must be 
  dynamically loaded.  This library is included in the picard-tools zipfile.  
  The shared library is found via one of the following methods:
  If -Dsamjdk.intel_deflater_so_path is set and points to the shared library, 
  it is loaded from that location.
  Else if the shared library is in the same directory as the Picard jar that 
  is executing, it is loaded from that location.  We presume that this will be 
  the typical way in which the shared library will be found.
  Else if the shared library is found on LD_LIBRARY_PATH, it is loaded from 
  there.
  Else java.util.zip.Deflater is used.
  Use of IntelDeflater may be suppressed with
  -Dsamjdk.try_use_intel_deflater=false.
  In the header line written by Picard command-line programs, at the end of 
  the line will appear either IntelDeflater or JdkDeflater to indicate which 
  has been loaded.
  We have seen compression time reduced by 13% to 33% depending on the hardware.
- Tribble.java: More intelligent determination of index file path; Treat URLs 
  with query strings properly, add index extension to the path element not 
  just the end of the string
- Have TabixReader use buffered seekable streams.
- Allow TabixReader to take an index file as an input parameter, instead of 
  just adding an extension. This is necessary for URLs with query parameters.
- Added a capacity to conditionally ignore blank lines in the fastq files.
- Setting the output read structure properly on IlluminaBasecallsToFastq when 
  there are skips.
- Improved assertion error messages in
  `SAMSequenceDictionary#assertSameDictionary(SAMSequenceDictionary)`.
- MultiLevelCollector.java: Handling missing read groups when requesting 
  accumulation at level that requires read group.
- Fix multi-threading bug in ExtractIlluminaBarcodes caused some metrics to 
  accumulate incorrectly.
* Wed Nov 20 2013 Shane Sturrock <shane@biomatters.com> - 1.103-1
- Optionally compute MD5 on the fly when writing FASTQ in 
  IlluminaBasecallsToFastq and SamToFastq, and write to companion file.
- For VCF and BCF writing, allow the caller to provide an IndexCreator 
  instead of using the default.
- Do not return non-zero exit status in SamToFastq if unmatched mates 
  found and validation_stringency is not STRICT.
* Wed Nov 06 2013 Shane Sturrock <shane@biomatters.com> - 1.102-1
- Changed default read name header formatting for fastq records emitted by 
  `IlluminaBasecallsToFastq` to include new values and, in particular, 
  passing-filter flags.  The old read name header formatting is referred to as 
  "Illumina," and the new formatting "Casava 1.8".  This change necessitated 
  adding two new required (by default) arguments: FLOWCELL_BARCODE and 
  MACHINE_NAME.
  You may control the formatting emitted by IlluminaBasecallsToFastq with the 
  `READ_NAME_FORMAT` argument.  (For example, pass READ_NAME_FORMAT=ILLUMINA 
  to emulate default functionality prior to this commit.)
- ValidateSamFile.java: Do not check file termination if reading from a pipe.
- Separating the VCF encoding functions from the VCFWriter class.
- Change SeekableStreamFactory to a singleton.
  Allow an application to set the implementation of SeekableStreamFactory. 
  Default implementation is the same.
- Moved `VariantContextUtil`'s `calcVCFGenotypeKeys` and a field member into 
  `VariantContext` to avoid referencing `VariantContextUtils` in some 
  command-line programs.  Referencing `VariantContextUtils` can cause 
  `ClassInitializationException`s because it references jexl packages which 
  do dynamic class-loading.  This is more of a band-aid than a fix.
- MakeSitesOnlyVcf.java: Bug fix: do not call `VCFHeader` constructor that 
  copies sample names, since that forces the writer to emit genotype data for 
  those samples (which fails the requirements of a site-only VCF).
* Wed Oct 23 2013 Shane Sturrock <shane@biomatters.com> - 1.101-1
- explain_sam_flags.py: Add 0x800 (supplementary alignment) flag.
- LongLineBufferedReader.java: Fix copyright message.
- PedFile.java: Implementation of a simple ped-file parser and writer for PED files that contain family/pheno information 
  but no genotypes.
- MathUtil.java: Added a couple of methods for 1) doing vector multiplication of two arrays and b) summing values in an 
  array.
- VCFFileReader.java: Tidied up a little bit and then added a method to be able to query by region from the VCFFileReader.

* Wed Oct 09 2013 Shane Sturrock <shane@biomatters.com> - 1.100-1
- explain_sam_flags.py: Add 0x800 (supplementary alignment) flag.
- Updated IterableIterator to IterableOnceIterator that throws an exception if multiple calls to iterator() are made.
- rnaSeqCoverage.R: When there are duplicate headers in the metrics file don't try to generate a PDF as it will crash and burn
* Wed Sep 25 2013 Shane Sturrock <shane@biomatters.com> - 1.99-1
- Implementing an easier-to-use VCF file reader API.
- Adding an option to not require indexes on VcfFormatConverter.
- SAMFileReader.java: Modify SAMFileReader.streamLooksLikeBam to accept URL.
- MakeSitesOnlyVcf.java: Bug fix: if SEQUENCE_DICTIONARY is null, NullPointerException is necessarily thrown.
- ReadNameFilter.java: eliminate Scanner class usage to reduce memory footprint.
* Wed Sep 11 2013 Shane Sturrock <shane@biomatters.com> - 1.98-1
- MarkDuplicates and EstimateLibraryComplexity: In usage message, clarify that optimization is done instead of applying default 
  regex.  Clarify that read name regex must match entire read name.
- AddOrReplaceReadGroups.java: added predicted insert size option.
- ProcessExecutor.java: Add methods for executing a command, interleaving stdout and stderr, and return exit status in addition 
  to command output.

* Wed Aug 28 2013 Shane Sturrock <shane@biomatters.com> - 1.97-1
- Requires Java 6.  Added new MarkIlluminaAdapters program and various bug fixes

* Wed Jul 31 2013 Shane Sturrock <shane@biomatters.com> - 1.96-1
- New upstream release

* Wed Jul 17 2013 Shane Sturrock <shane@biomatters.com> - 1.95-1
- New upstream release

* Wed Jul 03 2013 Shane Sturrock <shane@biomatters.com> - 1.94-1
- New upstream release

* Wed Jun 26 2013 Shane Sturrock <shane@biomatters.com> - 1.93-1
- New upstream release

* Wed May 22 2013 Simon Buxton <simon@biomatters.com> - 1.92-1
- New upstream release

* Wed May 08 2013 Shane Sturrock <shane@biomatters.com> - 1.91-1
- New upstream release

* Wed Apr 24 2013 Shane Sturrock <shane@biomatters.com> - 1.90-1
- New upstream release

* Fri Apr 12 2013 Simon Buxton <simon@biomatters.com> - 1.89-1
- New upstream release

* Wed Mar 27 2013 Shane Sturrock <shane@biomatters.com> - 1.88-1
- New upstream release

* Mon Mar 18 2013 Shane Sturrock <shane@biomatters.com> - 1.87-1
- New upstream release

* Mon Mar 04 2013 Shane Sturrock <shane@biomatters.com> - 1.86-1
- New upstream release

* Mon Feb 11 2013 Carl Jones <carl@biomatters.com> - 1.85-1
- New upstream release

* Wed Jan 15 2013 Carl Jones <carl@biomatters.com> - 1.84-1
- New upstream release

* Tue Jan 08 2013 Carl Jones <carl@biomatters.com> - 1.83-1
- New upstream release

* Thu Dec 20 2012 Carl Jones <carl@biomatters.com> - 1.82-1
- New upstream release

* Wed Dec 05 2012 Carl Jones <carl@biomatters.com> - 1.81-1
- New upstream release
* Thu Nov 22 2012 Carl Jones <carl@biomatters.com> - 1.80-1
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 1.79-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 1.77-1
- New upstream release

* Wed Aug 01 2012 Carl Jones <carl@biomatters.com> - 1.74-1
- Rename package to picard
- Bump to 1.74

* Tue Aug 23 2011 Adam Huffman <bloch@verdurin.com> - 1.50-2
- change to picard-tools-bin

* Thu Aug 11 2011 Adam Huffman <bloch@verdurin.com> - 1.50-1
- initial version

