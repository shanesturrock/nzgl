%define priority 141
Name:		samtools
Version:	1.4
Release:	1%{?dist}
Summary:	Tools for nucleotide sequence alignments in the SAM format

Group:		Applications/Engineering
License:	MIT
URL:		http://samtools.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	samtools14
# Post requires alternatives to install tool alternatives.
Requires(post):   %{_sbindir}/alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): %{_sbindir}/alternatives

%description
SAM (Sequence Alignment/Map) is a flexible generic format for storing
nucleotide sequence alignment.
SAM Tools provide various utilities for manipulating alignments in the
SAM format, including sorting, merging, indexing and generating
alignments in a per-position format.

%post
alternatives \
   --install %{_bindir}/samtools samtools /usr/lib64/samtools14/bin/samtools %{priority} \
   --slave %{_bindir}/ace2sam ace2sam /usr/lib64/samtools14/bin/ace2sam \
   --slave %{_bindir}/blast2sam.pl blast2sam.pl /usr/lib64/samtools14/bin/blast2sam.pl \
   --slave %{_bindir}/bowtie2sam.pl bowtie2sam.pl /usr/lib64/samtools14/bin/bowtie2sam.pl \
   --slave %{_bindir}/export2sam.pl export2sam.pl /usr/lib64/samtools14/bin/export2sam.pl \
   --slave %{_bindir}/interpolate_sam.pl interpolate_sam.pl /usr/lib64/samtools14/bin/interpolate_sam.pl \
   --slave %{_bindir}/maq2sam-long maq2sam-long /usr/lib64/samtools14/bin/maq2sam-long \
   --slave %{_bindir}/maq2sam-short maq2sam-short /usr/lib64/samtools14/bin/maq2sam-short \
   --slave %{_bindir}/md5fa md5fa /usr/lib64/samtools14/bin/md5fa \
   --slave %{_bindir}/md5sum-lite md5sum-lite /usr/lib64/samtools14/bin/md5sum-lite \
   --slave %{_bindir}/novo2sam.pl novo2sam.pl /usr/lib64/samtools14/bin/novo2sam.pl \
   --slave %{_bindir}/plot-bamstats plot-bamstats /usr/lib64/samtools14/bin/plot-bamstats \
   --slave %{_bindir}/psl2sam.pl psl2sam.pl /usr/lib64/samtools14/bin/psl2sam.pl \
   --slave %{_bindir}/sam2vcf.pl sam2vcf.pl /usr/lib64/samtools14/bin/sam2vcf.pl \
   --slave %{_bindir}/samtools.pl samtools.pl /usr/lib64/samtools14/bin/samtools.pl \
   --slave %{_bindir}/seq_cache_populate.pl seq_cache_populate.pl /usr/lib64/samtools14/bin/seq_cache_populate.pl \
   --slave %{_bindir}/soap2sam.pl soap2sam.pl /usr/lib64/samtools14/bin/soap2sam.pl \
   --slave %{_bindir}/varfilter.py varfilter.py /usr/lib64/samtools14/bin/varfilter.py \
   --slave %{_bindir}/wgsim wgsim /usr/lib64/samtools14/bin/wgsim \
   --slave %{_bindir}/wgsim_eval.pl wgsim_eval.pl /usr/lib64/samtools14/bin/wgsim_eval.pl \
   --slave %{_bindir}/zoom2sam.pl zoom2sam.pl /usr/lib64/samtools14/bin/zoom2sam.pl \
   --slave %{_mandir}/man1/samtools.1 samtools.1 /usr/lib64/samtools14/man/man1/samtools.1

%postun
if [ $1 -eq 0 ]
then
  alternatives --remove samtools /usr/lib64/samtools14/bin/samtools
fi

%files

%changelog
* Wed Mar 15 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 1.4-1
- Fixed Issue #345 - out-by-one error in insert-size in samtools stats
- bam_split now add a @PG header to the bam file
- Added mate cigar tag support to fixmate
- Multi-threading is now supported for decoding BAM and CRAM (as well
  as the previously supported encoding).  Most commands that read BAM
  or CRAM have gained an -@ or --threads arguments, providing a
  significant speed bonus.  For commands that both read and write
  files the threads are shared between decoding and encoding tasks.
- Added -a option to samtools mpileup to show all locations, including
  sites with zero depth; repeating the option as -aa or -a -a additionally
  shows reference sequences without any reads mapped to them (#496).
- The mpileup text output no longer contains empty columns at zero coverage
  positions.  Previously it would output "...0\t\t..." in some circumstances
  (zero coverage due to being below a minumum base quality); this has been
  fixed to output as "...0\t*\t*..." with placeholder '*' characters as in
  other zero coverage circumstances (see PR #537).
- To stop it from creating too many temporary files, samtools sort
  will now not run unless its per-thread memory limit (-m) is set to
  at least 1 megabyte (#547).
- The misc/plot-bamstats script now has a -l / --log-y option to change
  various graphs to display their Y axis log-scaled.  Currently this
  affects the Insert Size graph (PR #589; thanks to Anton Kratz).
- Fixmate will now also add and update MC (mate CIGAR) tags.

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
- CRAM reference files are now cached by default (see HTSlib below and samtools(
1) man page)
- Tested against Intel-optimised zlib (https://github.com/jtkukunas/zlib; see RE
ADME for details)
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

* Mon Aug 18 2014 Shane Sturrock <shane@biomatters.com> - 0.1.19-3
- Create versioned package for modulefile compatibility
- Removes devel and libs packages as they're not used
