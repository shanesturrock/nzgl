Name:           clustal-omega
Version:        1.2.3
Release:	1%{?dist}
License:        GPL
Group:          Productivity/Scientific/Chemistry
Summary:        The last alignment program you'll ever need
Url:            http://www.clustal.org/omega/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  libargtable2-devel

%description
Clustal Omega is the latest addition to the Clustal family. It offers a 
significant increase in scalability over previous versions, allowing hundreds 
of thousands of sequences to be aligned in only a few hours. It will also 
make use of multiple processors, where present. In addition, the quality of 
alignments is superior to previous versions, as measured by a range of 
popular benchmarks.

%prep
%setup -q

%build
%configure
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/clustalo %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/clustalo

%changelog
* Thu Jul 21 2016 shane@biomatters.com 1.2.3-1
- fixed consensus line in ClustalW format, 'H' in NHQK not recognised as strong
  (bug in Squid)
* Mon Jul 04 2016 shane@biomatters.com 1.2.2-1
- plugged memory leak, parallelised hhalign, more MAC-RAM.
* Mon Mar 03 2014 shane@biomatters.com 1.2.1-1
- corrected Clustal format consensus line and label justification (multi-bit).
* Fri Oct 11 2013 shane@biomatters.com 1.2.0-1
- Initial build for NZGL repository
