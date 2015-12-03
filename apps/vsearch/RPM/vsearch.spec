Name:		vsearch
Version:	1.9.4
Release:	1%{?dist}
Summary:	An alternative to the USEARCH
Group:		Applications/Engineering
License:	GPL3
URL:		https://github.com/torognes/vsearch
Source0: 	vsearch-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	autogen,automake,autoconf

%description
VSEARCH stands for vectorized search, as the tool takes advantage of
parallelism in the form of SIMD vectorization as well as multiple threads to
perform accurate alignments at high speed. VSEARCH uses an optimal global
aligner (full dynamic programming Needleman-Wunsch), in contrast to USEARCH
which by default uses a heuristic seed and extend aligner. This results in more
accurate alignments and overall improved sensitivity (recall) with VSEARCH,
especially for alignments with gaps.

%prep
%setup -q

%build
./autogen.sh
./configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 bin/vsearch %{buildroot}%{_bindir}
install -m 0644 man/vsearch.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/vsearch
%{_mandir}/man1/vsearch.1*

%changelog
* Fri Dec 04 2015 Shane Sturrock <shane@biomatters.com> - 1.9.4-1
- Fixed incrementation of counter when relabeling dereplicated sequences.

* Fri Nov 20 2015 Shane Sturrock <shane@biomatters.com> - 1.9.3-1
- Workaround for missing x86intrin.h with old compilers

* Wed Nov 18 2015 Shane Sturrock <shane@biomatters.com> - 1.9.2-1
- Fixed a bug in computation of some values with --fastq_stats.

* Mon Nov 16 2015 Shane Sturrock <shane@biomatters.com> - 1.9.1-1
- Fixed memory leak and a bug in score computation in fastq_mergepairs, and
  improved speed.

* Fri Nov 13 2015 Shane Sturrock <shane@biomatters.com> - 1.9.0-1
- Added the --fastq_mergepairs command and associated options. This command has
  not been tested well yet.
- Included additional files to avoid dependency of autoconf for compilation. 
- Fixed an error where identifiers in fasta headers where not truncated at
  tabs, just spaces. 
- Fixed a bug in detection of the file format (FASTA/FASTQ) of a gzip
  compressed input file.

* Wed Nov 04 2015 Shane Sturrock <shane@biomatters.com> - 1.8.1-1
- This release fixes some compatibility issues with older OS X versions as well
  as with QIIME and usearch61.
  - OS X version 10.7 and newer should now be properly supported. 
  - The --threads option will now accept floating point arguments for
    compatibility with usearch61 and QIIME (specifically
    identify_chimeric_seqs.py).

* Wed Oct 21 2015 Shane Sturrock <shane@biomatters.com> - 1.8.0-1
- Added --search_exact, --fastx_mask and --fastq_convert commands. 
- Changed most commands to read FASTQ input files as well as FASTA files. 
- Modified --fastx_revcomp and --fastx_subsample to also write FASTQ files.

* Mon Oct 19 2015 Shane Sturrock <shane@biomatters.com> - 1.7.0-1
- Added relabel_keep option

* Mon Oct 12 2015 Shane Sturrock <shane@biomatters.com> - 1.6.0-1
- Added relabelling options for shuffle and added xsize option for several
  commands.

* Thu Oct 08 2015 Shane Sturrock <shane@biomatters.com> - 1.5.0-1
- Initial NZGL release

