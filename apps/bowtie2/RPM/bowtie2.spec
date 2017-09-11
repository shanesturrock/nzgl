%define debug_package %{nil}

Name:		bowtie2
Version:	2.3.3
Release:	1%{?dist}
Summary:	An ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences
Group:		Applications/Engineering
License:	GPLv3
URL:		http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
Source0:	%{name}-%{version}-linux-x86_64.zip
#Patch0:         pat.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires:	readline,zlib
#BuildRequires:  readline-devel,zlib-devel

%description
Bowtie 2 is an ultrafast and memory-efficient tool for
aligning sequencing reads to long reference sequences. It is
particularly good at aligning reads of about 50 up to 100s or 1,000s
of characters, and particularly good at aligning to relatively long
(e.g. mammalian) genomes. Bowtie 2 indexes the genome with an FM Index
to keep its memory footprint small: for the human genome, its memory
footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local,
and paired-end alignment modes.

%prep
%setup -n %{name}-%{version}
#%patch0 -p0

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}

install -m 0755 bowtie2 %{buildroot}/%{_bindir}
install -m 0755 bowtie2-align-l %{buildroot}/%{_bindir}
install -m 0755 bowtie2-align-s %{buildroot}/%{_bindir}
install -m 0755 bowtie2-build %{buildroot}/%{_bindir}
install -m 0755 bowtie2-build-l %{buildroot}/%{_bindir}
install -m 0755 bowtie2-build-s %{buildroot}/%{_bindir}
install -m 0755 bowtie2-inspect %{buildroot}/%{_bindir}
install -m 0755 bowtie2-inspect-l %{buildroot}/%{_bindir}
install -m 0755 bowtie2-inspect-s %{buildroot}/%{_bindir}
cp -a scripts %{buildroot}/%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc MANUAL NEWS VERSION AUTHORS TUTORIAL doc/
%dir %{_datadir}/%{name}
%{_bindir}/bowtie2
%{_bindir}/bowtie2-align-l
%{_bindir}/bowtie2-align-s
%{_bindir}/bowtie2-build
%{_bindir}/bowtie2-build-l
%{_bindir}/bowtie2-build-s
%{_bindir}/bowtie2-inspect
%{_bindir}/bowtie2-inspect-l
%{_bindir}/bowtie2-inspect-s
#%{_datadir}/bowtie/genomes
#%{_datadir}/bowtie/indexes
#%{_datadir}/bowtie/reads
#%{_datadir}/bowtie2/scripts
%{_datadir}/%{name}

%changelog
* Tue Sep 12 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 2.3.3-1
- bowtie2-build now supports gzip-compressed FASTA inputs
- New --xeq parameter for bowtie2 disambiguates the 'M' CIGAR flag. When
  specified, matches are indicated with the = operation and mismatches with X
- Fixed a possible infinite loop during parallel index building due to the
  compiler optimizing away a loop condition
- Added --soft-clipped-unmapped-tlen parameter for bowtie2 that ignores
  soft-clipped bases when calculating template length (TLEN)
- Added support for multi-line sequences in FASTA read inputs
- Expanded explanation of MD:Z field in manual
- Fixed a crashing bug when output is redirected to a pipe
- Fixed ambiguity in the SEED alignment policy that sometimes caused -N
  parameter to be ignored

* Mon May 08 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 2.3.2-1
- Added support for interleaved paired-end FASTQ inputs (--interleaved)
- Now reports MREVERSE SAM flag for unaligned end when only one end of a pair
  aligns
- Fixed issue where first character of some read names was omitted from SAM
  output when using tabbed input formats
- Added --sam-no-qname-trunc option, which causes entire read name, including
  spaces, to be written to SAM output. This violates SAM specification, but can
  be useful in applications that immediately postprocess the SAM.
- Fixed compilation error caused by pointer comparison issue in
  aligner_result.cpp
- Removed termcap and readline dependencies introduced in v2.3.1
- Fixed compilation issues caused by gzbuffer function when compiling with zlib
  v1.2.3.5 and earlier. Users compiling against these libraries will use the
  zlib default buffer size of 8Kb when decompressing read files.
