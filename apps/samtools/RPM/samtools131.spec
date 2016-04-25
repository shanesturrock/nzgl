%global pkgbase samtools
%global versuffix 131
Name:		%{pkgbase}%{versuffix}
Version:	1.3.1
Release:	1%{?dist}
Summary:	Tools for nucleotide sequence alignments in the SAM format

Group:		Applications/Engineering
License:	MIT
URL:		http://samtools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{pkgbase}/%{pkgbase}-%{version}.tar.bz2
Source1:	%{name}.modulefile
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	zlib-devel >= 1.2.3
BuildRequires:	ncurses-devel

%description
SAM (Sequence Alignment/Map) is a flexible generic format for storing
nucleotide sequence alignment.
SAM Tools provide various utilities for manipulating alignments in the
SAM format, including sorting, merging, indexing and generating
alignments in a per-position format.

%prep
%setup -q -n %{pkgbase}-%{version}

# fix wrong interpreter
perl -pi -e "s[/software/bin/python][%{__python}]" misc/varfilter.py

# fix eol encoding
sed -i 's/\r//' misc/export2sam.pl


%build
make CFLAGS="%{optflags} -fPIC" %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/%{name}/bin
mkdir -p %{buildroot}%{_libdir}/%{name}/man/man1
install -p samtools %{buildroot}%{_libdir}/%{name}/bin
cp -p samtools.1 %{buildroot}%{_libdir}/%{name}/man/man1/

# install modulefile
install -D -p -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

cd misc/
install -p ace2sam blast2sam.pl bowtie2sam.pl export2sam.pl \
    interpolate_sam.pl maq2sam-long maq2sam-short md5fa md5sum-lite \
    novo2sam.pl plot-bamstats psl2sam.pl sam2vcf.pl samtools.pl \
    seq_cache_populate.pl soap2sam.pl varfilter.py wgsim wgsim_eval.pl \
    zoom2sam.pl \
    %{buildroot}%{_libdir}/%{name}/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog.old LICENSE INSTALL NEWS examples/
%{_libdir}/%{name}
%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%changelog
* Tue Apr 26 2016 Shane Sturrock <shane@biomatters.com> - 1.3.1-1
- The sort command creates any needed temporary files alongside the final
  output file (similarly to the pre-1.3 behaviour), and now aborts when it
  detects a collision with another sort invocation's temporary files.
