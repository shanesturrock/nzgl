# Requires velvet sources to build against
%define velvet_version 1.2.07
%define velvet_dir velvet_%{velvet_version}

Summary:	De novo transcriptome assembler for very short reads
Name:		oases
Version:	0.2.08
Release:	1%{?dist}
License:	GPLv3
Group:		Applications/Engineering
URL:		http://www.ebi.ac.uk/~zerbino/oases/
Source:		http://www.ebi.ac.uk/~zerbino/oases/%{name}_%{version}.tgz
Source1:	http://www.ebi.ac.uk/~zerbino/velvet/velvet_%{velvet_version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	zlib-devel
AutoReqProv:	no

%description

Oases is a de novo transcriptome assembler designed to produce transcripts from 
short read sequencing technologies, such as Illumina, SOLiD, or 454 in the absence 
of any genomic assembly. It was developed by Marcel Schulz (MPI for Molecular Genomics) 
and Daniel Zerbino (previously at the European Bioinformatics Institute (EMBL-EBI), 
now at UC Santa Cruz).

Oases uploads a preliminary assembly produced by Velvet, and clusters the contigs 
into small groups, called loci. It then exploits the paired-end read and long read 
information, when available, to construct transcript isoforms.

This package builds the sequencespace and colorspace versions of Oases.

%prep
%setup -q -n %{name}_%{version} -a 1

%build
make VELVET_DIR=%{velvet_dir}
make color VELVET_DIR=%{velvet_dir}

%install
%{__rm} -rf %{buildroot}
%{__install} -m 0755 -d %{buildroot}%{_bindir}
%{__install} -m 0755 oases %{buildroot}%{_bindir}
%{__install} -m 0755 oases_de %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE.txt README.txt *.pdf
%{_bindir}/*

%changelog
* Wed Aug 01 2012 Carl Jones <carl@biomatters.com> - 0.2.08-1
- Initial package.
