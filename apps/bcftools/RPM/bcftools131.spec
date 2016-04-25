%global pkgbase bcftools
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
BCFtools implements utilities for variant calling (in conjunction with
SAMtools) and manipulating VCF and BCF files.  The program is intended
to replace the Perl-based tools from vcftools.

%prep
%setup -q -n %{pkgbase}-%{version}

%build
make CFLAGS="%{optflags} -fPIC" %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/%{name}/bin
mkdir -p %{buildroot}%{_libdir}/%{name}/man/man1
install -p bcftools plot-vcfstats vcfutils.pl %{buildroot}%{_libdir}/%{name}/bin
cp -p doc/bcftools.1 %{buildroot}%{_libdir}/%{name}/man/man1/

# install modulefile
install -D -p -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE INSTALL
%{_libdir}/%{name}
%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%changelog
* Tue Apr 26 2016 Shane Sturrock <shane@biomatters.com> - 1.3.1-1
- The concat command has a new --naive option for faster operations on large
  BCFs (PR #359).
- GTisec: new plugin courtesy of David Laehnemann (@dlaehnemann) to count
  genotype intersections across all possible sample subsets in a VCF file.
- Numerous VCF parsing fixes.
- Build fix: peakfit.c now builds correctly with GSL v2 (#378).
- Various bug fixes and improvements to the annotate (#365), call (#366), index
  (#367), norm (#368, #385), reheader (#356), and roh (#328) commands, and to
  the fill-tags (#345) and tag2tag (#394) plugins.
- Clarified documentation of view filter options, and of the --regions-file and
  --targets-file options (#357, #411).

* Thu Dec 17 2015 Shane Sturrock <shane@biomatters.com> - 1.3-1
- bcftools call has new options --ploidy and --ploidy-file to make handling
  sample ploidy easier. See man page for details.
- stats: -i/-e short options changed to -I/-E to be consistent with the
  filtering -i/-e (--include/--exclude) options used in other tools.
- general --threads option to control the number of output compression threads
  used when outputting compressed VCF or BCF.
- cnv and polysomy: new commands for detecting CNVs, aneuploidy, and
  contamination from SNP genotyping data.
- various new options, plugins, and bug fixes, including #84, #201, #204, #205,
  #208, #211, #222, #225, #242, #243, #249, #282, #285, #289, #302, #311, #318,
  #336, and #338.

* Mon Feb 09 2015 Shane Sturrock <shane@biomatters.com> - 1.2-1
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
