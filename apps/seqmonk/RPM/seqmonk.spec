Name:		seqmonk
Version:	0.32.0
Release:	1%{?dist}
Summary:	A tool to visualise and analyse high throughput mapped sequence data
Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.bioinformatics.babraham.ac.uk/projects/seqmonk/
Source0:	http://www.bioinformatics.babraham.ac.uk/projects/seqmonk/seqmonk_v%{version}.zip
Source1:	seqmonk-icons.tar.gz
Source2:	seqmonk.desktop
Patch0:		seqmonk-classpath.patch
Requires:	java-1.7.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
SeqMonk is a program to enable the visualisation and analysis of mapped 
sequence data. It was written for use with mapped next generation sequence 
data but can in theory be used for any dataset which can be expressed as a 
series of genomic positions.

%prep
%setup -q -n SeqMonk
%patch0 -p0

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 seqmonk %{buildroot}/%{_bindir}
/bin/cp -r uk/ %{buildroot}/%{_javadir}/%{name}/
/bin/cp -r com/ %{buildroot}/%{_javadir}/%{name}/

# Icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/
tar xf %{SOURCE1} -C %{buildroot}%{_datadir}/icons/hicolor/

# .desktop
mkdir -p %{buildroot}%{_datadir}/applications/
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet /usr/share/icons/hicolor
fi

