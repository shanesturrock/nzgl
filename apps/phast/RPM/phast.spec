Name:		phast
Version:	1.3
Release:	1%{?dist}
Summary:	PHAST is a freely available software package for comparative and evolutionary genomics.
Group:		Applications/Engineering
License:	BSD Modified
URL:		http://compgen.bscb.cornell.edu/phast/index.php
Source0:	http://compgen.bscb.cornell.edu/phast/downloads/phast.v1_2_1.tgz
Source1:	http://www.netlib.org/clapack/clapack.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
PHAST is a freely available software package for comparative and evolutionary genomics. 
It consists of about half a dozen major programs, plus more than a dozen utilities for 
manipulating sequence alignments, phylogenetic trees, and genomic annotations. 

%prep
%setup -q -n %{name} -a 1

%build
cd CLAPACK-3.2.1
/bin/cp make.inc.example make.inc 
make f2clib
make blaslib
make lib
cd ../src
make CLAPACKPATH=$(pwd/../CLAPACK-3.2.1/)

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt
%{_bindir}/all_dists
%{_bindir}/base_evolve
%{_bindir}/chooseLines
%{_bindir}/clean_genes
%{_bindir}/consEntropy
%{_bindir}/convert_coords
%{_bindir}/display_rate_matrix
%{_bindir}/dless
%{_bindir}/dlessP
%{_bindir}/draw_tree
%{_bindir}/eval_predictions
%{_bindir}/exoniphy
%{_bindir}/hmm_train
%{_bindir}/hmm_tweak
%{_bindir}/hmm_view
%{_bindir}/indelFit
%{_bindir}/indelHistory
%{_bindir}/maf_parse
%{_bindir}/makeHKY
%{_bindir}/modFreqs
%{_bindir}/msa_diff
%{_bindir}/msa_split
%{_bindir}/msa_view
%{_bindir}/pbsDecode
%{_bindir}/pbsEncode
%{_bindir}/pbsScoreMatrix
%{_bindir}/pbsTrain
%{_bindir}/phast
%{_bindir}/phastCons
%{_bindir}/phastMotif
%{_bindir}/phastOdds
%{_bindir}/phyloBoot
%{_bindir}/phyloFit
%{_bindir}/phyloP
%{_bindir}/prequel
%{_bindir}/refeature
%{_bindir}/stringiphy
%{_bindir}/tree_doctor
%{_bindir}/treeGen
/usr/share/man/man7/*.gz
/opt/phast/*

%changelog
* Thu Jul 31 2014 Shane Sturrock <shane@biomatters.com> - 1.3-1
- Updated release
* Mon Sep 24 2012 Carl Jones <carl@biomatters.com> - 1.2.1-1
- Initial release.
