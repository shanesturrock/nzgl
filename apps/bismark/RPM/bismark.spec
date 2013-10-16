Name:		bismark
Version:	0.10.0
Release:	1%{?dist}
Summary:	A tool to map bisulfite converted sequence reads and determine cytosine methylation states.
Group:		Applications/Engineering
License:	GNU GPL v3
URL:		http://www.bioinformatics.babraham.ac.uk/projects/bismark/
Source0:	http://www.bioinformatics.babraham.ac.uk/projects/bismark/bismark_v%{version}.tar.gz
Requires:	bowtie
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

Bismark is a program to map bisulfite treated sequencing reads to a genome of interest 
and perform methylation calls in a single step. The output can be easily imported into
a genome viewer, such as SeqMonk, and enables a researcher to analyse the methylation
levels of their samples straight away.

%prep
%setup -q -n %{name}_v%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 bismark %{buildroot}/%{_bindir}
install -m 0755 bismark_genome_preparation %{buildroot}/%{_bindir}
install -m 0755 bismark_methylation_extractor %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Bismark_User_Guide_v%{version}.pdf license.txt RELEASE_NOTES.txt
%{_bindir}/bismark
%{_bindir}/bismark_genome_preparation
%{_bindir}/bismark_methylation_extractor

%changelog
* Thu Oct 17 2013 Shane Sturrock <shane@biomatters.com> - 0.10.0-1
- Bismark - The option --prefix <some.prefix> does now also work for the C->T and G->A 
  transcribed temporary files to allow multiple instances of Bismark to be run on the same 
  file in the same folder (e.g. using Bowtie and Bowtie 2 or some stricter and laxer 
  parameters concurrently).
- Bismark Genome Preparation - Made a couple of changes to make the genome preparation fully 
  non-interactive. This means that the path to the genome folder and to Bowtie (1/2) have to 
  be specified up front (for Bowtie (1/2) it is otherwise assumed that it is in the PATH). 
  Furthermore, already existing bisulfite indices in the target folder will be overwritten 
  and the user is no longer prompted if he agrees to this. We got rid of this because 
  creating a second index (Bowtie 1 as well as 2) in the same folder in non-interactive 
  mode got stuck in loops asking whether it is alright to proceed or not, generating 
  therabyte sized log files without ever starting doing anything useful...).
- Methylation extractor - The methylation extractor will now delete unused methylation 
  context files (e.g. CTOT and CTOB files for a directional library). I finally got round to 
  implementing this after having to delete manually thousands of files containing the header 
  line only...
- bismark2bedGraph - Dropped the option -k3,3 from the sort command to result in a dramatic 
  speed increase while sorting. This option had been used previously to enable sorting by 
  chromosome in addition to position, but should no longer be needed because the files are 
  being read in sorted by chromosome already.  This module does now produces these two 
  output files: 
    (1) A bedGraph file, which now contains a header line: 'track type=bedGraph' The 
        genomic start coords are 0-based, the end coords are 1-based.
    (2) A coverage file ending in .cov. This file replaces the former 'bedGraph --counts' 
        file and is required to proceed with the subsequent step to generate a genome-wide 
        cytosine report (the module doing this has been renamed to coverage2cytosine to 
        reflect this file name change. 
- coverage2cytosine - Changed the name of this module from 'bedGraph2cytosine' to 
  'coverage2cytosine' to reflect the change that this module now requires the methylation 
  coverage file produced by the bismark2bedGraph module, ending in .cov (this coverage file 
  replaces the former "bedGraph --counts" output). Previously, the cytosine report would 
  always report every C position in any context, even though the default should have 
  reported CpG positions only. This has now been fixed.
- bismark2report - Changed the behavior of this module to automatically find all Bismark 
  mapping reports in the current working directory, and to try and work out whether the 
  optional reports are present as well (i.e. deduplication, splitting and M-bias reports). 
  This uses the file basename and will fail if the files have been renamed at any stage. 
  Specifying file names using the individual options takes precedence over the automatic 
  detection.
- deduplicate_bismark - Renamed the rather long deduplication script to this slightly 
  shorter one. Also added some filehandle closing statements that might have caused 
  buffering issues under certain circumstances.

* Mon Aug 26 2013 Shane Sturrock <shane@biomatters.com> - 0.9.0-2
- Peter Stockwell confirms this works for him so putting into stable repo

* Mon Aug 19 2013 Shane Sturrock <shane@biomatters.com> - 0.9.0-1
- New upstream release - release notes don't say why, put into testing repo

* Mon Jul 29 2013 Shane Sturrock <shane@biomatters.com> - 0.8.3-1
- New upstream release

* Fri Jul 26 2013 Shane Sturrock <shane@biomatters.com> - 0.8.2-1
- New upstream release

* Wed Jul 17 2013 Shane Sturrock <shane@biomatters.com> - 0.8.1-1
- New upstream release

* Mon Jul 15 2013 Shane Sturrock <shane@biomatters.com> - 0.8.0-1
- New upstream release

* Mon Mar 18 2013 Shane Sturrock <shane@biomatters.com> - 0.7.9-1
- New upstream release

* Mon Mar 4 2013 Shane Sturrock <shane@biomatters.com> - 0.7.8-1
- New upstream release

* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 0.7.7-1
- New upstream release

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.7.6-1
- New upstream release

* Wed Jul 24 2012 Carl Jones <carl@biomatters.com> - 0.7.5-1
- Initial build.
