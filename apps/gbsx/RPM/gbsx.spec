Name:		gbsx
Version:	1.2
Release:	1%{?dist}
Summary:	GBSX
Group:		Applications/Engineering
License:	GPL3
URL:		https://github.com/GenomicsCoreLeuven/GBSX
Source0:	gbsx-%{version}.tar.gz
Source1:	gbsx
Requires:	java-1.7.0 perl
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Genotyping by Sequencing is an emerging technology for cost effective variant
discovery and genotyping. However, current analysis tools do not fulfill all
experimental design and analysis needs.

GBSX is a package of tools to first aid in experimental design, including
choice of enzymes and barcode design. Secondly, it provides a first analysis
step to demultiplex samples using in-line barcodes, providing fastq files that
can easily be plugged into existing variant analysis pipelines.

%prep
%setup -q -n GBSX-%{version}

%build
find . -type f -name '*.pl' | xargs sed 's=perl\ GBSX_digest_v1.1.pl=GBSX_digest=g' --in-place

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}
install -m 0755 releases/latest/GBSX_digest_v1.1.pl %{buildroot}/%{_bindir}/GBSX_digest
install -m 0644 releases/latest/GBSX_v%{version}.jar %{buildroot}/%{_javadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/gbsx
/usr/bin/GBSX_digest
/usr/share/java/gbsx/GBSX_v%{version}.jar

%changelog
* Wed Jan 27 2016 Shane Sturrock <shane@biomatters.com> - 1.2-1
- Code Clean-up
- Deleted demultiplex parameter -m

* Tue Jan 12 2016 Shane Sturrock <shane@biomatters.com> - 1.1.5-1
- Updated digest script
- Updated Single Read demultiplexing

* Thu Aug 06 2015 Shane Sturrock <shane@biomatters.com> - 1.1-1
- Possible to simulate and demultiplex dual barcode experiments (in paired end
  modus only)
- Updated barcode recognition for paired end modus in the demultiplexer: when a
  read can be assigned to multiple samples, the read is considered as invalid
  (previous was first sample)
