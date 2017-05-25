%global pkgbase bcftools
%global versuffix 141
Name:		%{pkgbase}%{versuffix}
Version:	1.4.1
Release:	1%{?dist}
Summary:	Tools for nucleotide sequence alignments in the SAM format

Group:		Applications/Engineering
License:	MIT
URL:		http://samtools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{pkgbase}/%{pkgbase}-%{version}.tar.bz2
Source1:	%{name}.modulefile
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	zlib-devel >= 1.2.3
BuildRequires:	ncurses-devel,bzip2-devel,xz-devel

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
install -p bcftools %{buildroot}%{_libdir}/%{name}/bin
install -p misc/plot-vcfstats misc/vcfutils.pl misc/color-chrs.pl misc/plot-roh.py misc/guess-ploidy.py %{buildroot}%{_libdir}/%{name}/bin
#install -p bcftools plot-vcfstats vcfutils.pl %{buildroot}%{_libdir}/%{name}/bin
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
* Thu May 25 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 1.4.1-1
- This is primarily a security bug fix update.
- roh: Fixed malfunctioning options -m, --genetic-map and -M, --rec-rate, and
  newly allowed their combination. Added a convenience wrapper misc/run-roh.pl
  and an interactive script for visualizing the calls misc/plot-roh.py.
- csq: More control over warning messages (#585).
- Portability improvements (#587). Still work to be done on this front.
- Add support for breakends to view, norm, query and filtering (#592).
- plot-vcfstats: Fix for python 2/3 compatibility (#593).
- New -l, --list option for +af-dist plugin.
- New -i, --use-id option for +fix-ref plugin.
- Add --include/--exclude options to +guess-ploidy plugin.
- New +check-sparsity plugin.
- Miscellaneous bugfixes for #575, #584, #588, #599, #535.

* Wed Mar 15 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 1.4-1
- Two new commands - mpileup and csq:
  - The mpileup command has been imported from samtools to bcftools. The
    reasoning behind this is that bcftools calling is intimately tied to
    mpileup and any changes to one, often requires changes to the other. Only 
    the genotype likelihood (BCF output) part of mpileup has moved to bcftools, 
    while the textual pileup output remains in samtools. The BCF output option 
    in samtools mpileup will likely be removed in a release or two or when 
    changes to bcftools call are incompatible with the old mpileup output.
  - The basic mpileup functionality remains unchanged as do most of the command
    line options, but there are some differences and new features that one
    should be aware of:
    - The option samtools mpileup -t, --output-tags changed to bcftools mpileup
      -a, --annotate to avoid conflict with the -t, --targets option common
      across other bcftools commands.
    - -O, --output-BP and -s, --output-MQ are no longer used as they are only
      for textual pipelup output, which is not included in bcftools mpileup. -O
      short option reassigned to --output-type and -s reassigned to --samples 
      for consistency with other bcftools commands.
    - -g, --BCF, -v, --VCF, and -u, --uncompressed options from samtools
      mpileup are no longer used, being replaced by the -O, --output-type
      option common to other bcftools commands.
    - The -f, --fasta-ref option is now required by default to help avoid user
      errors. Can be disabled using --no-reference.
    - The option -d, --depth .. max per-file depth now behaves as expected and
      according to the documentation, and prints a meaningful diagnostics.
    - The -S, --samples-file can be used to rename samples on the fly. See man
      page for details.
    - The -G, --read-groups functionality has been extended to allow
      reassignment, grouping and exclusion of readgroups. See man page for
      details.
    - The -l, --positions replaced by the -t, --targets and -T, --targets-file
      options to be consistent with other bcftools commands.
    - gVCF output is supported. Per-sample gVCFs created by mpileup can be
      merged using bcftools merge --gvcf.
    - Can generate mpileup output on multiple (indexed) regions using the -r,
      --regions and -R, --regions-file options. In samtools, one was restricted
      to a single region with the -r, --region option.
    - Several speedups thanks to @jkbonfield (cf3a55a).
  - csq: New command for haplotype-aware variant consequence calling. See man
    page and paper.
- Updates, improvements and bugfixes for many other commands:
  - annotate: --collapse option added. --mark-sites now works with VCF files
    rather than just tab-delimited files. Now possible to annotate a subset of
    samples from tab file, not just VCF file (#469). Bugfixes (#428).
  - call: New option -F, --prior-freqs to take advantage of prior knowledge of
    population allele frequencies. Improved calculation of the QUAL score
    particularly for REF sites (#449, 7c56870). PLs>=256 allowed in call -m.
    Bugfixes (#436).
  - concat --naive now works with vcf.gz in addition to bcf files.
  - consensus: handle variants overlapping region boundaries (#400).
  - convert: gvcf2vcf support for mpileup and GATK. new --sex option to assign
    sex to be used in certain output types (#500). Large speedup of --hapsample
    and --haplegendsample (e8e369b) especially with --threads option enabled.
    Bugfixes (#460).
  - cnv: improvements to output (be8b378).
  - filter: bugfixes (#406).
  - gtcheck: improved cross-check mode (#441).
  - index can now specify the path to the output index file. Also, gains the
    --threads option.
  - merge: Large overhaul of merge command including support for merging gVCF
    files created by bcftools mpileup --gvcf with the new -g, --gvcf option.
    New options -F to control filter logic and -0 to set missing data to REF.
    Resolved a number of longstanding issues (#296, #361, #401, #408, #412).
  - norm: Bugfixes (#385,#452,#439), more informative error messages (#364).
  - query: %END plus %POS0, %END0 (0-indexed) support - allows easy BED format
    output (#479). %TBCSQ for use with the new csq command. Bugfixes
    (#488,#489).
  - plugin: A number of new plugins:
    - GTsubset (thanks to @dlaehnemann)
    - ad-bias
    - af-dist
    - fill-from-fasta
    - fixref
    - guess-ploidy (deprecates vcf2sex plugin)
    - isecGT
    - Trio-switch-rate
  - and changes to existing plugins:
    - tag2tag: Added gp-to-gt, pl-to-gl and --threshold options and bugfixes
      (#475).
    - ad-bias: New -d option for minimum depth.
    - impute-info: Bugfix (49a9eaf).
    - fill-tags: Added ability to aggregate tags for sample subgroups, thanks
      to @mh11. (#503). HWE tag added as an option.
    - mendelian: Bugfix (#566).
  - reheader: allow muiltispace delimiters in --samples option.
  - roh: Now possible to process multiple samples at once. This allows
    considerable speedups for files with thousands of samples where the cost of
    HMM is neglibible compared to I/O and decompressing. In order to fit tens of
    thousands samples in memory, a sliding HMM can be used (new --buffer-size
    option). Viterbi training now uses Baum-Welch algorithm, and works much 
    better. Support for gVCFs or FORMAT/PL tags. Added -o, output and -O, 
    --output-type options to control output of sites or regions (compression 
    optional). Many bugs fixed - do not segfault on missing PL values anymore, 
    a typo in genetic map calculation resulted in a slowdown and incorrect 
    results.
  - stats: Bugfixes (16414e6), new options -af-bins and -af-tags to control
    allele frequency binning of output. Per-sample genotype concordance tables
    added (#477).
  - view -a, --trim-alt-alleles various bugfixes for missing data and more
    informative errors should now be given on failure to pinpoint problems.
- General changes:
  - Timestamps are now added to header lines summarising the command (#467).
  - Use of the --threads options should be faster across the board thanks to
    changes in HTSlib meaning meaning threads are now shared by the compression
    and decompression calls.
  - Changes to genotype filtering with -i, --include and -e, --exclude (#454).

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
