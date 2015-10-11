Name:		vsearch
Version:	1.6.0
Release:	1%{?dist}
Summary:	An alternative to the USEARCH
Group:		Applications/Engineering
License:	GPL3
URL:		https://github.com/torognes/vsearch
Source0: 	vsearch-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	autogen,automake,autoconf

%description
VSEARCH stands for vectorized search, as the tool takes advantage of
parallelism in the form of SIMD vectorization as well as multiple threads to
perform accurate alignments at high speed. VSEARCH uses an optimal global
aligner (full dynamic programming Needleman-Wunsch), in contrast to USEARCH
which by default uses a heuristic seed and extend aligner. This results in more
accurate alignments and overall improved sensitivity (recall) with VSEARCH,
especially for alignments with gaps.

%prep
%setup -q

%build
./autogen.sh
./configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 bin/vsearch %{buildroot}%{_bindir}
install -m 0644 man/vsearch.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/vsearch
%{_mandir}/man1/vsearch.1*

%changelog
* Mon Oct 12 2015 Shane Sturrock <shane@biomatters.com> - 1.6.0
- Added relabelling options for shuffle and added xsize option for several
  commands.

* Thu Oct 08 2015 Shane Sturrock <shane@biomatters.com> - 1.5.0
- Initial NZGL release

