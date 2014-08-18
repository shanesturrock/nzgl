%define priority 1001
Name:		bcftools
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
BCFtools implements utilities for variant calling (in conjunction with
SAMtools) and manipulating VCF and BCF files.  The program is intended
to replace the Perl-based tools from vcftools.

%post
alternatives \
   --install %{_bindir}/bcftools bcftools /usr/lib64/bcftools100/bin/bcftools %{priority} \
   --slave %{_bindir}/plot-vcfstats plot-vcfstats /usr/lib64/bcftools100/bin/plot-vcfstats \
   --slave %{_bindir}/vcfutils.pl vcfutils.pl /usr/lib64/bcftools100/bin/vcfutils.pl \
   --slave %{_mandir}/man1/bcftools.1 bcftools.1 /usr/lib64/bcftools100/man/man1/bcftools.1

%postun
if [ $1 -eq 0 ]
then
  alternatives --remove bcftools /usr/lib64/bcftools100/bin/bcftools
fi

%files

%changelog
* Mon Aug 18 2014 Shane Sturrock <shane@biomatters.com> - 1.0-1
- First release of HTSlib-based bcftools
- Use in conjunction with samtools 1.0
