Summary:	Sequence assembler for short reads
Name:		abyss
Version:	2.0.0
Release:	1%{?dist}
License:	GPLv3
Group:		Applications/Engineering
URL:		http://www.bcgsc.ca/platform/bioinfo/software/abyss
Source0:	http://www.bcgsc.ca/platform/bioinfo/software/abyss/releases/%{version}/abyss-%{version}.tar.gz
Source1:	boost_1_56_0.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	openmpi-devel sparsehash-devel sqlite-devel
Requires:	openmpi

%description
ABySS is a de novo, parallel, paired-end sequence assembler that is designed 
for short reads. The single-processor version is useful for assembling genomes 
up to 100 Mbases in size. The parallel version is implemented using MPI and 
is capable of assembling larger genomes.

%prep
%setup -q -n abyss-%{version}

%build
/bin/tar jxf %{SOURCE1} -C .
./configure CFLAGS=-w CXXFLAGS=-w
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cd bin
install -m 0755 abyss-bowtie abyss-bowtie2 abyss-bwa abyss-bwasw abyss-bwamem abyss-fatoagp abyss-kaligner abyss-pe abyss-samtoafg abyss-tabtomd abyss-bloom-dist.mk %{buildroot}/%{_bindir}
cd ..
install -m 0755 ABYSS/ABYSS %{buildroot}/%{_bindir}
/bin/ln -sf ABYSS %{buildroot}/%{_bindir}/ABYSS-P
install -m 0755 AdjList/AdjList %{buildroot}/%{_bindir}
install -m 0755 DataLayer/abyss-fac %{buildroot}/%{_bindir}
install -m 0755 DataLayer/abyss-tofastq %{buildroot}/%{_bindir}
install -m 0755 Graph/abyss-gc %{buildroot}/%{_bindir}
install -m 0755 Graph/abyss-todot %{buildroot}/%{_bindir}
install -m 0755 Align/abyss-align %{buildroot}/%{_bindir}
install -m 0755 Align/abyss-mergepairs %{buildroot}/%{_bindir}
install -m 0755 Bloom/abyss-bloom %{buildroot}/%{_bindir}
install -m 0755 BloomDBG/abyss-bloom-dbg %{buildroot}/%{_bindir}
install -m 0755 Sealer/abyss-sealer %{buildroot}/%{_bindir}
install -m 0755 Konnector/konnector %{buildroot}/%{_bindir}
install -m 0755 Consensus/Consensus %{buildroot}/%{_bindir}
install -m 0755 DAssembler/DAssembler %{buildroot}/%{_bindir}
install -m 0755 DistanceEst/DistanceEst %{buildroot}/%{_bindir}
install -m 0755 DistanceEst/DistanceEst-ssq %{buildroot}/%{_bindir}
install -m 0755 KAligner/KAligner %{buildroot}/%{_bindir}
install -m 0755 Layout/abyss-layout %{buildroot}/%{_bindir}
install -m 0755 LogKmerCount/logcounter %{buildroot}/%{_bindir}
cd Map
install -m 0755 abyss-index abyss-map abyss-map-ssq abyss-overlap %{buildroot}/%{_bindir}
cd ..
cd MergePaths
install -m 0755 MergePaths MergeContigs PathConsensus %{buildroot}/%{_bindir}
cd ..
install -m 0755 Overlap/Overlap %{buildroot}/%{_bindir}
cd ParseAligns
install -m 0755 abyss-fixmate abyss-fixmate-ssq ParseAligns %{buildroot}/%{_bindir}
cd ..
install -m 0755 PathOverlap/PathOverlap %{buildroot}/%{_bindir}
install -m 0755 PopBubbles/PopBubbles %{buildroot}/%{_bindir}
cd Scaffold
install -m 0755 abyss-scaffold abyss-junction abyss-longseqdist %{buildroot}/%{_bindir}
cd ..
install -m 0755 SimpleGraph/SimpleGraph %{buildroot}/%{_bindir}
install -m 0755 FilterGraph/abyss-filtergraph %{buildroot}/%{_bindir}
install -m 0755 GapFiller/abyss-gapfill %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/abyss-bowtie
%{_bindir}/abyss-bowtie2
%{_bindir}/abyss-bwa
%{_bindir}/abyss-bwasw
%{_bindir}/abyss-bwamem
%{_bindir}/abyss-fatoagp
%{_bindir}/abyss-kaligner
%{_bindir}/abyss-pe
%{_bindir}/abyss-samtoafg
%{_bindir}/abyss-sealer
%{_bindir}/abyss-tabtomd
%{_bindir}/abyss-bloom-dist.mk
%{_bindir}/ABYSS
%{_bindir}/ABYSS-P
%{_bindir}/AdjList
%{_bindir}/abyss-fac
%{_bindir}/abyss-tofastq
%{_bindir}/abyss-gc
%{_bindir}/abyss-todot
%{_bindir}/abyss-align
%{_bindir}/abyss-mergepairs
%{_bindir}/abyss-bloom
%{_bindir}/abyss-bloom-dbg
%{_bindir}/konnector
%{_bindir}/Consensus
%{_bindir}/DAssembler
%{_bindir}/DistanceEst
%{_bindir}/DistanceEst-ssq
%{_bindir}/KAligner
%{_bindir}/abyss-layout
%{_bindir}/logcounter
%{_bindir}/abyss-index
%{_bindir}/abyss-map
%{_bindir}/abyss-map-ssq
%{_bindir}/abyss-overlap
%{_bindir}/MergePaths
%{_bindir}/MergeContigs
%{_bindir}/PathConsensus
%{_bindir}/Overlap
%{_bindir}/abyss-fixmate
%{_bindir}/abyss-fixmate-ssq
%{_bindir}/ParseAligns
%{_bindir}/PathOverlap
%{_bindir}/PopBubbles
%{_bindir}/abyss-scaffold
%{_bindir}/abyss-junction
%{_bindir}/abyss-longseqdist
%{_bindir}/SimpleGraph
%{_bindir}/abyss-filtergraph
%{_bindir}/abyss-gapfill

