Name:		bedtools2
Version:	2.19.0
Release:	1%{?dist}
Summary:	Tools for handing BED files
Group:		Applications/Engineering
License:	GPL
URL:		https://github.com/arq5x/bedtools2
SOURCE:		bedtools2-2.19.0.tar.gz
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
%{_bindir}

%changelog
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
