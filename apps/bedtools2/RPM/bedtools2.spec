Name:		bedtools2
Version:	2.22.1
Release:	2%{?dist}
Summary:	Tools for handing BED files
Group:		Applications/Engineering
License:	GPL
URL:		https://github.com/arq5x/bedtools2
SOURCE:		bedtools2-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	zlib-devel

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
