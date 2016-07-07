Name:		bedtools2
Version:	2.26.0
Release:	1%{?dist}
Summary:	Tools for handing BED files
Group:		Applications/Engineering
License:	GPL
URL:		https://github.com/arq5x/bedtools2
SOURCE:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	zlib-devel python

%description
BEDTools is a suite of utilities for comparing genomic features in BED format. 
These utilities allow one to quickly address tasks such as: 1. Intersecting 
two BED files. 2. Merge overlapping features. 3. Paired-end overlaps.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 bin/annotateBed %{buildroot}%{_bindir}
install -m 0755 bin/bamToBed %{buildroot}%{_bindir}
install -m 0755 bin/bamToFastq %{buildroot}%{_bindir}
install -m 0755 bin/bed12ToBed6 %{buildroot}%{_bindir}
install -m 0755 bin/bedpeToBam %{buildroot}%{_bindir}
install -m 0755 bin/bedToBam %{buildroot}%{_bindir}
install -m 0755 bin/bedToIgv %{buildroot}%{_bindir}
install -m 0755 bin/bedtools %{buildroot}%{_bindir}
install -m 0755 bin/closestBed %{buildroot}%{_bindir}
install -m 0755 bin/clusterBed %{buildroot}%{_bindir}
install -m 0755 bin/complementBed %{buildroot}%{_bindir}
install -m 0755 bin/coverageBed %{buildroot}%{_bindir}
install -m 0755 bin/expandCols %{buildroot}%{_bindir}
install -m 0755 bin/fastaFromBed %{buildroot}%{_bindir}
install -m 0755 bin/flankBed %{buildroot}%{_bindir}
install -m 0755 bin/genomeCoverageBed %{buildroot}%{_bindir}
install -m 0755 bin/getOverlap %{buildroot}%{_bindir}
install -m 0755 bin/groupBy %{buildroot}%{_bindir}
install -m 0755 bin/intersectBed %{buildroot}%{_bindir}
install -m 0755 bin/linksBed %{buildroot}%{_bindir}
install -m 0755 bin/mapBed %{buildroot}%{_bindir}
install -m 0755 bin/maskFastaFromBed %{buildroot}%{_bindir}
install -m 0755 bin/mergeBed %{buildroot}%{_bindir}
install -m 0755 bin/multiBamCov %{buildroot}%{_bindir}
install -m 0755 bin/multiIntersectBed %{buildroot}%{_bindir}
install -m 0755 bin/nucBed %{buildroot}%{_bindir}
install -m 0755 bin/pairToBed %{buildroot}%{_bindir}
install -m 0755 bin/pairToPair %{buildroot}%{_bindir}
install -m 0755 bin/randomBed %{buildroot}%{_bindir}
install -m 0755 bin/shuffleBed %{buildroot}%{_bindir}
install -m 0755 bin/slopBed %{buildroot}%{_bindir}
install -m 0755 bin/sortBed %{buildroot}%{_bindir}
install -m 0755 bin/subtractBed %{buildroot}%{_bindir}
install -m 0755 bin/tagBam %{buildroot}%{_bindir}
install -m 0755 bin/unionBedGraphs %{buildroot}%{_bindir}
install -m 0755 bin/windowBed %{buildroot}%{_bindir}
install -m 0755 bin/windowMaker %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/annotateBed
%{_bindir}/bamToBed
%{_bindir}/bamToFastq
%{_bindir}/bed12ToBed6
%{_bindir}/bedpeToBam
%{_bindir}/bedToBam
%{_bindir}/bedToIgv
%{_bindir}/bedtools
%{_bindir}/closestBed
%{_bindir}/clusterBed
%{_bindir}/complementBed
%{_bindir}/coverageBed
%{_bindir}/expandCols
%{_bindir}/fastaFromBed
%{_bindir}/flankBed
%{_bindir}/genomeCoverageBed
%{_bindir}/getOverlap
%{_bindir}/groupBy
%{_bindir}/intersectBed
%{_bindir}/linksBed
%{_bindir}/mapBed
%{_bindir}/maskFastaFromBed
%{_bindir}/mergeBed
%{_bindir}/multiBamCov
%{_bindir}/multiIntersectBed
%{_bindir}/nucBed
%{_bindir}/pairToBed
%{_bindir}/pairToPair
%{_bindir}/randomBed
%{_bindir}/shuffleBed
%{_bindir}/slopBed
%{_bindir}/sortBed
%{_bindir}/subtractBed
%{_bindir}/tagBam
%{_bindir}/unionBedGraphs
%{_bindir}/windowBed
%{_bindir}/windowMaker

%changelog
* Fri Jul 08 2016 Shane Sturrock <shane@biomatters.com> - 2.26.0-1
- Fixed a major memory leak when using -sorted. Thanks to Emily Tsang and
  Stephen Montgomery.
