%global pkgbase bwa
%global versuffix 079a
# Alternatives priority needs to be an integer and not start 
# with 0 so replace letters with numbers and add a release number
%define priority 7912
Name:           %{pkgbase}%{versuffix}
Version:        0.7.9a
Release:        2%{?dist}
Summary:        Burrows-Wheeler Alignment tool

Group:          Applications/Engineering
License:        GPLv3
URL:            http://bio-bwa.sourceforge.net/
Source0:        http://downloads.sourceforge.net/bio-%{pkgbase}/%{pkgbase}-%{version}.tar.bz2
Source1:        %{name}.modulefile
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  zlib-devel
# Post requires alternatives to install tool alternatives.
Requires(post):   %{_sbindir}/alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): %{_sbindir}/alternatives

%description

BWA is a program for aligning sequencing reads against a large
reference genome (e.g. human genome). It has two major components, one
for read shorter than 150bp and the other for longer reads.

%prep
%setup -q -n %{pkgbase}-%{version}


%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/%{name}/bin
mkdir -p %{buildroot}%{_libdir}/%{name}/man/man1

install -m 0755 bwa %{buildroot}%{_libdir}/%{name}/bin
install -m 0755 qualfa2fq.pl %{buildroot}%{_libdir}/%{name}/bin
install -m 0755 xa2multi.pl %{buildroot}%{_libdir}/%{name}/bin

install -m 0644 bwa.1 %{buildroot}%{_libdir}/%{name}/man/man1/bwa.1

# install modulefile
install -D -p -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%clean
rm -rf %{buildroot}

%post
alternatives \
   --install %{_bindir}/bwa bwa %{_libdir}/%{name}/bin/bwa %{priority} \
   --slave %{_bindir}/qualfa2fq.pl qualfa2fq.pl %{_libdir}/%{name}/bin/qualfa2fq.pl \
   --slave %{_bindir}/xa2multi.pl xa2multi.pl %{_libdir}/%{name}/bin/xa2multi.pl \
   --slave %{_mandir}/man1/bwa.1 bwa.1 %{_libdir}/%{name}/man/man1/bwa.1

%postun
if [ $1 -eq 0 ]
then
  alternatives --remove bwa %{_libdir}/%{name}/bin/bwa 
fi

%files
%defattr(-,root,root,-)
%doc COPYING 
%{_libdir}/%{name}
%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%changelog
* Tue Jul 29 2014 Shane Sturrock <shane@biomatters.com> - 0.7.9a-2
- Built for module and alternatives support

* Wed May 21 2014 Shane Sturrock <shane@biomatters.com> - 0.7.9a-1
- This release brings several major changes to BWA-MEM. Notably, BWA-MEM now
  formally supports PacBio read-to-reference alignment and experimentally supports
  PacBio read-to-read alignment. BWA-MEM also runs faster at a minor cost of
  accuracy. The speedup is more significant when GRCh38 is in use. More
  specifically:
  - Support PacBio subread-to-reference alignment. Although older BWA-MEM works
    with PacBio data in principle, the resultant alignments are frequently
    fragmented. In this release, we fine tuned existing methods and introduced
    new heuristics to improve PacBio alignment. These changes are not used by
    default. Users need to add option "-x pacbio" to enable the feature.
  - Support PacBio subread-to-subread alignment (EXPERIMENTAL). This feature is
    enabled with option "-x pbread". In this mode, the output only gives the
    overlapping region between a pair of reads without detailed alignment.
  - Output alternative hits in the XA tag if there are not so many of them. This
    is a BWA-backtrack feature.
  - Support mapping to ALT contigs in GRCh38 (EXPERIMENTAL). We provide a script
    to postprocess hits in the XA tag to adjust the mapping quality and generate
    new primary alignments to all overlapping ALT contigs. We would *NOT*
    recommend this feature for production uses.
  - Improved alignments to many short reference sequences. Older BWA-MEM may
    generate an alignment bridging two or more adjacent reference sequences.
    Such alignments are split at a later step as postprocessing. This approach
    is complex and does not always work. This release forbids these alignments
    from the very beginning. BWA-MEM should not produce an alignment bridging
    two or more reference sequences any more.
  - Reduced the maximum seed occurrence from 10000 to 500. Reduced the maximum
    rounds of Smith-Waterman mate rescue from 100 to 50. Added a heuristic to
    lower the mapping quality if a read contains seeds with excessive
    occurrences. These changes make BWA-MEM faster at a minor cost of accuracy
    in highly repetitive regions.
  - Added an option "-Y" to use soft clipping for supplementary alignments.
  - Bugfix: incomplete alignment extension in corner cases.
  - Bugfix: integer overflow when aligning long query sequences.
  - Bugfix: chain score is not computed correctly (almost no practical effect)
  - General code cleanup
  - Added FAQs to README
- Changes in BWA-backtrack:
  - Bugfix: a segmentation fault when an alignment stands out of the end of the
    last chromosome.

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

