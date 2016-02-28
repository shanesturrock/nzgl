Name:		bsmap
Version:	2.90
Release:	1%{?dist}
Summary:	Bisulfite Sequence Mapping Program
Group:		Applications/Engineering
License:	GNU GPL v3
URL:		http://code.google.com/p/bsmap/
Requires:	samtools
BuildRequires:	zlib-devel
Source0:	bsmap-%{version}.tgz
Patch0:		sam2bam.sh-pathfix.patch
Patch1:		param.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
BSMAP is a short reads mapping software for bisulfite sequencing reads.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 bsmap %{buildroot}/%{_bindir}
install -m 0755 sam2bam.sh %{buildroot}/%{_bindir}
install -m 0755 methratio.py %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc RELEASE.txt README.txt GPL_3.0.txt
%{_bindir}/bsmap
%{_bindir}/sam2bam.sh
%{_bindir}/methratio.py

%changelog
* Mon Feb 29 2015 Shane Sturrock <shane@biomatters.com> - 2.9.0-1
- Added "#include <unistd.h>" to param.h.
- fixed methratio.py memory issue that fail to fork samtools process when
  using more than 50% system memory (by Greg Zynda)
- fixed a bug in RRBS mode indexing
- improved the randomness selecting a random hit from multiple hits using "-r
  1" option
- increased the max number of chromosomes/contigs from 2^13 to 2^17  
- added methdiff.py script for differential methylation analysis
- bsmap upgrade:
  - added -3 for 3 nucleotide mapping mode
  - restored -r 2 to report all multiple hits
  - added -V [0,1,2] to set verbose level
  - modified -D  can be set multiple times to support RRBS with multiple
    restriction enzyme digestion 
  - improved alignment speed/sensitivity for N-containing reads and gap
    alignment
  - increased max read length to 160 nt
  - generating bam by direct pipe instead of conversion after alignment in
    previous versions
- methratio.py upgrade
  - added stdin/stdout input/output for methratio.py to pipe with bsmap and
    other tools.
  - added -w and -b option to generate a wiggle file for methylation ratio
    visualization
  - added -x [CG|CHG|CHH] option to select reporting specified methyC pattern
  - the sequence context changed to CG|CHG|CHH instead of previous 5nt
    neighborhood sequences 

* Thu Feb 19 2015 Shane Sturrock <shane@biomatters.com> - 2.7.4-2
- Patch to build on CentOS 7

* Tue Jan 29 2013 Carl Jones <carl@biomatters.com> - 2.7.4-1
- New upstream release

* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 2.7.3-1
- New upstream release

* Thu Aug 30 2012 Carl Jones <carl@biomatters.com> - 2.7.2-1
- New upstream release

* Thu Jul 26 2012 Carl Jones <carl@biomatters.com> - 2.7-2
- Add patches to fix methratio.py and sam2bam.sh paths/shebang.
- Add samtools dependency 

* Thu Jul 26 2012 Carl Jones <carl@biomatters.com> - 2.7-1
- Initial build.
