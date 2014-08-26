Name:		picard
Version:	1.119
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

