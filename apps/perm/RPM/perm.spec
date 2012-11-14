Name:		perm
Version:	0.4.0
Release:	1%{?dist}
Summary:	Efficient mapping of short sequences accomplished with periodic full sensitive spaced seeds
Group:		Applications/Engineering
License:	Apache License 2.0
URL:		http://code.google.com/p/perm/
Source0:	http://perm.googlecode.com/files/PerM4Source.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	glibc-static

%description
PerM is a software package which was designed to perform highly efficient genome scale 
alignments for hundreds of millions of short reads produced by the ABI SOLiD and Illumina 
sequencing platforms. Today PerM is capable of providing full sensitivity for alignments 
within 4 mismatches for 50bp SOLID reads and 9 mismatches for 100bp Illumina reads.

%prep
%setup -q -n Source

%build
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 perm %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/perm

%changelog
* Mon Sep 24 2012 Carl Jones <carl@biomatters.com> - 0.4.0-1
- Initial release.
