%global pkgbase samtools
%global versuffix 100
%define priority 1000
Name:		%{pkgbase}%{versuffix}
Version:	1.0
Release:	1%{?dist}
Summary:	Tools for nucleotide sequence alignments in the SAM format

Group:		Applications/Engineering
License:	MIT
URL:		http://samtools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{pkgbase}/%{pkgbase}-%{version}.tar.bz2
Source1:	%{name}.modulefile
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	zlib-devel >= 1.2.3
BuildRequires:	ncurses-devel
# Post requires alternatives to install tool alternatives.
Requires(post):   %{_sbindir}/alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): %{_sbindir}/alternatives

%description
SAM (Sequence Alignment/Map) is a flexible generic format for storing
nucleotide sequence alignment.
SAM Tools provide various utilities for manipulating alignments in the
SAM format, including sorting, merging, indexing and generating
alignments in a per-position format.

%prep
%setup -q -n %{pkgbase}-%{version}

# fix wrong interpreter
perl -pi -e "s[/software/bin/python][%{__python}]" misc/varfilter.py

# fix eol encoding
sed -i 's/\r//' misc/export2sam.pl


%build
make CFLAGS="%{optflags} -fPIC" %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/%{name}/bin
mkdir -p %{buildroot}%{_libdir}/%{name}/man/man1
install -p samtools %{buildroot}%{_libdir}/%{name}/bin
cp -p samtools.1 %{buildroot}%{_libdir}/%{name}/man/man1/

# install modulefile
install -D -p -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

cd misc/
install -p ace2sam blast2sam.pl bowtie2sam.pl export2sam.pl \
    interpolate_sam.pl maq2sam-long maq2sam-short md5fa md5sum-lite \
    novo2sam.pl plot-bamstats psl2sam.pl sam2vcf.pl samtools.pl \
    seq_cache_populate.pl soap2sam.pl varfilter.py wgsim wgsim_eval.pl \
    zoom2sam.pl \
    %{buildroot}%{_libdir}/%{name}/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog.old LICENSE INSTALL NEWS examples/
%{_libdir}/%{name}
%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%changelog
* Mon Aug 18 2014 Shane Sturrock <shane@biomatters.com> - 1.0-1
- First release of HTSlib-based samtools
- Numerous changes, notably support for CRAM sequencing file format.
- Removes bcftools from package as that is now separate
- Doesn't produce samtools-devel and samtools-lib RPMs anymore

* Mon Apr 22 2013 Shane Sturrock <shane@biomatters.com> - 0.1.19-2
- Bring upstream update from fedora into NZGL replacing homegrown

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 0.1.19-1
- update to 0.1.19

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Adam Huffman <verdurin@fedoraproject.org> - 0.1.18-2
- make sure new seqtk tool included

* Tue Sep  6 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.18-1
- Updated to 0.1.18

* Tue May 10 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.16-1
- Updated to 0.1.16

* Mon Apr 11 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.15-1
- Updated to 0.1.15

* Wed Mar 23 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.14-1
- Updated to 0.1.14
- Build shared library instead of static

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.12a-2
- Fixed header files directory ownership
- Added missing header files

* Mon Dec  6 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.12a-1
- Updated to 0.1.12a

* Tue Nov 23 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-4
- cleanup man page handling

* Sun Oct 10 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-4
- fix attributes for devel subpackage
- fix library location

* Sun Sep 26 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-3
- put headers and library in standard locations

* Mon Sep 6 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-2
- merge Rasmus' latest changes (0.1.8 update)
- include bam.h and libbam.a for Bio-SamTools compilation
- move bam.h and libbam.a to single directory
- put bgzf.h, khash.h and faidx.h in the same place
- add -fPIC to CFLAGS to make Bio-SamTools happy
- add virtual Provide as per guidelines

* Tue Aug 17 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.8-1
- Updated to 0.1.8.

* Mon Nov 30 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.7a-1
- Updated to 0.1.7a.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-3
- Specfile cleanup.

* Sat Jul 11 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-2
- Fixed manpage location.
- Make sure optflags is passed to the makefiles.

* Sat Jul 11 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-1
- Initial build.
