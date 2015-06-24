%global pkgbase bowtie
%global versuffix 112
# Alternatives priority needs to be an integer
%define priority 112
Name:		%{pkgbase}%{versuffix}
Version:	1.1.2
Release:	1%{?dist}
Summary:	An ultrafast, memory-efficient short read aligner

Group:		Applications/Engineering
License:	Artistic 2.0
URL:		http://bowtie-bio.sourceforge.net/index.shtml
Source0:	http://downloads.sourceforge.net/%{pkgbase}-bio/%{pkgbase}-%{version}-src.zip
Source1:        %{name}.modulefile
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# Post requires alternatives to install tool alternatives.
Requires(post):   %{_sbindir}/alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): %{_sbindir}/alternatives

%description

Bowtie, an ultrafast, memory-efficient short read aligner for short
DNA sequences (reads) from next-gen sequencers. Please cite: Langmead
B, et al. Ultrafast and memory-efficient alignment of short DNA
sequences to the human genome. Genome Biol 10:R25.

%prep
%setup -q -n %{pkgbase}-%{version}

%build
make %{?_smp_mflags} -p EXTRA_FLAGS="%{optflags}"


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_libdir}/%{name}/bin
mkdir -p %{buildroot}/%{_datadir}/%{name}/bowtie


install -m 0755 bowtie %{buildroot}/%{_libdir}/%{name}/bin
install -m 0755 bowtie-build %{buildroot}/%{_libdir}/%{name}/bin
install -m 0755 bowtie-build-l %{buildroot}/%{_libdir}/%{name}/bin
install -m 0755 bowtie-align-l %{buildroot}/%{_libdir}/%{name}/bin
install -m 0755 bowtie-build-s %{buildroot}/%{_libdir}/%{name}/bin
install -m 0755 bowtie-align-s %{buildroot}/%{_libdir}/%{name}/bin
install -m 0755 bowtie-inspect %{buildroot}/%{_libdir}/%{name}/bin
install -m 0755 bowtie-inspect-l %{buildroot}/%{_libdir}/%{name}/bin
install -m 0755 bowtie-inspect-s %{buildroot}/%{_libdir}/%{name}/bin

cp -a reads %{buildroot}/%{_datadir}/%{name}/bowtie/
cp -a indexes %{buildroot}/%{_datadir}/%{name}/bowtie/
cp -a genomes %{buildroot}/%{_datadir}/%{name}/bowtie/
cp -a scripts %{buildroot}/%{_datadir}/%{name}/bowtie/

# install modulefile
install -D -p -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%clean
rm -rf %{buildroot}

%post
alternatives \
   --install %{_bindir}/bowtie bowtie %{_libdir}/%{name}/bin/bowtie %{priority} \
   --slave %{_bindir}/bowtie-build bowtie-build %{_libdir}/%{name}/bin/bowtie-build \
   --slave %{_bindir}/bowtie-build-l bowtie-build-l %{_libdir}/%{name}/bin/bowtie-build-l \
   --slave %{_bindir}/bowtie-build-s bowtie-build-s %{_libdir}/%{name}/bin/bowtie-build-s \
   --slave %{_bindir}/bowtie-align-l bowtie-align-l %{_libdir}/%{name}/bin/bowtie-align-l \
   --slave %{_bindir}/bowtie-align-s bowtie-align-s %{_libdir}/%{name}/bin/bowtie-align-s \
   --slave %{_bindir}/bowtie-inspect-l bowtie-inspect-l %{_libdir}/%{name}/bin/bowtie-inspect-l \
   --slave %{_bindir}/bowtie-inspect-s bowtie-inspect-s %{_libdir}/%{name}/bin/bowtie-inspect-s \
   --slave %{_bindir}/bowtie-inspect bowtie-inspect %{_libdir}/%{name}/bin/bowtie-inspect

%postun
if [ $1 -eq 0 ]
then
  alternatives --remove bowtie %{_libdir}/%{name}/bin/bowtie 
fi

%files
%defattr(-,root,root,-)
%doc LICENSE MANUAL NEWS VERSION AUTHORS TUTORIAL doc/
%dir %{_datadir}/%{name}/bowtie
%{_libdir}/%{name}
%{_datadir}/%{name}/bowtie
%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%changelog
* Thu Jun 25 2015 Shane Sturrock <shane@biomatters.com> - 1.1.2-1
- Fixed the building process for OSX Yosemite.
- Added the install target for linux to better aid package building process 
  and the overall installation process.
- Added the Intel TBB option which provides in most situations a better performance
  output. TBB is not present by default in the current build but can be added
  by compiling the source code with WITH_TBB=1 option.
- Fixed a minor issue related with managing the number of threads spawned.
- Fixed a minor issue which may have caused a memory leak after an exception
  was thrown.
- Fixed a bug that caused bowtie to crash if a read was trimmed more than the
  read's lenght on 5 prime end.
- Added some minor corrections/addition to the manual.
- Fixed a bug that caused the wrapper to incorrectly identify the bowtie binary.

* Thu Oct 02 2014 Shane Sturrock <shane@biomatters.com> - 1.1.1-1
- Fixed a compiling linkage problem related with Mavericks OSX.
- Improved performance for cases where the reference contains ambiguous or 
  masked nucleobases represented by Ns.
- Some minor automatic tests updates.

* Mon Aug 04 2014 Shane Sturrock <shane@biomatters.com> - 1.1.0-1
- Added support for large and small indexes, removing 4-billion-nucleotide
  barrier.  Bowtie can now be used with reference genomes of any size.
- No longer releasing 32-bit binaries.  Simplified manual and Makefile
  accordingly.
- Phased out CygWin support.
- Improved efficiency of index files loading.
- Fixed a bug that made the inspector fail in some situations.

* Mon Mar 24 2014 Shane Sturrock <shane@biomatters.com> - 1.0.1-1
- improved index querying efficiency using "population count" instructions 
  available since SSE4.2.

* Mon Apr 15 2013 Shane Sturrock <shane@biomatters.com> - 1.0.0-1
- New upstream release

* Tue Dec 18 2012 Carl Jones <carl@biomatters.com> - 0.12.9-1
- New upstream release

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.12.8-1
- New upstream release

* Mon Jun 27 2011 Adam Huffman <bloch@verdurin.com> - 0.12.7-2
- add missing doc/ 
- add patch to fix Perl script without shebang

* Mon Sep 13 2010 Adam Huffman <bloch@verdurin.com> - 0.12.7-1
- new upstream release 0.12.7
- changelog at http://bowtie-bio.sourceforge.net/index.shtml

* Tue Aug 31 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-3
- really fix compilation flags

* Wed Aug 25 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-2
- fix compilation flags

* Mon Aug  2 2010 Adam Huffman <bloch@verdurin.com> - 0.12.5-1
- initial version

