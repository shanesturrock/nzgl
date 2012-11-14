Name:		bsmap
Version:	2.73
Release:	1%{?dist}
Summary:	Bisulfite Sequence Mapping Program
Group:		Applications/Engineering
License:	GNU GPL v3
URL:		http://code.google.com/p/bsmap/
Requires:	samtools
BuildRequires:	zlib-devel
Source0:	bsmap-%{version}.tgz
Patch0:		sam2bam.sh-pathfix.patch
Patch1:		methratio.py-add-shebang.patch
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
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 2.7.3-1
- New upstream release

* Thu Aug 30 2012 Carl Jones <carl@biomatters.com> - 2.7.2-1
- New upstream release

* Thu Jul 25 2012 Carl Jones <carl@biomatters.com> - 2.7-2
- Add patches to fix methratio.py and sam2bam.sh paths/shebang.
- Add samtools dependency 

* Thu Jul 25 2012 Carl Jones <carl@biomatters.com> - 2.7-1
- Initial build.