- Fixed a bug for BED files containing a single record with no newline. Thanks
  to @jmarshall.
- The getfasta tool includes name, chromosome and position in fasta headers
  when the -name option is used. Thanks to @rishavray.
- Fixed a bug that now forces the coverage tool to process every record in the
  -a file.
- Fixed a bug preventing proper processing of BED files with consecutive tabs.
- VCF files containing structural variants now infer SV length from either the
  SVLEN or END INFO fields. Thanks to Zev Kronenberg.
- Resolve off by one bugs when intersecting GFF or VCF files with BED files.
- The shuffle tool now uses roulette wheel sampling to shuffle to -incl regions
  based upon the size of the interval. Thanks to Zev Kronenberg and Michael
  Imbeault.
- Fixed a bug in coverage that prevented correct calculation of depth when
  using the -split option.
- The shuffle tool warns when an interval exceeds the maximum chromosome
  length.
- The complement tool better checks intervals against the chromosome lengths.
- Fixes for stddev, min, and max operations. Thanks to @jmarshall.
- Enabled stdev, sstdev, freqasc, and freqdesc options for groupby.
- Allow -s and -w to be used in any order for makewindows.
- Added new -bedOut option to getfasta.
- The -r option forces the -F value for intersect.
- Add -pc option to the genomecov tool, allowing coverage to be calculated
  based upon paired-end fragments.

* Fri Sep 04 2015 Shane Sturrock <shane@biomatters.com> - 2.25.0-1
- Added new -F option that allows one to set the minimum fraction of
  overlap required for the B interval. This complements the
  functionality of the -f option.Available for intersect, coverage, map,
  subtract, and jaccard.
- Added new -e option that allows one to require that the minimum
  fraction overlap is achieved in either A _OR_ B, not A _AND_ B which
  is the behavior of the -r option. Available for intersect, coverage,
  map, subtract, and jaccard.
- Fixed a longstanding bug that prevented genomecov from reporting
  chromosomes that lack a single interval.
- Modified a src directory called "aux" to "driver" to prevent
  compilation errors on Windows machines. Thanks very much to John
  Marshall.
- Fixed a regression that caused the coverage tool to complain if BED
  files had less than 5 columns.
- Fixed a variable overload bug that prevented compilation on Debian
  machines.
- Speedups to the groupby tool.
- New -delim option for the groupby tool.
- Fixed a bug in map that prevented strand-specifc overlaps from being
  reported when using certain BEDPLUS formats.
- Prevented excessive memory usage when not using pre-sorted input.

* Tue Jun 02 2015 Shane Sturrock <shane@biomatters.com> - 2.24.0-1
- The coverage tool now takes advantage of pre-sorted intervals via the 
  -sorted option. This allows the coverage tool to be much faster, use far 
  less memory, and report coverage for intervals in their original order 
  in the input file.
- We have changed the behavior of the coverage tool such that it is 
  consistent with the other tools. Specifically, coverage is now computed 
  for the intervals in the A file based on the overlaps with the B file, 
  rather than vice versa.
- The subtract tool now supports pre-sorted data via the -sorted option and 
  is therefore much faster and scalable.
- The -nonamecheck option provides greater tolerance for chromosome labeling 
  when using the -sorted option.
- Support for multiple SVLEN tags in VCF format, and fixed a bug that failed 
  to process SVLEN tags coming at the end of a VCF INFO field.
- Support for reverse complementing IUPAC codes in the getfasta tool.
- Provided greater flexibility for “BED+” files, where the first 3 columns 
  are chrom, start, and end, and the remaining columns are free-form.
- We now detect stale FAI files and recreate an index thanks to a fix from 
  @gtamazian.
- New feature from Pierre Lindenbaum allowing the sort tool to sort files 
  based on the chromosome order in a faidx file.
- Eliminated multiple compilation warnings thanks to John Marshall.
- Fixed bug in handling INS variants in VCF files.

* Tue Feb 24 2015 Shane Sturrock <shane@biomatters.com> - 2.23.0-1
- New features.
  - Added -k option to the closest tool to report the k-closest features in 
    one or more -b files.
  - Added -fd option to the closest tool to for the reporting of downstream 
    features in one or more -b files. Requires -D to dictate how "downstream" 
    should be defined.
  - Added -fu option to the closest tool to for the reporting of downstream 
    features in one or more -b files. Requires -D to dictate how "downstream" 
    should be defined.
  - @lindenb added a new split tool that will split an input file into 
    multiple sub files. Unlike UNIX split, it can balance the chunking of the 
    sub files not just by number of lines, but also by total number of base 
    pairs in each sub file.
  - Added a new spacing tool that reports the distances between features in a 
    file.
  - @jayhesselberth added a -reverse option to the makewindows tool that 
    reverses the order of the assigned window numbers.
