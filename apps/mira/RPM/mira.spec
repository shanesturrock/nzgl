%define debug_package %{nil}

Name:        mira
Version:     4.9.5_2
Release:     1
Summary:     MIRA whole genome shotgun and EST sequence assembler
Exclusiveos: linux
Group:       Applications/Engineering
License:     GPLv2
URL:         http://sourceforge.net/projects/mira-assembler/
Source0:     %{name}_%{version}_linux-gnu_x86_64_static.tar.bz2
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:   x86_64

%description
MIRA is a whole genome shotgun and EST sequence assembler for Sanger,
454, Solexa (Illumina), IonTorrent data and PacBio (the later at the
moment only CCS and error-corrected CLR reads). It can be seen as a
Swiss army knife of sequence assembly developed and used in the past
16 years to get assembly jobs done efficiently - and especially
accurately. That is, without actually putting too much manual work
into finishing the assembly.

%prep 
%setup -q -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/bin/mira %{buildroot}/%{_bindir}/mira
/bin/ln -sf mira %{buildroot}/%{_bindir}/mirabait
/bin/ln -sf mira %{buildroot}/%{_bindir}/miraconvert
/bin/ln -sf mira %{buildroot}/%{_bindir}/miramem
# install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/bin/mirabait %{buildroot}/%{_bindir}/mirabait
# install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/bin/miraconvert %{buildroot}/%{_bindir}/miraconvert
# install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/bin/miramem %{buildroot}/%{_bindir}/miramem
install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/scripts/fasta2frag.tcl %{buildroot}%{_bindir}/fasta2frag.tcl
install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/scripts/fixACE4consed.tcl %{buildroot}%{_bindir}/fixACE4consed.tcl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mira
%{_bindir}/mirabait
%{_bindir}/miraconvert
%{_bindir}/miramem
%{_bindir}/fasta2frag.tcl
%{_bindir}/fixACE4consed.tcl

%changelog
* Mon May 18 2015 Shane Sturrock <shane@biomatters.com> - 4.9.5_2-1
- Upstream update

* Mon May 04 2015 Shane Sturrock <shane@biomatters.com> - 4.9.4-1
- Upstream update

* Mon Nov 10 2014 Shane Sturrock <shane@biomatters.com> - 4.9.3-1
- Upstream update

* Mon Nov 03 2014 Shane Sturrock <shane@biomatters.com> - 4.9.2-1
- Upstream update

* Wed Oct 29 2014 Shane Sturrock <shane@biomatters.com> - 4.9.1-1
- MIRA
  - improvement: better overall assemblies.
  - improvement: mira can now use kmer sizes up to 256 bases
  - improvement: new functionality to automatically determine optimal number of
    passes and different kmer sizes in a denovo assembly (see -AS:nop=0 below)
  - improvement: new parameter -AS:kms as one-stop-shop to configure number of
    passes and used kmer sizes. E.g.: -AS:kms=17,31,63,127,127
  - improvement: better assembly of data with self-hybridising read chimeras
    (seen in Illumina 300bp data). Not perfect yet, but an improvement
  - improvement: in manifest, new segment_naming scheme "SRA" for reads comming
    from the short read archive. New attribute 'rollcomment'.
  - improvement: new MIRA parameter -CO:cmrs for better control on reads
    incorporated in contigs
  - improvement: faster mapping of long Illumina reads with lots of differences
  - improvement: MIRA now uses the SIOc tag also in mapping. Allows finding
    ploidy differences in multiploid genomes.
  - improvement: new info file "*_readgroups.txt” for statistics on paired reads
  - improvement: some temporary files compressed to minimise impact on disk
    space.

- MIRABAIT
  - all new mirabait functionality: work on read pairs; multiple bait files;
    simultaneous filtering of matches and non matches; safety checks on -L data
  - change: mirabait lowercases all sequences, uppercasing just kmers hitting
    bait sequences. Use -c if not wanted.
  - improvement: mirabait can now use kmer sizes up to 256 bases

* Thu Aug 21 2014 Shane Sturrock <shane@biomatters.com> - 4.0.2-1
- Initial import of MIRA
