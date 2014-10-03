Name:		bowtie
Version:	1.1.1
Release:	1%{?dist}
Summary:	An ultrafast, memory-efficient short read aligner

Group:		Applications/Engineering
License:	Artistic 2.0
URL:		http://bowtie-bio.sourceforge.net/index.shtml
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       bowtie111

%description

Bowtie, an ultrafast, memory-efficient short read aligner for short
DNA sequences (reads) from next-gen sequencers. Please cite: Langmead
B, et al. Ultrafast and memory-efficient alignment of short DNA
sequences to the human genome. Genome Biol 10:R25.

%files

%changelog
* Thu Oct 02 2014 Shane Sturrock <shane@biomatters.com> - 1.1.1-1
- Fixed a compiling linkage problem related with Mavericks OSX.
- Improved performance for cases where the reference contains ambiguous or 
  masked nucleobases represented by Ns.
- Some minor automatic tests updates.

* Mon Aug 04 2014 Shane Sturrock <shane@biomatters.com> - 1.1.0-1
- Added support for large and small indexes, removing 4-billion-nucleotide
  barrier.  Bowtie can now be used with reference genomes of any size.
- No longer releasing 32-bit binaries.  Simplified manual and Makefile
  accordingly.
- Phased out CygWin support.
- Improved efficiency of index files loading.
- Fixed a bug that made the inspector fail in some situations.

* Mon Mar 24 2014 Shane Sturrock <shane@biomatters.com> - 1.0.1-1
- improved index querying efficiency using "population count" instructions 
  available since SSE4.2.

* Mon Apr 15 2013 Shane Sturrock <shane@biomatters.com> - 1.0.0-1
- New upstream release

* Tue Dec 18 2012 Carl Jones <carl@biomatters.com> - 0.12.9-1
- New upstream release

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.12.8-1
- New upstream release

* Mon Jun 27 2011 Adam Huffman <bloch@verdurin.com> - 0.12.7-2
- add missing doc/ 
- add patch to fix Perl script without shebang

* Mon Sep 13 2010 Adam Huffman <bloch@verdurin.com> - 0.12.7-1
- new upstream release 0.12.7
- changelog at http://bowtie-bio.sourceforge.net/index.shtml

* Tue Aug 31 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-3
- really fix compilation flags

* Wed Aug 25 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-2
- fix compilation flags

* Mon Aug  2 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-1
- initial version