- Bug fixes.
  - Fixed a bug that caused incorrect reporting of overlap for zero-length 
    BED records. Thanks to @roryk.
  - Fixed a bug that caused the map tool to not allow -b to be specified 
    before -a. Thanks to @semenko.
  - Fixed a bug in makewindows that mistakenly required -s with -n.

* Thu Feb 19 2015 Shane Sturrock <shane@biomatters.com> - 2.22.1-3
- Building on CentOS 7 requires python

* Tue Feb 17 2015 Shane Sturrock <shane@biomatters.com> - 2.22.1-2
- Compatability with CentOS 7

* Mon Jan 12 2015 Shane Sturrock <shane@biomatters.com> - 2.22.1-1
- When using -sorted with intersect, map, and closest, bedtools can now detect 
  and warn you when your input datasets employ different chromosome sorting 
  orders.
- Fixed multiple bugs in the new, faster closest tool. Specifically, the -iu, 
  -id, and -D options were not behaving properly with the new "sweeping" 
  algorithm that was implemented for the 2.22.0 release. Many thanks to Sol 
  Katzman for reporting these issues and for providing a detailed analysis 
  and example files.
- We FINALLY wrote proper documentation for the closest tool.
  http://bedtools.readthedocs.org/en/latest/content/tools/closest.html
- Fixed bug in the tag tool when using -intervals, -names, or -scores. Thanks 
  to Yarden Katz for reporting this.
- Fixed issues with chromosome boundaries in the slop tool when using negative 
  distances. Thanks to @acdaugherty!
- Multiple improvements to the fisher tool. Added a -m option to the fisher 
  tool to merge overlapping intervals prior to comparing overlaps between two 
  input files. Thanks to @brentp
- Fixed a bug in makewindows tool requiring the use of -b with -s.
- Fixed a bug in intersect that prevented -split from detecting complete 
  overlaps with -f 1. Thanks to @tleonardi .
- Restored the default decimal precision to the groupby tool.
- Added the -prec option to the merge and map tools to specific the decimal 
  precision of the output.

* Thu Nov 13 2014 Shane Sturrock <shane@biomatters.com> - 2.22.0-1
- Multiple database support for the closest tool. The closest tool now 
  requires sorted input, but it is between 10 and 60 times faster depending 
  on the use case.
- Support for IMPRECISE SVs in VCF format.
- Added the -prec option to grouby to allow control over the reported decimal 
  precision.
- Fixed a bug with zero length records.
- Fixed a precision bug in the fisher tool. Thanks to @brentp
- Fixed a bug in the bamtofastq tool. Thanks to @ryan-williams

* Mon Sep 22 2014 Shane Sturrock <shane@biomatters.com> - 2.21.0-1
- Added ability to intersect against multiple -b files in the intersect tool.
- Fixed a bug causing slowdowns in the -sorted option when using -split with 
  very large split alignments.
- Added a new fisher tool to report a P-value associated with the significance 
  of the overlaps between two interval sets. Thanks to @brentp!
- Added a “genome” file for GRCh38. Thanks @martijnvermaat!
- Fixed a bug in the -pct option of the slop tool. Thanks to @brentp!
- Tweak to the Makefile to accomodate Intel compilers. Thanks to @jmarshall.
- Many updates to the docs from the community. Thank you!

* Mon May 26 2014 Sidney Markowitz <sidney@biomatters.com> - 2.20.1-1
- Fixed a float rounding bug causing occasional off-by-one issues in the slop
  added by the slop tool.
- Fixed a bug injected in 2.19 arising when files have a single line not ending
  in a newline.

* Mon Mar 10 2014 Shane Sturrock <shane@biomatters.com> - 2.19.1-1
- Bug fix to intersect causing BAM footers to be erroneously written when 
  -b is BAM
- Speedup for the map tool.
- Map tool now allows multiple columns and operations in a single run.

* Mon Feb 10 2014 Shane Sturrock <shane@biomatters.com> - 2.19.0-1
- Bug Fixes
  - Fixed a long standing bug in which the number of base pairs of overlap 
    was incorrectly calculated when using the -wo option with the -split 
    option.
  - Fixed a bug in which certain flavors of unmapped BAM alignments were 
    incorrectly rejected in the latest 2.18.* series.
- Enhancements
  - Substantially reduced memory usage, especially when dealing with unsorted 
    data. Memory usage ballooned in the 2.18.* series owing to default buffer 
    sizes we were using in a custom string class.  We have adjusted this and 
    the memory usage has returned to 2.17.* levels while maintaining speed 
    increases.
- New Features
  - The latest version of the "map" function is ~3X faster than the one 
    available in version 2.17 and 2.18
  - The map function now supports the "-split" option, as well as "absmin" 
    and "absmax" operations.
  - In addition, it supports multiple chromosome sorting criterion by 
    supplying a genome file that defines the expected chromosome order. 

* Tue Feb 04 2014 Shane Sturrock <shane@biomatters.com> - 2.18.2-1
- Initial build.
