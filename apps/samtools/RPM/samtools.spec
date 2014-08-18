%define priority 1001
Name:		samtools
Version:	1.0
Release:	1%{?dist}
Summary:	Tools for nucleotide sequence alignments in the SAM format

Group:		Applications/Engineering
License:	MIT
URL:		http://samtools.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	samtools100
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
   --install %{_bindir}/samtools samtools /usr/lib64/samtools100/bin/samtools %{priority} \
   --slave %{_bindir}/ace2sam ace2sam /usr/lib64/samtools100/bin/ace2sam \
   --slave %{_bindir}/blast2sam.pl blast2sam.pl /usr/lib64/samtools100/bin/blast2sam.pl \
   --slave %{_bindir}/bowtie2sam.pl bowtie2sam.pl /usr/lib64/samtools100/bin/bowtie2sam.pl \
   --slave %{_bindir}/export2sam.pl export2sam.pl /usr/lib64/samtools100/bin/export2sam.pl \
   --slave %{_bindir}/interpolate_sam.pl interpolate_sam.pl /usr/lib64/samtools100/bin/interpolate_sam.pl \
   --slave %{_bindir}/maq2sam-long maq2sam-long /usr/lib64/samtools100/bin/maq2sam-long \
   --slave %{_bindir}/maq2sam-short maq2sam-short /usr/lib64/samtools100/bin/maq2sam-short \
   --slave %{_bindir}/md5fa md5fa /usr/lib64/samtools100/bin/md5fa \
   --slave %{_bindir}/md5sum-lite md5sum-lite /usr/lib64/samtools100/bin/md5sum-lite \
   --slave %{_bindir}/novo2sam.pl novo2sam.pl /usr/lib64/samtools100/bin/novo2sam.pl \
   --slave %{_bindir}/plot-bamstats plot-bamstats /usr/lib64/samtools100/bin/plot-bamstats \
   --slave %{_bindir}/psl2sam.pl psl2sam.pl /usr/lib64/samtools100/bin/psl2sam.pl \
   --slave %{_bindir}/sam2vcf.pl sam2vcf.pl /usr/lib64/samtools100/bin/sam2vcf.pl \
   --slave %{_bindir}/samtools.pl samtools.pl /usr/lib64/samtools100/bin/samtools.pl \
   --slave %{_bindir}/seq_cache_populate.pl seq_cache_populate.pl /usr/lib64/samtools100/bin/seq_cache_populate.pl \
   --slave %{_bindir}/soap2sam.pl soap2sam.pl /usr/lib64/samtools100/bin/soap2sam.pl \
   --slave %{_bindir}/varfilter.py varfilter.py /usr/lib64/samtools100/bin/varfilter.py \
   --slave %{_bindir}/wgsim wgsim /usr/lib64/samtools100/bin/wgsim \
   --slave %{_bindir}/wgsim_eval.pl wgsim_eval.pl /usr/lib64/samtools100/bin/wgsim_eval.pl \
   --slave %{_bindir}/zoom2sam.pl zoom2sam.pl /usr/lib64/samtools100/bin/zoom2sam.pl \
   --slave %{_mandir}/man1/samtools.1 samtools.1 /usr/lib64/samtools100/man/man1/samtools.1

%postun
if [ $1 -eq 0 ]
then
  alternatives --remove samtools /usr/lib64/samtools100/bin/samtools
fi

%files

%changelog
* Mon Aug 18 2014 Shane Sturrock <shane@biomatters.com> - 1.0-1
- First release of HTSlib-based samtools
- Numerous changes, notably support for CRAM sequencing file format.
- Removes bcftools from package as that is now separate
- Doesn't produce samtools-devel and samtools-lib RPMs anymore

* Mon Aug 18 2014 Shane Sturrock <shane@biomatters.com> - 0.1.19-3
- Create versioned package for modulefile compatibility
- Removes devel and libs packages as they're not used
