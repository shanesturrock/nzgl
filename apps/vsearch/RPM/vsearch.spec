Name:		vsearch
Version:	2.1.1
Release:	1%{?dist}
Summary:	An alternative to the USEARCH
Group:		Applications/Engineering
License:	GPL3
URL:		https://github.com/torognes/vsearch
Source0: 	vsearch-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	autogen,automake,autoconf

%description
VSEARCH stands for vectorized search, as the tool takes advantage of
parallelism in the form of SIMD vectorization as well as multiple threads to
perform accurate alignments at high speed. VSEARCH uses an optimal global
aligner (full dynamic programming Needleman-Wunsch), in contrast to USEARCH
which by default uses a heuristic seed and extend aligner. This results in more
accurate alignments and overall improved sensitivity (recall) with VSEARCH,
especially for alignments with gaps.

%prep
%setup -q

%build
./autogen.sh
./configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 bin/vsearch %{buildroot}%{_bindir}
install -m 0644 man/vsearch.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/vsearch
%{_mandir}/man1/vsearch.1*

%changelog
* Mon Sep 26 2016 Shane Sturrock <shane@biomatters.com> - 2.1.1-1
- Fixed bugs in UC-output from clustering, updated docs.

* Mon Sep 19 2016 Shane Sturrock <shane@biomatters.com> - 2.1.0-1
- Added fastx_filter command and options fastq_truncee and fastq_maxlen.
- Allowed minwordmatches down to 3.

* Mon Sep 12 2016 Shane Sturrock <shane@biomatters.com> - 2.0.5-1
- Added options to output discarded sequences from subsampling to separate
  files. 
- Updated manual.

* Mon Sep 05 2016 Shane Sturrock <shane@biomatters.com> - 2.0.4-1
- Improved manual and one error message.

* Thu Aug 04 2016 Shane Sturrock <shane@biomatters.com> - 2.0.3-1
- Fix Illegal instruction faults when running the precompiled binaries on some
  systems.

* Wed Jul 06 2016 Shane Sturrock <shane@biomatters.com> - 2.0.2-1
- Fix GCC version 6 warnings.

* Fri Jul 01 2016 Shane Sturrock <shane@biomatters.com> - 2.0.1-1
- Fix segmentation fault when masking very long sequences, due to use of 
  alloca.

* Mon Jun 27 2016 Shane Sturrock <shane@biomatters.com> - 2.0.0-1
- Support for reading from and writing to pipes.

* Wed Jun 22 2016 Shane Sturrock <shane@biomatters.com> - 1.11.2-1
- Fixed issues relating to query_cov option and to consensus sequences with Ns.

* Thu Apr 14 2016 Shane Sturrock <shane@biomatters.com> - 1.11.1-1
- Add strand info to uc file after dereplication.
- Add info about expected errors (ee) to FASTA files with fastq_filter and
  fastq_mergepairs commands if option -fastq_eeout or -eeout is specified. 
- Delete unnecessary autotool files.

* Mon Mar 21 2016 Shane Sturrock <shane@biomatters.com> - 1.10.2-1
- Fixed a bug causing a segmentation fault when running usearch_global with an
  empty query sequence. 
- Also fixed a bug causing imperfect alignments to be reported with an
  alignment string of "=" in uc output files. 
- Fixed typos in man file. 
- Fixed fasta/fastq processing code regarding presence or absence of
  compression library header files.

* Fri Feb 26 2016 Shane Sturrock <shane@biomatters.com> - 1.10.1-1
- Fix truncated labels for fastq_mergepairs command

* Tue Feb 16 2016 Sidney Markowitz <sidney@biomatters.com> - 1.10.0-1
- Parallelize and improve merging of paired-end reads and adjust some defaults
- Remove progress indicator when stderr is not a terminal
- Add --fasta_score option to report chimera scores in FASTA files.
- Add rereplicate and fastq_eestats commands.
- Fix typos.
- Add relabelling to files produced with --consout and --profile options.

* Wed Jan 27 2016 Shane Sturrock <shane@biomatters.com> - 1.9.10-1
- This version fixes bugs with DUST-masking and lower case database sequences.
  Lower case sequences were masked even when DUST masking was specified for the
  database sequences. During debugging it was detected that DUST-masking of
  database sequences probably have not occurred at all. Both problems fixed.

* Mon Jan 25 2016 Shane Sturrock <shane@biomatters.com> - 1.9.9-1
- Fixes bug causing segfault when chimera detection is performed on extremely
  short sequences.
- Adjusted default min word matches for improved performance.

* Thu Jan 14 2016 Shane Sturrock <shane@biomatters.com> - 1.9.7-1
- Masking behavior is changed somewhat to keep the letter case of the input
  sequences unchanged when no masking is performed. Masking is now performed
  also during chimera detection. Documentation updated.

* Mon Jan 11 2016 Shane Sturrock <shane@biomatters.com> - 1.9.6-1
- Should fix bug in aligned sequences produced with --fastapairs and --userout
  (qrow, trow) options 

* Mon Dec 07 2015 Shane Sturrock <shane@biomatters.com> - 1.9.5-1
- Fixed bug resulting in inferior chimera detection performance.

* Fri Dec 04 2015 Shane Sturrock <shane@biomatters.com> - 1.9.4-1
- Fixed incrementation of counter when relabeling dereplicated sequences.

* Fri Nov 20 2015 Shane Sturrock <shane@biomatters.com> - 1.9.3-1
- Workaround for missing x86intrin.h with old compilers

* Wed Nov 18 2015 Shane Sturrock <shane@biomatters.com> - 1.9.2-1
- Fixed a bug in computation of some values with --fastq_stats.

* Mon Nov 16 2015 Shane Sturrock <shane@biomatters.com> - 1.9.1-1
- Fixed memory leak and a bug in score computation in fastq_mergepairs, and
  improved speed.

* Fri Nov 13 2015 Shane Sturrock <shane@biomatters.com> - 1.9.0-1
- Added the --fastq_mergepairs command and associated options. This command has
  not been tested well yet.
- Included additional files to avoid dependency of autoconf for compilation. 
- Fixed an error where identifiers in fasta headers where not truncated at
  tabs, just spaces. 
- Fixed a bug in detection of the file format (FASTA/FASTQ) of a gzip
  compressed input file.

* Wed Nov 04 2015 Shane Sturrock <shane@biomatters.com> - 1.8.1-1
- This release fixes some compatibility issues with older OS X versions as well
  as with QIIME and usearch61.
  - OS X version 10.7 and newer should now be properly supported. 
  - The --threads option will now accept floating point arguments for
    compatibility with usearch61 and QIIME (specifically
    identify_chimeric_seqs.py).

* Wed Oct 21 2015 Shane Sturrock <shane@biomatters.com> - 1.8.0-1
- Added --search_exact, --fastx_mask and --fastq_convert commands. 
- Changed most commands to read FASTQ input files as well as FASTA files. 
- Modified --fastx_revcomp and --fastx_subsample to also write FASTQ files.

* Mon Oct 19 2015 Shane Sturrock <shane@biomatters.com> - 1.7.0-1
- Added relabel_keep option

* Mon Oct 12 2015 Shane Sturrock <shane@biomatters.com> - 1.6.0-1
- Added relabelling options for shuffle and added xsize option for several
  commands.

* Thu Oct 08 2015 Shane Sturrock <shane@biomatters.com> - 1.5.0-1
- Initial NZGL release

