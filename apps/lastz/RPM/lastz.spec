Name:		lastz
Version:	1.02.00
Release:	2%{?dist}
Summary:	LASTZ is a program for aligning DNA sequences, a pairwise aligner
Group:		Applications/Engineering
License:	Public Domain
URL:		http://www.bx.psu.edu/~rsharris/lastz/
Source0:	http://www.bx.psu.edu/miller_lab/dist/lastz-1.02.00.tar.gz
Patch0:		Makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
LASTZ is a program for aligning DNA sequences, a pairwise aligner. Originally 
designed to handle sequences the size of human chromosomes and from different 
species, it is also useful for sequences produced by NGS sequencing technologies 
such as Roche 454.

%prep
%setup -q -n %{name}-distrib-%{version}
%patch0 -p0

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/lastz %{buildroot}%{_bindir}
install -m 0755 src/lastz_D %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.lastz.html lav_format.html hsx_format.html images/
%{_bindir}/lastz
%{_bindir}/lastz_D

%changelog
* Thu Feb 26 2014 Shane Sturrock <shane@biomatters.com> - 1.02.00-2
- Patch to build on CentOS 7

* Mon Sep 24 2012 Carl Jones <carl@biomatters.com> - 1.02.00-1
- Initial release.
