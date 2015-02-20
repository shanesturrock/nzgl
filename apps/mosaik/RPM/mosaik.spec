Name:		mosaik
Version:	2.2.3
Release:	2%{?dist}
Summary:	Reference-guided aligner for next-generation sequencing technologies
Group:		Applications/Engineering
License:	GPL
URL:		http://code.google.com/p/mosaik-aligner/
Source0:	http://mosaik-aligner.googlecode.com/files/MOSAIK-%{version}-Linux-x64.tar
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	x86_64

%description
MOSAIK is a reference-guided assembler comprising of four main modular programs:
MosaikBuild
MosaikAligner
MosaikBuild converts various sequence formats into Mosaik’s native read format. 
MosaikAligner pairwise aligns each read to a specified series of reference sequences 
and produces BAMs as outputs.

%prep
%setup -q -n MOSAIK-%{version}-Linux-x64

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 MosaikAligner %{buildroot}%{_bindir}
install -m 0755 MosaikBuild %{buildroot}%{_bindir}
install -m 0755 MosaikJump %{buildroot}%{_bindir}
install -m 0755 MosaikText %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/MosaikAligner
%{_bindir}/MosaikBuild
%{_bindir}/MosaikJump
%{_bindir}/MosaikText

%changelog
* Thu Feb 26 2015 Shane Sturrock <shane@biomatters.com> - 2.2.3-2
- Switched to 64 bit Linux binary distribution due to issues building from
  source on CentOS 7

* Mon Sep 23 2013 Shane Sturrock <shane@biomatters.com> - 2.2.3-1
- Four fold speedup due to improved Smith-Waterman strategy

* Mon Nov 12 2012 Carl Jones <carl@biomatters.com> - 2.1.73-1
- New upstream release.

* Mon Sep 24 2012 Carl Jones <carl@biomatters.com> - 2.1.33-1
- Initial release.
