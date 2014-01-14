Name:		picard
Version:	1.106
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

mv ../snappy-java-1.0.3-rc3.jar .

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_javadir}/%{name}

cp *.jar %{buildroot}%{_javadir}/%{name}

cp snappy-java-1.0.3-rc3.jar %{buildroot}%{_javadir}/%{name}

mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)

%{_javadir}/%{name}/*

%changelog
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

