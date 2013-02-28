Name:		trinityrnaseq
Version:	20130225
Release:	1%{?dist}
Summary:	Provides software targeted to the reconstruction of full-length transcripts and alternatively spliced isoforms from Illumina RNA-Seq data.
Group:		Applications/Engineering
License:	BSD Modified
URL:		http://trinityrnaseq.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}_r2013-02-25.tgz
Patch0:		%{name}-rootdir.patch
Requires:	java-1.6.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
Requires:	bowtie
AutoReqProv:	no

%description
Trinity, developed at the Broad Institute and the Hebrew University of Jerusalem, represents a 
novel method for the efficient and robust de novo reconstruction of transcriptomes from RNA-seq 
data. Trinity combines three independent software modules: Inchworm, Chrysalis, and Butterfly, 
applied sequentially to process large volumes of RNA-seq reads.

%prep
%setup -q -n %{name}_r2013-02-25
%patch0 -p0
# Fix perl shebangs
find . -type f -name '*.pl' | xargs sed 's=/usr/local/bin/perl=/usr/bin/perl=g' --in-place

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{perl_vendorarch}
mkdir -p %{buildroot}/%{_bindir}
#mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/Butterfly
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/Chrysalis

install -m 0755 Trinity.pl %{buildroot}/%{_bindir}

#install -m 0644 Butterfly/Butterfly.jar %{buildroot}/%{_javadir}/%{name}
install -m 0644 Butterfly/Butterfly.jar %{buildroot}/%{_libexecdir}/%{name}/Butterfly

install -m 0755 Inchworm/bin/cigar_tweaker %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin/cigar_tweaker
install -m 0755 Inchworm/bin/FastaToDeBruijn %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin/FastaToDeBruijn
install -m 0755 Inchworm/bin/inchworm %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin/inchworm
install -m 0755 Inchworm/bin/ParaFly %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin/ParaFly
install -m 0755 Inchworm/bin/pull_reads_with_kmers %{buildroot}/%{_libexecdir}/%{name}/Inchworm/bin/pull_reads_with_kmers

install -m 0755 Chrysalis/checkLock %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/checkLock
install -m 0755 Chrysalis/MakeDepend %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/MakeDepend
install -m 0755 Chrysalis/JoinTransByPairs %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/JoinTransByPairs
install -m 0755 Chrysalis/TranscriptomeFromVaryK %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/TranscriptomeFromVaryK
install -m 0755 Chrysalis/IsoformAugment %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/IsoformAugment
install -m 0755 Chrysalis/RunButterfly %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/RunButterfly
install -m 0755 Chrysalis/Chrysalis %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/Chrysalis
install -m 0755 Chrysalis/QuantifyGraph %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/QuantifyGraph
install -m 0755 Chrysalis/BreakTransByPairs %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/BreakTransByPairs
install -m 0755 Chrysalis/GraphFromFasta %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/GraphFromFasta
install -m 0755 Chrysalis/ReadsToTranscripts %{buildroot}/%{_libexecdir}/%{name}/Chrysalis/ReadsToTranscripts

/bin/cp -r PerlLib/* %{buildroot}/%{perl_vendorarch}
/bin/cp -r PerlLibAdaptors/* %{buildroot}/%{perl_vendorarch}

/bin/cp -r util %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r trinity-plugins %{buildroot}/%{_libexecdir}/%{name}/
/bin/cp -r Analysis %{buildroot}/%{_libexecdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/ LICENSE README Release.Notes
/usr/bin/Trinity.pl
#/usr/share/java/%{name}/Butterfly.jar
/usr/libexec/%{name}/*
%{perl_vendorarch}/*

%changelog
* Mon Feb 18 2013 Shane Sturrock <shane@biomatters.com> - 20130225-1
- New upstream release
* Mon Feb 18 2013 Shane Sturrock <shane@biomatters.com> - 20130216-1
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 20121005-1
- New upstream release
* Tue Sep 04 2012 Carl Jones <carl@biomatters.com> - 20120608-6
- Include Analysis/
* Tue Sep 04 2012 Carl Jones <carl@biomatters.com> - 20120608-5
- Move Butterfly.jar into libexec
* Tue Sep 04 2012 Carl Jones <carl@biomatters.com> - 20120608-4
- Fix ROOTDIR in Trinity.pl
- Include utils/ and trinity-plugins

* Fri Aug 10 2012 Carl Jones <carl@biomatters.com> - 20120608-3
- Move binaries to libexec
- Patch Trinity.pl so it finds the correct binaries

* Fri Aug 10 2012 Carl Jones <carl@biomatters.com> - 20120608-2
- Fix paths

* Mon Aug 06 2012 Carl Jones <carl@biomatters.com> - 20120608-1
- Initial build.
