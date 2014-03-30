%define samtools_version 0.1.19

Name:		cufflinks
Version:	2.2.0
Release:	1%{?dist}
Summary:	RNA-Seq transcript assembly, differential expression/regulation
Group:		Applications/Engineering
License:	Boost
URL:		http://cufflinks.cbcb.umd.edu/
Source0:	http://cufflinks.cbcb.umd.edu/downloads/cufflinks-%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/samtools/samtools-%{samtools_version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	boost >= 1.47
BuildRequires:	boost-devel >= 1.47
BuildRequires:	boost-thread >= 1.47
BuildRequires:	boost-jam >= 1.47
BuildRequires:	boost-math >= 1.47
BuildRequires:	boost-random >= 1.47
BuildRequires:	zlib-devel
BuildRequires:	ncurses-devel
BuildRequires:	eigen3-devel

%description

Cufflinks assembles transcripts, estimates their abundances, and tests
for differential expression and regulation in RNA-Seq samples. It
accepts aligned RNA-Seq reads and assembles the alignments into a
parsimonious set of transcripts. Cufflinks then estimates the relative
abundances of these transcripts based on how many reads support each
one.

Cufflinks is a collaborative effort between the Laboratory for
Mathematical and Computational Biology, led by Lior Pachter at UC
Berkeley, Steven Salzberg's group at the University of Maryland Center
for Bioinformatics and Computational Biology, and Barbara Wold's lab
at Caltech.

%prep
%setup -q -a 1

%build
cd samtools-%{samtools_version}
make %{_smp_mflags}
mkdir -p %{_tmppath}/bamlib/include/bam
mkdir -p %{_tmppath}/bamlib/lib
/bin/cp *.h %{_tmppath}/bamlib/include/bam
/bin/cp *.a %{_tmppath}/bamlib/lib
cd ..
LDFLAGS='-lboost_thread-mt -lboost_serialization' ./configure --prefix=/usr --with-bam=%{_tmppath}/bamlib --with-eigen=/usr/include/eigen3
# Fix src/Makefile
sed 's=/usr/include/eigen3/include=/usr/include/eigen3=g' --in-place src/Makefile
# Does not build if smp_mflags used
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/cufflinks %{buildroot}%{_bindir}
install -m 0755 src/cuffcompare %{buildroot}%{_bindir}
install -m 0755 src/cuffquant %{buildroot}%{_bindir}
install -m 0755 src/cuffnorm %{buildroot}%{_bindir}
install -m 0755 src/cuffdiff %{buildroot}%{_bindir}
install -m 0755 src/cuffmerge %{buildroot}%{_bindir}
install -m 0755 src/gtf_to_sam %{buildroot}%{_bindir}
install -m 0755 src/compress_gtf %{buildroot}%{_bindir}
install -m 0755 src/gffread %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README AUTHORS LICENSE
%{_bindir}/*

%changelog
* Wed Mar 26 2014 Shane Sturrock <shane@biomatters.com> 2.2.0-1
- Introduce two new programs - cuffquant and cuffnorm
- Introduce sample sheets and contrast files

* Fri Apr 12 2013 Simon Buxton <simon@biomatters.com> 2.1.1-1
- New upstream release

* Thu Aug 30 2012 Carl Jones <carl@biomatters.com> 2.0.2-3
- Fix issue with binaries being installed incorrectly

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> 2.0.2-2
- Rebuild from source

* Fri Jul 27 2012 Carl Jones <carl@biomatters.com> 2.0.2-1
- Initial build
