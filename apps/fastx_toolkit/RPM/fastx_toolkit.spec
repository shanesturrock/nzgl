Name:		fastx_toolkit
Version:	0.0.13.2
Release:	3%{?dist}
Summary:	Tools to process short-reads FASTA/FASTQ files

Group:		Applications/Engineering
License:	AGPLv3+
URL:		http://hannonlab.cshl.edu/%{name}/index.html
Source0:	http://hannonlab.cshl.edu/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	libgtextutils
BuildRequires:	libgtextutils-devel
# FASTX-Barcode-Splitter requires the GNU Sed program.
Requires:	sed
Requires:	gnuplot

%description

The FASTX-Toolkit is a collection of command line tools for
Short-Reads FASTA/FASTQ files preprocessing.

Next-Generation sequencing machines usually produce FASTA or FASTQ
files, containing multiple short-reads sequences (possibly with
quality information).

The main processing of such FASTA/FASTQ files is mapping (aka
aligning) the sequences to reference genomes or other databases using
specialized programs. Example of such mapping programs are: Blat,
SHRiMP, LastZ, MAQ and many many others.

However, It is sometimes more productive to preprocess the FASTA/FASTQ
files before mapping the sequences to the genome - manipulating the
sequences to produce better mapping results.

The FASTX-Toolkit tools perform some of these preprocessing tasks. 

%package       galaxy
Summary:       Integrate fastx_toolkit with a local Galaxy installation
Group:	       Applications/Engineering
Requires:      %{name} = %{version}-%{release}


%description   galaxy

These files allow the integration of fastx_toolkit with a local
installation of Galaxy (http://main.g2.bx.psu.edu/), a web-based
platform for analyzing multiple alignments, comparing genomic
annotations, profiling metagenomic samples and much more.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

mkdir %{buildroot}/%{_datadir}/%{name}
cp -a galaxy/ %{buildroot}/%{_datadir}/%{name}

# remove unnecessary m4 files
rm %{buildroot}/%{_datadir}/aclocal/*.m4

# remove autotools Makefile
find %{buildroot}/%{_datadir}/%{name}/galaxy/ -name "Makefile\.*" -delete

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README THANKS
%{_bindir}/fast*

%files	galaxy
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
* Thu Sep 05 2012 Carl Jones <carl@biomatters.com> - 0.0.13.2-3
- Add gnuplot dependency
* Fri Jul 27 2012 Carl Jones <carl@biomatters.com> - 0.0.13.2-2
- Add libgtextutils dependency

* Fri Jul 27 2012 Carl Jones <carl@biomatters.com> - 0.0.13.2-1
- Upgrade to 0.0.13.2 release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.13-6
- Rebuilt for c++ ABI breakage

* Mon Jan  9 2012 Adam Huffman <verdurin@fedoraproject.org> - 0.0.13-5
- fix compilation with GCC 4.7

* Fri May 27 2011 Adam Huffman <bloch@verdurin.com> - 0.0.13-4
- fix ownership of /usr/share/fastx_toolkit

* Tue Nov 16 2010 Adam Huffman <bloch@verdurin.com> - 0.0.13-3
- fix license and remove autotools Makefiles

* Wed Aug 25 2010 Adam Huffman <bloch@verdurin.com> - 0.0.13-2
- fix CFLAGS and CXXFLAGS

* Tue May 11 2010 Adam Huffman <bloch@verdurin.com> - 0.0.13-1
- initial version