- When the -T PREFIX option specified is a directory (or when sorting to
  standard output), a random component is now added to temporary filenames to
  try to avoid collisions (#432, #523, #529, #535, PR #530).
- All samtools commands now check for I/O errors more carefully, especially
  when writing output files (#111, #253, #470, PR #467).
- Build fixes for 32-bit systems; be sure to run configure on such systems to
  enable large file support and access to 2GiB+ files.
- The fasta/fastq/bam2fq command no longer ignores reads when the -s option is
  used (#532).
- The fastq -O option no longer crashes on reads that do not have an OQ tag
  field (#517).
- The merge and sort commands now handle (unusual) BAM files that have no
  textual @SQ headers (#548, #550).
- Sorting files containing @CO headers no longer duplicates the comment
  headers, which previously happened on large sorts for which temporary files
  were needed (#563).
- The rmdup and view -l commands no longer crash on @RG headers that do not
  have a LB field (#538).
- Fixed miscellaneous issues #128, #130, #131, #489, and #514.

* Thu Dec 17 2015 Shane Sturrock <shane@biomatters.com> - 1.3-1
- The obsolete samtools sort in.bam out.prefix usage has been removed. If you
  are still using ‑f, ‑o, or out.prefix, convert to use -T PREFIX and/or -o
  FILE instead. (#295, #349, #356, #418, PR #441; see also discussions in #171,
  #213.)
- The bamshuf command has been renamed to collate (hence the term bamshuf no
  longer appears in the documentation, though it still works on the command
  line for compatibility with existing scripts).
- The mpileup command now outputs the unseen allele in VCF/BCF as <*> rather
  than X or <X> as previously, and now has AD, ADF, ADR, INFO/AD, INFO/ADF,
  INFO/ADR --output-tags annotations that largely supersede the existing DV, 
  DP4, DPR annotations.
- The mpileup command now applies BAQ calculations at all base positions,
  regardless of which -l or -r options are used (previously with -l it was not
  applied to the first few tens of bases of each chromosome, leading to 
  different mpileup results with -l vs. -r; #79, #125, #286, #407).
- Samtools now has a configure script which checks your build environment and
  facilitates choosing which HTSlib to build against. See INSTALL for details.
- Samtools's Makefile now fully supports the standard convention of allowing
  CC/CPPFLAGS/CFLAGS/LDFLAGS/LIBS to be overridden as needed. Previously it
  listened to $(LDLIBS) instead; if you were overriding that, you should now
  override LIBS rather than LDLIBS.
- A new addreplacerg command that adds or alters @RG headers and RG:Z record
  tags has been added.
- The rmdup command no longer immediately aborts (previously it always aborted
  with bam_get_library() not yet implemented), but remains not recommended for
  most use (#159, #252, #291, #393).
- Merging files with millions of headers now completes in a reasonable amount
  of time (#337, #373, #419, #453; thanks to Nathan Weeks, Chris Smowton,
  Martin Pollard, Rob Davies).
- Samtools index's optional index output path argument works again (#199).
- Fixed calmd, targetcut, and potential mpileup segfaults when given broken
  alignments with POS far beyond the end of their reference sequences.
- If you have source code using bam_md.c's bam_fillmd1_core(), bam_cap_mapQ(),
  or bam_prob_realn_core() functions, note that these now take an additional
  ref_len parameter. (The versions named without _core are unchanged.)
- The tview command's colour scheme has been altered to be more suitable for
  users with colour blindness (#457).
- Samtools depad command now handles CIGAR N operators and accepts CRAM files
  (#201, #404).
- Samtools stats now outputs separate "N" and "other" columns in the ACGT
  content per cycle section (#376).
- Added -a option to samtools depth to show all locations, including zero depth
  sites (#374).
- New samtools dict command, which creates a sequence dictionary (as used by
  Picard) from a FASTA reference file.
- Samtools stats --target-regions option works again.
- Added legacy API sam.h functions sam_index_load() and samfetch() providing
  bam_fetch()-style iteration over either BAM or CRAM files. (In general we
  recommend recoding against the htslib API directly, but this addition may help
  existing libbam-using programs to be CRAM-enabled easily.)
- Fixed legacy API's samopen() to write headers only with "wh" when writing SAM
  files. Plain "w" suppresses headers for SAM file output, but this was broken
  in 1.2.
- samtools fixmate - - works in pipelines again; with 1.0 to 1.2, this failed
  with [bam_mating] cannot determine output format.
- Restored previous samtools calmd -u behaviour of writing compression level 0
  BAM files. Samtools 1.0 to 1.2 incorrectly wrote raw non-BGZF BAM files,
  which cannot be read by most other tools. (Samtools commands other than calmd
  were unaffected by this bug.)
- Restored bam_nt16_nt4_table[] to legacy API header bam.h.
- Fixed bugs #269, #305, #320, #328, #346, #353, #365, #392, #410, #445, #462,
  #475, and #495.

* Mon Feb 09 2015 Shane Sturrock <shane@biomatters.com> - 1.2-1
- Flagstat now works on SAM, BAM, or CRAM files (rather than BAM only)
- Stats calculates mismatches per cycle for unclipped length
- Merge can now merge SAM input files
- CRAM reference files are now cached by default (see HTSlib below and 
  samtools(1) man page)
- Tested against Intel-optimised zlib (https://github.com/jtkukunas/zlib; see 
  README for details)
- Fixed bugs #302, #309, #318, and #327

* Thu Sep 25 2014 Shane Sturrock <shane@biomatters.com> - 1.1-1
- Samtools fixmate and flagstat now consider supplementary reads
- Sorting BAM files with thousands of reference contigs now completes in a 
  reasonable amount of time
- Fixed samtools idxstats when displaying statistics from indices generated by 
  samtools 0.1.x
- Fixed samtools calmd memory leak
- Samtools fixmate now only adds a template cigar tag (ct:Z) when requested 
  with -c, and never adds it repeatedly
- Regularised script #! directives as #!/usr/bin/env perl etc
- Fixed DPR annotation in samtools mpileup
- New bcftools convert and plugin commands and annotate --rename-chrs option
- BCFtools norm performance is improved and now averages QUALs and accumulates 
  IDs and FILTERs
- Improved bcftools filter expressions, query support for IUPAC ambiguity 
  codes, and annotate support for genotype fields
- Plugins for bcftools have now moved from annotate to the new plugin command

* Mon Aug 18 2014 Shane Sturrock <shane@biomatters.com> - 1.0-1
- First release of HTSlib-based samtools
- Numerous changes, notably support for CRAM sequencing file format.
- Removes bcftools from package as that is now separate
- Doesn't produce samtools-devel and samtools-lib RPMs anymore

* Mon Apr 22 2013 Shane Sturrock <shane@biomatters.com> - 0.1.19-2
- Bring upstream update from fedora into NZGL replacing homegrown

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 0.1.19-1
- update to 0.1.19

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Adam Huffman <verdurin@fedoraproject.org> - 0.1.18-2
- make sure new seqtk tool included

* Tue Sep  6 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.18-1
- Updated to 0.1.18

* Tue May 10 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.16-1
- Updated to 0.1.16

* Mon Apr 11 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.15-1
- Updated to 0.1.15

* Wed Mar 23 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.14-1
- Updated to 0.1.14
- Build shared library instead of static

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.12a-2
- Fixed header files directory ownership
- Added missing header files

* Mon Dec  6 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.12a-1
- Updated to 0.1.12a

* Tue Nov 23 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-4
- cleanup man page handling

* Sun Oct 10 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-4
- fix attributes for devel subpackage
- fix library location

* Sun Sep 26 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-3
- put headers and library in standard locations

* Mon Sep 6 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-2
- merge Rasmus' latest changes (0.1.8 update)
- include bam.h and libbam.a for Bio-SamTools compilation
- move bam.h and libbam.a to single directory
- put bgzf.h, khash.h and faidx.h in the same place
- add -fPIC to CFLAGS to make Bio-SamTools happy
- add virtual Provide as per guidelines

* Tue Aug 17 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.8-1
- Updated to 0.1.8.

* Mon Nov 30 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.7a-1
- Updated to 0.1.7a.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-3
- Specfile cleanup.

* Sat Jul 11 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-2
- Fixed manpage location.
- Make sure optflags is passed to the makefiles.

* Sat Jul 11 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-1
- Initial build.
