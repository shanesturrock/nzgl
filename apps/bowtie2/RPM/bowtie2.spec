Name:		bowtie2
Version:	2.2.1
Release:	0%{?dist}
Summary:	An ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences
Group:		Applications/Engineering
License:	GPLv3
URL:		http://bowtie-bio.sourceforge.net/bowtie2/index.shtml
Source0:	%{name}-%{version}-source.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Bowtie 2 is an ultrafast and memory-efficient tool for
aligning sequencing reads to long reference sequences. It is
particularly good at aligning reads of about 50 up to 100s or 1,000s
of characters, and particularly good at aligning to relatively long
(e.g. mammalian) genomes. Bowtie 2 indexes the genome with an FM Index
to keep its memory footprint small: for the human genome, its memory
footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local,
and paired-end alignment modes.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 bowtie2 %{buildroot}/%{_bindir}
install -m 0755 bowtie2-align-l %{buildroot}/%{_bindir}
install -m 0755 bowtie2-align-s %{buildroot}/%{_bindir}
install -m 0755 bowtie2-build %{buildroot}/%{_bindir}
install -m 0755 bowtie2-build-l %{buildroot}/%{_bindir}
install -m 0755 bowtie2-build-s %{buildroot}/%{_bindir}
install -m 0755 bowtie2-inspect %{buildroot}/%{_bindir}
install -m 0755 bowtie2-inspect-l %{buildroot}/%{_bindir}
install -m 0755 bowtie2-inspect-s %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc MANUAL NEWS VERSION AUTHORS TUTORIAL doc/
%{_bindir}/bowtie2
%{_bindir}/bowtie2-align-l
%{_bindir}/bowtie2-align-s
%{_bindir}/bowtie2-build
%{_bindir}/bowtie2-build-l
%{_bindir}/bowtie2-build-s
%{_bindir}/bowtie2-inspect
%{_bindir}/bowtie2-inspect-l
%{_bindir}/bowtie2-inspect-s
#%{_datadir}/bowtie/genomes
#%{_datadir}/bowtie/indexes
#%{_datadir}/bowtie/reads
#%{_datadir}/bowtie/scripts

%changelog
* Mon Mar 03 2014 Shane Sturrock <shane@biomatters.com> - 2.2.1-1
- Improved way in which index files are loaded for alignment. Should fix 
  efficiency problems on some filesystems.
- Fixed a bug that made older systems unable to correctly deal with bowtie 
  relative symbolic links.
- Fixed a bug that, for very big indexes, could determine to determine file 
  offsets correctly.
- Fixed a bug where using --no-unal option incorrectly suppressed 
  --un/--un-conc output.
- Dropped a perl dependency that could cause problems on old systems.
- Added --no-1mm-upfront option and clarified documentation for parameters 
  governing the multiseed heuristic.
* Wed Feb 12 2014 Shane Sturrock <shane@biomatters.com> - 2.2.0-1
- Improved index querying efficiency using "population count" instructions 
  available since SSE4.2
- Added support for large and small indexes, removing 4-billion-nucleotide 
  barrier. Bowtie 2 can now be used with reference genomes of any size.
- Fixed bug that could cause bowtie2-build to crash when reference length is 
  close to 4 billion.
- Added a CL: string to the @PG SAM header to preserve information about the 
  aligner binary and paramteres.
- Fixed bug that could cause bowtie2-build to crash when reference length is 
  close to 4 billion.
- No longer releasing 32-bit binaries. Simplified manual and Makefile 
  accordingly.
- Credits to the Intel® enabling team for performance optimizations included 
  in this release. Thank you!
- Phased out CygWin support. MinGW can still be used for Windows building.
- Added the .bat generation for Windows.
- Fixed some issues with some uncommon chars in fasta files.
- Fixed wrappers so bowtie can now be used with symlinks.

* Mon Feb 25 2013 Carl Jones <carl@biomatters.com> - 2.1.0-0
- New upstream release

* Tue Jan 29 2013 Carl Jones <carl@biomatters.com> - 2.0.6-1
- New upstream release

* Tue Jan 08 2013 Carl Jones <carl@biomatters.com> - 2.0.5-1
- New upstream release

* Thu Dec 20 2012 Carl Jones <carl@biomatters.com> - 2.0.4-1
- New upstream release

* Mon Dec 17 2012 Carl Jones <carl@biomatters.com> - 2.0.3-1
- New upstream release

* Mon Nov 05 2012 Carl Jones <carl@biomatters.com> - 2.0.2-1
- New upstream release

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 2.0.0.beta7-2
- Small SPEC file tweaks for licence, description  