- Fixed issue that would cause Bowtie 2 hang when aligning FASTA inputs with
  more than one thread

* Fri Apr 28 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 2.3.1-1
- Added native support for gzipped read files. The wrapper script is no longer
  responsible for decompression. This simplifies the wrapper and improves speed
  and thread scalability for gzipped inputs.
- Fixed a bug that caused 'bowtie2-build' to crash when the first FASTA
  sequence contains all Ns.
- Add support for interleaved FASTQ format -—interleaved.
- Empty FASTQ inputs would yield an error in Bowtie 2 2.3.0, whereas previous
  versions would simply align 0 reads and report the SAM header as usual. This
  version returns to the pre-2.3.0 behavior, resolving a compatibility issue
  between TopHat2 and Bowtie 2 2.3.0.
- Fixed a bug whereby combining -—un-conc* with -k or -a would cause 'bowtie2'
  to print duplicate reads in one or both of the --un-conc* output files,
  causing the ends to be misaligned.
- The default ---score-min for --local mode is now 'G,20,8'. That was the
  stated default in the documentation for a while, but the actual default was
  'G,0,10' for many versions. Now the default matches the documentation and, we
  find, yields more accurate alignments than 'G,0,10'

* Mon Jan 09 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 2.3.0-1
- Code related to read parsing was completely rewritten to improve scalability
  to many threads. In short, the critical section is simpler and parses input
  reads in batches rather than one at a time. The improvement applies to all 
  read formats.
- TBB is now the default threading library. We consistently found TBB to give
  superior thread scaling. It is widely available and widely installed. That
  said, we are also preserving a "legacy" version of Bowtie that, like previous
  releases, does not use TBB. To compile Bowtie source in legacy mode use
  NO_TBB=1. To use legacy binaries, download the appropriate binary archive with
  "legacy" in the name.
- Bowtie now uses a queue-based lock rather than a spin or heavyweight lock. We
  find this gives superior thread scaling; we saw an order-of-magnitude
  throughput improvements at 120 threads in one experiment, for example.
- Unnecessary thread synchronization removed
- Fixed issue with parsing FASTA records with greater-than symbol in the name
- Now detects and reports inconsistencies between --score-min and --ma
- Changed default for --bmaxdivn to yield better memory footprint and running
  time when building an index with many threads

* Tue Apr 26 2016 Shane Sturrock <shane@biomatters.com> - 2.2.9-1
- Fixed the multiple threads issue for the bowtie2-build.
- Fixed a TBB related build issue impacting TBB v4.4.

* Tue Mar 15 2016 Shane Sturrock <shane@biomatters.com> - 2.2.8-1
- Various website updates.
- Fixed the bowtie2-build issue that made TBB compilation fail.
- Fixed the static build for Win32 platform.

* Mon Feb 15 2016 Sidney Markowitz <sidney@biomatters.com> - 2.2.7-1
- Added a parallel index build option: bowtie2-build --threads <# threads>
- Bug fix:  IUPAC codes (other than A/C/G/T/N) in reads were converted to As
  Now they are converted to Ns,
- Removed debugging code that could impede performancg in some cases
- Fixed a few typos in documentation
* Wed Aug 26 2015 Shane Sturrock <shane@biomatters.com> - 2.2.6-1
- Switched to a stable sort to avoid some potential reproducibility confusions.
- Added 'install' target for *nix platforms.
- Added the Intel TBB option which provides in most situations a better
  performance output. TBB is not present by default in the current build but
  can be added by compiling the source code with WITH_TBB=1 option.
- Fixed a bug that caused seed length to be dependent of the -L and -N
  parameters order.
- Fixed a bug that caused --local followed by -N to reset seed length to 22
  which is actually the default value for global.
- Enable compilation on FreeBSD and clang, although gmake port is still
  required.
- Fixed an issue that made bowtie2 compilation process to fail on Snow Leopard.

