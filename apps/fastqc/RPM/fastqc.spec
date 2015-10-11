Name:		fastqc
Version:	0.11.4
Release:	1%{?dist}
Summary:	A quality control application for high throughput sequence data
Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.bioinformatics.babraham.ac.uk/projects/%{name}/
Source0:	http://www.bioinformatics.babraham.ac.uk/projects/%{name}/%{name}_v%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0:		%{name}.patch

%description
FastQC aims to provide a simple way to do some quality control checks on raw sequence data coming from 
high throughput sequencing pipelines. It provides a modular set of analyses which you can use to give a 
quick impression of whether your data has any problems of which you should be aware before doing any 
further analysis.

%prep
%setup -q -n FastQC
%patch0 -p0

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_bindir}

/bin/cp -r Configuration/ Help/ Templates/ net/ org/ uk/ *.jar %{buildroot}/%{_javadir}/%{name}
install -m 0755 fastqc %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt  README.txt  RELEASE_NOTES.txt
/usr/bin/fastqc
/usr/share/java/fastqc/*

%changelog
* Mon Oct 12 2015 Shane Sturrock <shane@biomatters.com> - 0.11.4-1
- Changed the OSX launcher to not rely on the internal JVM framework, but use
  any command line java which is found
- Fixed a typo in one of the adapter sequences
- Fixed a bug which meant that some file extensions weren't removed from report
  names in non-interactive mode
- Made the per-tile module not collect any stats if it's disabled in limits.txt
- Fixed a bug in the calculation of duplication for highly duplicated, ordered
  files with very small numbers of sequences
- Fixed an incorrect error flag in the per-base quality module where there were
  less than 100 observations in a read group

* Thu Mar 26 2015 Shane Sturrock <shane@biomatters.com> - 0.11.3-1
- Fixed a bug when disabling the per-tile plot from limits.txt
- Fixed a bug which caused the program to continue when processing of 
  multiple files was actually complete
- Fixed a bug which meant format selection in the interactive application 
  didn't work
- Added checks for mis-itentifying tile numbers in confusing sample ids
- Added the SOLID smallRNA adapter to the standard search set
- Fixed a bug when extracting casava names from uncompressed fastq files
- Added support for processing files of Oxford Nanopore reads

* Mon Jun 09 2014 Shane Sturrock <shane@biomatters.com> - 0.11.2-1
- Fixed incorrect warn/fail defaults for per-seq quality plot
- Fixed memory leaks in Kmer and per-seq quality modules
- Added an option to use a custom limits file
- Fixed a bug in the naming of the folder inside the zip output file
- Fixed a bug in the --extract option

* Tue Jun 01 2014 Sidney Markowitz <sidney@biomatters.com> - 0.11.1-1
- Added configurable warn/fail thresholds for all modules
- Allow modules to be selectively turned off
- Added a per-tile quality plot for Illumina libraries
- Added an adapter content plot
- Improved the duplication plot
- Improved the Kmer module
- Used embedded graphics in the HTML output so you can distribute a single file
- Added the ability to read data from stdin
- Changed how base grouping works to better accommodate long reads
- Dropped support for Solexa64 format (NB not Phred 64 which is still supported)

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.10.1-3
- Set $RealBin correcting in /usr/bin/fastqc
- Add bzip2 and SAM JAR files to RPM

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.10.1-2
- Install Java files into correct location

* Thu Jul 25 2012 Carl Jones <carl@biomatters.com> - 0.10.1-1
- Initial build.
