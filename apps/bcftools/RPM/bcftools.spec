%define priority 1201
Name:		bcftools
Version:	1.2
Release:	1%{?dist}
Summary:	Tools for nucleotide sequence alignments in the SAM format

Group:		Applications/Engineering
License:	MIT
URL:		http://samtools.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	samtools120
Requires:	bcftools120
# Post requires alternatives to install tool alternatives.
Requires(post):   %{_sbindir}/alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): %{_sbindir}/alternatives

%description
BCFtools implements utilities for variant calling (in conjunction with
SAMtools) and manipulating VCF and BCF files.  The program is intended
to replace the Perl-based tools from vcftools.

%post
alternatives \
   --install %{_bindir}/bcftools bcftools /usr/lib64/bcftools110/bin/bcftools %{priority} \
   --slave %{_bindir}/plot-vcfstats plot-vcfstats /usr/lib64/bcftools110/bin/plot-vcfstats \
   --slave %{_bindir}/vcfutils.pl vcfutils.pl /usr/lib64/bcftools110/bin/vcfutils.pl \
   --slave %{_mandir}/man1/bcftools.1 bcftools.1 /usr/lib64/bcftools110/man/man1/bcftools.1

%postun
if [ $1 -eq 0 ]
then
  alternatives --remove bcftools /usr/lib64/bcftools110/bin/bcftools
fi

%files

%changelog
* Mon Feb 09 2015 Shane Sturrock <shane@biomatters.com> - 1.2-1
- Use in conjunction with samtools 1.2
- new consensus command
- new annotate plugins: fixploidy, vcf2sex, tag2tag
- more features in convert command, amongst others new --hapsample function
  (thanks to Warren Kretzschmar)
- support for complements in bcftools annotate --remove
- support for -i/-e filtering expressions in isec
- improved error reporting
- call command changes:
  - the default prior increased from -P1e-3 to -P1.1e-3, some clear calls
    were missed with default settings previously
  - support for the new symbolic allele <*>
  - support for -f GQ
  - bug fixes, such as: proper trimming of DPR tag with -c; the -A switch
    does not add back records removed by -v and the behaviour has been made
    consistent with -c and -m
- many bug fixes and improvements, such as
  - bug in filtering, FMT & INFO vs INFO & FMT
  - fixes in bcftools merge
  - filter update AN/AC with -S
  - isec outputs matching records for both VCFs in the Venn mode
  - annotate considers alleles when working with Number=A,R tags
  - new --set-id feature for annotate
  - convert can be used similarly to view

* Thu Sep 25 2014 Shane Sturrock <shane@biomatters.com> - 1.1-1
- Use in conjunction with samtools 1.1

* Mon Aug 18 2014 Shane Sturrock <shane@biomatters.com> - 1.0-1
- First release of HTSlib-based bcftools
- Use in conjunction with samtools 1.0