%files
%defattr(-,root,root,-)
%doc README.txt LICENSE.txt RELEASE_NOTES.txt
/usr/bin/seqmonk
/usr/share/java/seqmonk/*
/usr/share/applications/seqmonk.desktop
/usr/share/icons/hicolor/*

%changelog
* Thu Aug 20 2015 Shane Sturrock <shane@biomatters.com> - 0.32.0-1
- Added a duplication plot based around DupRadar
- Added a binomial stats filter for bisulphite analysis where there is a 
  global methylation change
- Fixed a bug in preferences editing for systems with R in the path
- Added a data export option to the quantitation trend plot
- Various bug and stability fixes

* Tue Jul 07 2015 Shane Sturrock <shane@biomatters.com> - 0.31.1-1
- Changed paired end SAM/BAM import to not rely on the TLEN SAM field
- Fixed a bug in logistic regression when only analysing probes on a single 
  chromosome
- Updated the MA plot to the same feature set as the scatterplot
- Added version checking to R installation validation

* Thu Jul 02 2015 Shane Sturrock <shane@biomatters.com> - 0.31.0-1
- Added DNA contamination estimation and paired end support to the RNA-Seq 
  pipeline
- Added an import filter for methylkit data
- Added an option to save the underlying data in QC plots
- Added an option to extract the centres of reads to the visible stores parser
- Added a for/rev binomial statistics test
- Improved the UI when long names are used for data stores or probe lists
- Various bug fixes

* Wed May 13 2015 Shane Sturrock <shane@biomatters.com> - 0.30.2-1
- Worked around an Adobe Illustrator bug which was causing SeqMonk SVG 
  files to not load cleanly
- Added a work round for installing R dependencies for unprivileged users 
  without a local R library
- Added better up-front data validation for the DESeq2 and EdgeR filters

* Mon May 04 2015 Shane Sturrock <shane@biomatters.com> - 0.30.1-1
- Fixed a bug in the installation of the DESeq2 R dependency

* Fri Apr 24 2015 Sidney Markowitz <sidney@biomatters.com> - 0.30.0-1
- Added ability for SeqMonk to link to R for some analyses
- Added a DESeq2 statistical filter
- Added a EdgeR statistical filter
- Added a logistic regression statistical filter
- Added a gene set intensity difference filter
- Added an import filter for Bismark cov files
- Added an import filter for QuasR files

* Mon Mar 16 2015 Shane Sturrock <shane@biomatters.com> - 0.29.0-2
- switch to Java 7 for CentOS 7

* Wed Dec 17 2014 Shane Sturrock <shane@biomatters.com> - 0.29.0-1
- Added and Even Coverage probe generator
- Added an exportable scale bar for the chromosome view
- Added a number of ways to show varaibility in replicate sets
- Added auto-dection of the most likely BAM import options
- Expanded and grouped the data track display options
- Added an active transcription quantitation pipeline
- Added the ability to re-order visible tracks based on the Data Store tree
- Added new options to the read position probe generator
- Improved the display of data tracks when large numbers of tracks are shown

* Tue Oct 28 2014 Shane Sturrock <shane@biomatters.com> - 0.28.0-1
- Added more options to the Distance to Feature quantitation
- Improved the efficiency with which large HiC heatmaps are drawn
- Added a tabular view to show the levels of overlaps between a set
  of probe lists
- Added the Star Wars plot for plotting means and confidence intervals
  in a manner similar to a boxplot.
- Added a genetrap quantitation pipeline
- Added a proportion of library statistics filter
- Added a euclidian distance mode for heirarcical clustering
- Added an RNA-Seq QC plot
- Added the ability to normalise in groups when doing Match Distributions
- Added an option to go to a centred window of a specified size
- Changed the quantitation model to allow probes in individual samples to
  not store a value.  Applied this to Bisulphite Quantitation rather than
  using flag values to indicate probes which didn't have enough data to 
  calculate a value. Changed the default filtering options to be much more
  lax.
- Added a BAM import option to choose to import only primary alignments from
  a BAM file, and made this the default.
- Added a popup menu item to make it easy to convert probe lists into annotation
  tracks
- Added a small RNA QC plot
- Added an import option for text files which contain a position and a count
- Added an option to do bulk find/replace renaming of DataSets
- Added a new Percentile Feature Probe Generator which makes sets of probes
  spaced evenly over features.
- Fixed a bug in the MACS caller when there were very low numbers of reads.
- Added a display option to show data as coloured blocks rather than bars.
- Added the option to reverse any selected gradient in the chromosome view.
- Added an option to design running window probes only within the currently
  visible region.

* Mon Jan 13 2014 Shane Sturrock <shane@biomatters.com> - 0.27.0-1
- Made improvements to the RNA-Seq and HiC Analysis tools
- Added a tool to automatically group DataSets based on their names
- Added options to downsample datasets or filter reads by their length
- Fixed a p-value correction bug in large HiC heatmaps
- Fixed a bug which occurred when sorting very large numbers of reads
- Fixed a bug when using GFFv3 files to create custom genomes
- Added warnings to pipelines which wipe out existing probe sets
* Tue Oct 29 2013 Shane Sturrock <shane@biomatters.com> - 0.26.0-1
- SeqMonk v0.26.0 adds a critical fix for the new OSX Mavericks release
  and also adds some new functionality to make it easier to deal with 
  incomplete genome assemblies or other custom genomes.
- Fixed the launcher on OSX to adapt to changes in OSX Mavericks
  which broke the auto configuration code.
- Fixed a bug which caused the program to hang after downloading
  a new genome in response to opening an existing seqmonk project.
- Added a new graphical tool to aid in the creation of custom genomes
  meaning that you can now create custom genomes including pseudo
  chromosomes from either a collection of fasta files or a GTF file.
* Tue Sep 10 2013 Shane Sturrock <shane@biomatters.com> - 0.25.0-1
- Added a quantitation trend plot to allow the examination of complex pattersn around features
- Added a muti-lane chi-square test for allele specific analysis and other applications
- Improved the options in the feature probe generator
- Allow multiple data stores in the aligned probes plot and allow custom sorting
- Allow filtering of reads against features when re-importing
- Added nice colour options to the hierarchical cluster plot
- Added a domainogram plot to look at quantitations at different levels
- Added an option to find sets of features using a list of search terms
- Added the ability to add comments to probe lists so you can remember why you did what you did
- Added a probe list description report to completely record the results of an analysis
- Added a subset normalisation quantitation method
- Reorganised the relative quantitation method to allow for specific pairings of references and samples
- Lots of other bug fixes and improvements
* Mon Feb 25 2013 Carl Jones <carl@biomatters.com> - 0.24.1-0
- New upstream release

* Thu Jan 24 2013 Carl Jones <carl@biomatters.com> - 0.24-0
- New upstream release

* Thu Jan 24 2013 Carl Jones <carl@biomatters.com> - 0.23.1-2
- Add desktop icons, menu

* Wed Dec 12 2012 Carl Jones <carl@biomatters.com> - 0.23.1-1
- New upstream release
* Wed Dec 05 2012 Carl Jones <carl@biomatters.com> - 0.23.0-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 0.22.0-2
- Use 0.22 tarball rather than 0.21
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 0.22.0-1
- New upstream release
* Fri Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.21.0-3
- Fixed Java paths
* Fri Aug 02 2012 Carl Jones <carl@biomatters.com> - 0.21.0-2
- Move bin/seqmonk to seqmonk.
* Fri Aug 02 2012 Carl Jones <carl@biomatters.com> - 0.21.0-1
- Initial build.