* Mon Mar 09 2015 Shane Sturrock <shane@biomatters.com> - 2.2.5-1
- Fixed some situations where incorrectly we could detect a Mavericks platform.
- Fixed some manual issues including some HTML bad formatting.
- Make sure the wrapper correctly identifies the platform under OSX.
- Fixed --rg/--rg-id options where included spaces were incorrectly treated.
- Various documentation fixes added by contributors.
- Fixed the incorrect behavior where parameter file names may contain spaces.
- Fixed bugs related with the presence of spaces in the path where bowtie 
  binaries are stored.
- Improved exception handling for misformatted quality values.
- Improved redundancy checks by correctly account for soft clipping.

* Fri Oct 24 2014 Shane Sturrock <shane@biomatters.com> - 2.2.4-1
- Fixed a Mavericks OSX specific bug caused by some linkage ambiguities.
- Added lz4 compression option for the wrapper.
- Fixed the vanishing --no-unal help line.
- Added the static linkage for MinGW builds.
- Added extra seed-hit output.
- Fixed missing 0-length read in fastq --passthrough output.
- Fixed an issue that would cause different output in -a mode depending on 
  random seed.

* Tue Jun 01 2014 Sidney Markowitz <sidney@biomatters.com> - 2.2.3-1
- Fixed a bug that made loading an index into memory crash sometimes.
- Fixed a silent failure to warn the user in case the -x option is missing.
- Updated al, un, al-conc and un-conc options to avoid confusion in cases
  where the user does not provide a base file name.
- Fixed a spurious assert that made bowtie2-inspect debug fail.
* Mon Apr 14 2014 Shane Sturrock <shane@biomatters.com> - 2.2.2-1
- Improved performance for cases where the reference contains ambiguous or 
  masked nucleobases represented by Ns.
* Mon Mar 03 2014 Shane Sturrock <shane@biomatters.com> - 2.2.1-1
- Improved way in which index files are loaded for alignment. Should fix 
  efficiency problems on some filesystems.
- Fixed a bug that made older systems unable to correctly deal with bowtie 
  relative symbolic links.
- Fixed a bug that, for very big indexes, could determine to determine file 
  offsets correctly.
- Fixed a bug where using --no-unal option incorrectly suppressed 
  --un/--un-conc output.
- Dropped a perl dependency that could cause problems on old systems.
- Added --no-1mm-upfront option and clarified documentation for parameters 
  governing the multiseed heuristic.
* Wed Feb 12 2014 Shane Sturrock <shane@biomatters.com> - 2.2.0-1
- Improved index querying efficiency using "population count" instructions 
  available since SSE4.2
- Added support for large and small indexes, removing 4-billion-nucleotide 
  barrier. Bowtie 2 can now be used with reference genomes of any size.
- Fixed bug that could cause bowtie2-build to crash when reference length is 
  close to 4 billion.
- Added a CL: string to the @PG SAM header to preserve information about the 
  aligner binary and paramteres.
- Fixed bug that could cause bowtie2-build to crash when reference length is 
  close to 4 billion.
- No longer releasing 32-bit binaries. Simplified manual and Makefile 
  accordingly.
- Credits to the Intel® enabling team for performance optimizations included 
  in this release. Thank you!
- Phased out CygWin support. MinGW can still be used for Windows building.
- Added the .bat generation for Windows.
- Fixed some issues with some uncommon chars in fasta files.
- Fixed wrappers so bowtie can now be used with symlinks.

* Mon Feb 25 2013 Carl Jones <carl@biomatters.com> - 2.1.0-0
- New upstream release

* Tue Jan 29 2013 Carl Jones <carl@biomatters.com> - 2.0.6-1
- New upstream release

* Tue Jan 08 2013 Carl Jones <carl@biomatters.com> - 2.0.5-1
- New upstream release

* Thu Dec 20 2012 Carl Jones <carl@biomatters.com> - 2.0.4-1
- New upstream release

* Mon Dec 17 2012 Carl Jones <carl@biomatters.com> - 2.0.3-1
- New upstream release

* Mon Nov 05 2012 Carl Jones <carl@biomatters.com> - 2.0.2-1
- New upstream release

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 2.0.0.beta7-2
- Small SPEC file tweaks for licence, description  
