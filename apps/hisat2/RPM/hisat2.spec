Name:		hisat2
Version:	2.0.4
Release:	1%{?dist}
Summary:	A fast and sensitive alignment program for mapping NGS reads
Group:		Applications/Bioinformatics
License:	GPL 3.0
URL:		https://ccb.jhu.edu/software/hisat2/index.shtml
Source0:	ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-%{version}-source.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	bowtie2 python27

%description

HISAT2 is a fast and sensitive alignment program for mapping next-generation
sequencing reads (whole-genome, transcriptome, and exome sequencing data) to a
population of human genomes (as well as to a single reference genome). Based on
an extension of BWT for a graph [1], we designed and implemented a graph FM
index (GFM), an original approach and its first implementation to the best of
our knowledge. In addition to using one global GFM index that represents
general population, HISAT2 uses a large set of small GFM indexes that
collectively cover the whole genome (each index representing a genomic region
of 56 Kbp, with 55,000 indexes needed to cover human population). These small
indexes (called local indexes) combined with several alignment strategies
enable effective alignment of sequencing reads. This new indexing scheme is
called Hierarchical Graph FM index (HGFM). We have developed HISAT2 based on
the HISAT [2] and Bowtie 2 [3] implementations. See the HISAT2 website for more
information.

%prep
%setup -q
find . -type f -name '*.py' | xargs sed 's=python=python2.7=g' --in-place

%build
make clean
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
/bin/cp -r scripts %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r doc %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r example %{buildroot}/%{_libexecdir}/%{name}/
install -m 0755 extract_exons.py %{buildroot}%{_bindir}
install -m 0755 extract_splice_sites.py %{buildroot}%{_bindir}
install -m 0755 hisat2 %{buildroot}%{_bindir}
install -m 0755 hisat2-align-l %{buildroot}%{_bindir}
install -m 0755 hisat2-align-s %{buildroot}%{_bindir}
install -m 0755 hisat2-build %{buildroot}%{_bindir}
install -m 0755 hisat2_build_genotype_genome.py %{buildroot}%{_bindir}
install -m 0755 hisat2-build-l %{buildroot}%{_bindir}
install -m 0755 hisat2-build-s %{buildroot}%{_bindir}
install -m 0755 hisat2_extract_exons.py %{buildroot}%{_bindir}
install -m 0755 hisat2_extract_HLA_vars.py %{buildroot}%{_bindir}
install -m 0755 hisat2_extract_snps_haplotypes_UCSC.py %{buildroot}%{_bindir}
install -m 0755 hisat2_extract_snps_haplotypes_VCF.py %{buildroot}%{_bindir}
install -m 0755 hisat2_extract_splice_sites.py %{buildroot}%{_bindir}
install -m 0755 hisat2_genotype.py %{buildroot}%{_bindir}
install -m 0755 hisat2-inspect %{buildroot}%{_bindir}
install -m 0755 hisat2-inspect-l %{buildroot}%{_bindir}
install -m 0755 hisat2-inspect-s %{buildroot}%{_bindir}
install -m 0755 hisat2_simulate_reads.py %{buildroot}%{_bindir}
install -m 0755 hisat2_test_BRCA_genotyping.py %{buildroot}%{_bindir}
install -m 0755 hisat2_test_HLA_genotyping.py %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE MANUAL NEWS TUTORIAL VERSION
/usr/bin/extract_exons.py
/usr/bin/extract_splice_sites.py
/usr/bin/hisat2
/usr/bin/hisat2-align-l
/usr/bin/hisat2-align-s
/usr/bin/hisat2-build
/usr/bin/hisat2_build_genotype_genome.py
/usr/bin/hisat2-build-l
/usr/bin/hisat2-build-s
/usr/bin/hisat2_extract_exons.py
/usr/bin/hisat2_extract_HLA_vars.py
/usr/bin/hisat2_extract_snps_haplotypes_UCSC.py
/usr/bin/hisat2_extract_snps_haplotypes_VCF.py
/usr/bin/hisat2_extract_splice_sites.py
/usr/bin/hisat2_genotype.py
/usr/bin/hisat2-inspect
/usr/bin/hisat2-inspect-l
/usr/bin/hisat2-inspect-s
/usr/bin/hisat2_simulate_reads.py
/usr/bin/hisat2_test_BRCA_genotyping.py
/usr/bin/hisat2_test_HLA_genotyping.py
/usr/libexec/%{name}/*

%changelog
* Tue Aug 16 2016 Shane Sturrock <shane@biomatters.com> - 2.0.4-1
- Initial release of Hisat2 for BioIT
- Scripts, doc and examples can be found in /usr/libexec/hisat2
