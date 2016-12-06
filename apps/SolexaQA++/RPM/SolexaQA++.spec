Name:		SolexaQA++
Version:	3.1.6
Release:	1%{?dist}
Summary:	Calculates quality statistics and creates visual representations of data quality from FASTQ files.
Group:		Applications/Engineering
License:	GPLv3
URL:		http://solexaqa.sourceforge.net/
Source0:	%{name}_v%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	x86_64

%description
SolexaQA is a Perl-based software package that calculates quality statistics 
and creates visual representations of data quality from FASTQ files generated 
by Illumina second-generation sequencing technology (“Solexa”).

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
#install -m 0755 Linux_x64/%{name} %{buildroot}/%{_bindir}
install -m 0755 %{name}_v%{version}/Linux_x64/%{name} %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}

%changelog
* Wed Dec 07 2016 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 3.1.6-1
- Minor bugfixes.

* Wed May 18 2016 Shane Sturrock <shane@biomatters.com> - 3.1.5-1
- Added subplot to histogram graph that shows the untrimmed length
  distribution.
- bugfixes.

* Tue Aug 18 2015 Shane Sturrock <shane@biomatters.com> - 3.1.4-1
- Bugfix in the analysis heatmap for variable length reads. In case a tile is
  entirely composed of reads shorter than all the other tiles, the squares for
  missing cycles are now painted gray. 
- Other minor bugfixes.

* Fri Jan 23 2015 Shane Sturrock <shane@biomatters.com> - 3.1.3-1
- Bugfix in the analysis histogram for variable length reads
- fix for a malloc error on some systems when the -d option with a trailing 
  forward slash is specified in dynamictrim
- the summary graph for lengthsort shows the sample(s) name(s) as the 
  graph title

* Tue Dec 09 2014 Shane Sturrock <shane@biomatters.com> - 3.1.2-1
- Bugfix in the analysis matrix graph: it now contemplates ".fastq" files 
  in which entire tiles are skipped, and names the tiles that are left 
  correctly on the heat map.
- Bugfix in LengthSort (single-end mode)

* Thu Oct 02 2014 Shane Sturrock <shane@biomatters.com> - 3.1-1
- Corrected a file naming bug when operating on .gz files (Linux and Mac only)
- improved command line output
- Analysis: 
  - added warning message for SRA-generated fastq files not containing the 
    tile number in the header
- DynamicTrim: 
  - added the [-a|--anchor] option, which allows trimming from the 3' end only
- LengthSort: New naming system for paired end reads:
  - Read 1 are named "[read1 name].paired"
  - Read 2 are named "[read2 name].paired"
  - Single reads are named "[read1 name].single"
  - Discarded reads are named "[read1 name].discard"

* Tue Aug 12 2014 Shane Sturrock <shane@biomatters.com> - 3.0-2
- Minor bug fix release
* Thu Aug 7 2014 Shane Sturrock <shane@biomatters.com> - 3.0-1
- Initial release of C++ based version
- Analysis (previously available as SolexaQA.pl): general performance
  improvements; the software can now process FASTQ files with variable read
  lengths, is compatible with Ion Torrent files (–t option), and .gz
  compressed files (Linux and OS X releases only). Minor cosmetic changes to
  graphs and command-line output have also been made.
- DynamicTrim: general performance improvements (up to 100% faster); bug fix
  for truncated graphs on variable length reads; compatible with .gz
  compressed files (Linux and OS X releases only); new progress bar in
  command-line output.
- LengthSort: paired-end mode includes a new option (–c) to remove
  non-matching reads from the two FASTQ files prior to processing; compatible
  with .gz compressed files (Linux and OS X releases only); new histogram
  output; new progress bar in command-line output.

