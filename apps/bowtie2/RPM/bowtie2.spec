Name:		bowtie2
Version:	2.0.4
Release:	1%{?dist}
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
install -m 0755 bowtie2-align %{buildroot}/%{_bindir}
install -m 0755 bowtie2-build %{buildroot}/%{_bindir}
install -m 0755 bowtie2-inspect %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc MANUAL NEWS VERSION AUTHORS TUTORIAL doc/
%{_bindir}/bowtie2
%{_bindir}/bowtie2-align
%{_bindir}/bowtie2-build
%{_bindir}/bowtie2-inspect
#%{_datadir}/bowtie/genomes
#%{_datadir}/bowtie/indexes
#%{_datadir}/bowtie/reads
#%{_datadir}/bowtie/scripts

%changelog
* Thu Dec 20 2012 Carl Jones <carl@biomatters.com> - 2.0.4-1
- New upstream release

* Mon Dec 17 2012 Carl Jones <carl@biomatters.com> - 2.0.3-1
- New upstream release

* Mon Nov 05 2012 Carl Jones <carl@biomatters.com> - 2.0.2-1
- New upstream release

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 2.0.0.beta7-2
- Small SPEC file tweaks for licence, description  
