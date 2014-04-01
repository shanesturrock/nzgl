Name:           bwa
Version:        0.7.8
Release:        1%{?dist}
Summary:        Burrows-Wheeler Alignment tool

Group:          Applications/Engineering
License:        GPLv3
URL:            http://bio-bwa.sourceforge.net/
Source0:        http://downloads.sourceforge.net/bio-%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  zlib-devel

%description

BWA is a program for aligning sequencing reads against a large
reference genome (e.g. human genome). It has two major components, one
for read shorter than 150bp and the other for longer reads.

%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1

install -m 0755 bwa %{buildroot}/%{_bindir}
install -m 0755 qualfa2fq.pl %{buildroot}/%{_bindir}
install -m 0755 xa2multi.pl %{buildroot}/%{_bindir}

install -m 0644 bwa.1 %{buildroot}/%{_mandir}/man1/bwa.1

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING NEWS 
%{_mandir}/man1/%{name}.1*
%{_bindir}/bwa
%{_bindir}/qualfa2fq.pl
%{_bindir}/xa2multi.pl


%changelog
* Wed Apr 02 2014 Shane Sturrock <shane@biomatters.com> - 0.7.8-1
- Changes in BWA-MEM:
 - Bugfix: off-diagonal X-dropoff (option -d) not working as intended.
   Short-read alignment is not affected.
 - Bugfix: unnecessarily large bandwidth used during global alignment,
   which reduces the mapping speed by ~5% for short reads. Results are not
   affected.
 - Bugfix: when the matching score is not one, paired-end mapping quality is
   inaccurate.
 - When the matching score (option -A) is changed, scale all score-related
   options accordingly unless overridden by users.
 - Allow to specify different gap open (or extension) penalties for deletions
   and insertions separately.
 - Allow to specify the insert size distribution.
 - Better and more detailed debugging information.

* Fri Feb 28 2014 Shane Sturrock <shane@biomatters.com> - 0.7.7-1
- This release fixes incorrect MD tags in the BWA-MEM output.
- A note about short-read mapping to GRCh38. The new human reference genome
  GRCh38 contains 60Mbp program generated alpha repeat arrays, some of which 
  are hard masked as they cannot be localized. These highly repetitive arrays 
  make BWA-MEM ~50% slower. If you are concerned with the performance of 
  BWA-MEM, you may consider to use option "-c2000 -m50". On simulated data, 
  this setting helps the performance at a very minor cost on accuracy. May 
  consider to change the default in future releases.

* Mon Jan 03 2014 Shane Sturrock <shane@biomatters.com> - 0.7.6a-1
- Changes in BWA-MEM:
 - Changed the way mapping quality is estimated. The new method tends to give
   the same alignment a higher mapping quality. On paired-end reads, the change
   is minor as with pairing, the mapping quality is usually high. For short
   single-end reads, the difference is considerable.
 - Improved load balance when many threads are spawned. However, bwa-mem is
   still not very thread efficient, probably due to the frequent heap memory
   allocation. Further improvement is a little difficult and may affect the
   code stability.
 - Allow to use different clipping penalties for 5'- and 3'-ends. This helps
   when we do not want to clip one end.
 - Print the @PG line, including the command line options.
 - Improved the band width estimate: a) fixed a bug causing the band
   width estimated from extension not used in the final global alignment; b)
   try doubled band width if the global alignment score is smaller.
   Insufficient band width leads to wrong CIGAR and spurious mismatches/indels.
 - Added a new option -D to fine tune a heuristic on dropping suboptimal hits.
   Reducing -D increases accuracy but decreases the mapping speed. If unsure,
   leave it to the default.
 - Bugfix: for a repetitive single-end read, the reported hit is not randomly
   distributed among equally best hits.
 - Bugfix: missing paired-end hits due to unsorted list of SE hits.
 - Bugfix: incorrect CIGAR caused by a defect in the global alignment.
 - Bugfix: incorrect CIGAR caused by failed SW rescue.
 - Bugfix: alignments largely mapped to the same position are regarded to be
   distinct from each other, which leads to underestimated mapping quality.
 - Added the MD tag.
- There are no changes to BWA-backtrack in this release. However, it has a few
  known issues yet to be fixed. If you prefer BWA-track, It is still advised to
  use bwa-0.6.x.
- While I developed BWA-MEM, I also found a few issues with BWA-SW. It is now
  possible to improve BWA-SW with the lessons learned from BWA-MEM. However, as
  BWA-MEM is usually better, I will not improve BWA-SW until I find applications
  where BWA-SW may excel.

* Tue Jun 04 2013 Simon Buxton <simon@biomatters.com> - 0.7.5a-1
- New upstream release

* Fri Apr 26 2013 Shane Sturrock <shane@biomatters.com> - 0.7.4-1
- New upstream release, drops explicit bwamem-lite binary

* Mon Mar 18 2013 Shane Sturrock <shane@biomatters.com> - 0.7.3a-1
- New upstream release

* Mon Mar 11 2013 Simon Buxton <simon@biomatters.com> - 0.7.2-1
- New upstream release

* Mon Mar 04 2013 Shane Sturrock <shane@biomatters.com> - 0.7.0-1
- New upstream release which removes solid2fastq.pl but adds bwamem-lite and xa2multi.pl

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.6.2-1
- New upstream release

* Thu Feb 17 2011 Adam Huffman <bloch@verdurin.com> - 0.5.9-1
- new upstream release 0.5.9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Adam Huffman <bloch@verdurin.com> - 0.5.8c-1
- upstream bugfix release

* Tue Jul 20 2010 Adam Huffman <bloch@verdurin.com> - 0.5.8a-1
- new upstream release

* Sat May 29 2010 Adam Huffman <bloch@verdurin.com> - 0.5.7-2
- fix source URL
- install manpage
- fix cflags

* Fri May 28 2010 Adam Huffman <bloch@verdurin.com> - 0.5.7-1
- initial version

