Summary:	Sequence assembler for short reads
Name:		abyss
Version:	1.5.2
Release:	3%{?dist}
License:	GPLv3
Group:		Applications/Engineering
URL:		http://www.bcgsc.ca/platform/bioinfo/software/abyss
Source0:	http://www.bcgsc.ca/platform/bioinfo/software/abyss/releases/%{version}/abyss-%{version}.tar.gz
Source1:	boost_1_55_0.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	openmpi-devel sparsehash-devel
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
* Thu Feb 19 2015 Shane Sturrock <shane@biomatters.com> - 1.5.2-3
- Add -w compiler flag which ignores warnings to allow build on CentOS 7

* Tue Feb 17 2015 Shane Sturrock <shane@biomatters.com> - 1.5.2-2
- Compatibility with CentOS 7

* Thu Aug 21 2014 Shane Sturrock <shane@biomatters.com> - 1.5.2-1
- Initial release
