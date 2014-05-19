%define debug_package %{nil}

Name:        legacy-blast
Version:     2.2.26
Release:     1
Source0:     blast-%{version}-x64-linux.tar.gz
Summary:     BLAST finds regions of similarity between biological sequences. 
Exclusiveos: linux
Group:       NCBI/BLAST
License:     Public Domain
BuildArch:   x86_64
BuildRoot:   %{_tmppath}/blast-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The legacy NCBI Basic Local Alignment Search Tool (BLAST) finds regions of
local similarity between sequences. The program compares nucleotide or
protein sequences to sequence databases and calculates the statistical
significance of matches. BLAST can be used to infer functional and
evolutionary relationships between sequences as well as help identify
members of gene families.

%prep 
%setup -q -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}/blast
install -m 755 -d %{buildroot}/%{_bindir}/blast/bin
install -m 755 blast-%{version}/bin/bl2seq blast-%{version}/bin/blastall blast-%{version}/bin/blastclust blast-%{version}/bin/blastpgp blast-%{version}/bin/copymat blast-%{version}/bin/fastacmd blast-%{version}/bin/formatdb blast-%{version}/bin/formatrpsdb blast-%{version}/bin/impala blast-%{version}/bin/makemat blast-%{version}/bin/megablast blast-%{version}/bin/rpsblast blast-%{version}/bin/seedtop %{buildroot}/%{_bindir}/blast/bin/
install -m 755 -d %{buildroot}/%{_bindir}/blast/data
install -m 644 blast-%{version}/data/asn2ff.prt blast-%{version}/data/BLOSUM45 blast-%{version}/data/BLOSUM62 blast-%{version}/data/BLOSUM80 blast-%{version}/data/bstdt.val blast-%{version}/data/ecnum_ambiguous.txt blast-%{version}/data/ecnum_specific.txt blast-%{version}/data/featdef.val blast-%{version}/data/gc.val blast-%{version}/data/humrep.fsa blast-%{version}/data/KSat.flt blast-%{version}/data/KSchoth.flt blast-%{version}/data/KSgc.flt blast-%{version}/data/KShopp.flt blast-%{version}/data/KSkyte.flt blast-%{version}/data/KSpcc.mat blast-%{version}/data/KSpur.flt blast-%{version}/data/KSpyr.flt blast-%{version}/data/lineages.txt blast-%{version}/data/makerpt.prt blast-%{version}/data/objprt.prt blast-%{version}/data/organelle_products.prt blast-%{version}/data/PAM30 blast-%{version}/data/PAM70 blast-%{version}/data/product_rules.prt blast-%{version}/data/pubkey.enc blast-%{version}/data/seqcode.val blast-%{version}/data/sequin.hlp blast-%{version}/data/sgmlbb.ent blast-%{version}/data/taxlist.txt blast-%{version}/data/UniVec_Core.nhr blast-%{version}/data/UniVec_Core.nin blast-%{version}/data/UniVec_Core.nsq blast-%{version}/data/UniVec.nhr blast-%{version}/data/UniVec.nin blast-%{version}/data/UniVec.nsq %{buildroot}/%{_bindir}/blast/data/
install -m 755 -d %{buildroot}/%{_bindir}/blast/doc
install -m 644 blast-%{version}/doc/bl2seq.html blast-%{version}/doc/blastall.html blast-%{version}/doc/blastclust.html blast-%{version}/doc/blastdb.html blast-%{version}/doc/blastftp.html blast-%{version}/doc/blast.html blast-%{version}/doc/blastpgp.html blast-%{version}/doc/fastacmd.html blast-%{version}/doc/filter.html blast-%{version}/doc/formatdb.html blast-%{version}/doc/formatrpsdb.html blast-%{version}/doc/history.html blast-%{version}/doc/impala.html blast-%{version}/doc/index.html blast-%{version}/doc/megablast.html blast-%{version}/doc/netblast.html blast-%{version}/doc/rpsblast.html blast-%{version}/doc/scoring.pdf blast-%{version}/doc/web_blast.pl %{buildroot}/%{_bindir}/blast/doc/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/*

%changelog
* Mon May 19 2014 Shane Sturrock <shane@biomatters.com> - 2.2.26-1
- Initial import of legacy blast
