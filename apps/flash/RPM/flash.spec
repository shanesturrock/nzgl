Name:		FLASH
Version:	1.2.10
Release:	1%{?dist}
Summary:	Fast Length Adjustment of SHort reads
Group:		Applications/Engineering
License:	GPL
URL:		http://ccb.jhu.edu/software/FLASH/
Source0:	FLASH-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	zlib-devel

%description
FLASH (Fast Length Adjustment of SHort reads) is a very accurate and fast tool
to merge paired-end reads that were generated from DNA fragments whose lengths
are shorter than twice the length of reads.  Merged read pairs result in
unpaired longer reads.  Longer reads are generally more desired in genome
assembly and genome analysis processes.

FLASH cannot merge paired-end reads that do not overlap.  It also cannot merge
jumping read pairs that have an outward orientation (but these reads tend not to
overlap anyway).  FLASH also is not designed for data that has a significant
portion of indel errors (such as Sanger sequencing data).

%prep
%setup -q

%build
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 flash %{buildroot}%{_bindir}/flash

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/flash

%changelog
* Tue Apr 22 2014 Shane Sturrock <shane@biomatters.com> - 1.2.10-1
- FLASH now supports combining read pairs in outie orientation.  See help for
  the new --allow-outies option.
- Added warning messages in a few cases where it may be helpful to specify
  different parameters.
* Wed Feb 26 2014 Shane Sturrock <shane@biomatters.com> - 1.2.9-1
- The core algorithm of FLASH has been optimized using SSE and SSE2
  instructions.  On x86_64 CPUs it now can run over twice as fast.
- The help output of FLASH has been improved.
- Added supported for tab-delimited input and output.
- FLASH now displays more informative error messages in some cases.
- Reorganized some of the code so that it's easier to modify.
- Reading the data from standard input now works correctly.
- With --to-stdout specified, informational messages are now written to standard
  error rather than omitted.
* Mon Dec 16 2013 Shane Sturrock <shane@biomatters.com> - 1.2.8-1
- Upstream update
* Tue Aug 06 2013 Shane Sturrock <shane@biomatters.com> - 1.2.7-1
- Upstream update
* Thu Jun 27 2013 Shane Sturrock <shane@biomatters.com> - 1.2.6-1
- Initial build.