%changelog
* Mon Sep 05 2016 Shane Sturrock <shane@biomatters.com> - 2.0.0-1
- New Bloom filter mode for assembly => assemble large genomes 
  with minimal memory (e.g. 34G for H. sapiens) 
- Update param defaults for modern Illumina data 
- Make sqlite3 an optional dependency 
- abyss-bloom: 
  - New 'compare' command for bitwise comparison of Bloom filters 
  - New 'kmers' command for printing k-mers that match a Bloom filter 
- abyss-bloom-dbg: 
  - New preunitig assembler that uses Bloom filter 
  - Add 'B' param (Bloom filter size) to 'abyss-pe' command to enable 
    Bloom filter mode 
  - See README.md and '--help' for further instructions 
- abyss-fatoagp: 
  - Mask scaftigs shorter than 50bp with 'N's (short scaftigs 
    were causing problems with NCBI submission) 
- abyss-pe: 
  - Update default parameter values for modern Illumina data 
  - Change 'l=k' => 'l=40' 
  - Change 's=200' => 's=1000' 
  - Change 'S=s' => 'S=1000-10000' (do a param sweep of 'S') 
  - Use 'DistanceEst --mean' for scaffolding stage, instead of 
    the default '--mle' 
- abyss-sealer: 
  - New '--max-gap-length' ('-G') option to replace unintuitive 
    '--max-frag'; use of '--max-frag' is now deprecated 
  - Require user to explicitly specify Bloom filter size (e.g. 
    '-b40G') 
  - Report false positive rate (FPR) when building/loading Bloom 
    filters 
  - Don't require input FASTQ files when using pre-built Bloom 
    filter files 
- konnector: 
  - Fix bug causing output read 2 file to be empty 
  - New percent sequence identity options ('-x' and '-X') 
  - New '--alt-paths-mode' option to output alternate connecting 
    paths between read pairs 
- README.md: 
  - Fix documentation of ABYSS and abyss-pe parameters 

* Tue Jun 02 2015 Shane Sturrock <shane@biomatters.com> - 1.9.0-1
- New paired de Bruijn graph mode for assembly. 
- First official release of Sealer, a tool for closing scaffold gaps by 
  navigating a Bloom filter de Bruijn graph. 
- New outward extension feature for Konnector to generate long pseudo-reads. 
- Support for the DIDA (Distributed Indexing Dispatched Alignment) framework, 
  for computing sequence alignments in parallel across multiple machines. 
- Unit tests can now be run easily with 'make check', without external 
  dependencies. 
- abyss-bloom: 
  - abyss-bloom 'build' command now supports -j option for multi-threaded 
    Bloom filter construction. 
- abyss-map: 
  - New --protein option for mapping protein sequences. 
_ abyss-pe: 
  - New paired de Bruijn graph mode for assembly. Enable by setting `k` to the 
    k-mer pair span and `K` to size of an individual k-mer in a k-mer pair. 
    See README.md for further details. 
  - New `aligner=dida` option for using the DIDA parallel alignment framework. 
    See the DIDA section of the abyss-pe man page for usage details. 
  - New `graph=gfa` option to use the GFA (Graphical Fragment Assembly) format 
    for intermediate graph files. 
- abyss-sealer: 
  - New tool for closing scaffold gaps by navigating a Bloom filter de Bruijn 
    graph 
  - See Sealer/README.md or abyss-sealer man page for details and examples. 
- konnector: 
  - New --extend option for extending merged and unmerged reads outwards in 
    the de Bruijn graph.

* Thu Feb 19 2015 Shane Sturrock <shane@biomatters.com> - 1.5.2-3
- Add -w compiler flag which ignores warnings to allow build on CentOS 7

* Tue Feb 17 2015 Shane Sturrock <shane@biomatters.com> - 1.5.2-2
- Compatibility with CentOS 7

* Thu Aug 21 2014 Shane Sturrock <shane@biomatters.com> - 1.5.2-1
- Initial release
