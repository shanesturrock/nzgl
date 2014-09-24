%global pkgbase bcftools
%global versuffix 110
Name:		%{pkgbase}%{versuffix}
Version:	1.1
Release:	1%{?dist}
Summary:	Tools for nucleotide sequence alignments in the SAM format

Group:		Applications/Engineering
License:	MIT
URL:		http://samtools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{pkgbase}/%{pkgbase}-%{version}.tar.bz2
Source1:	%{name}.modulefile
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	zlib-devel >= 1.2.3
BuildRequires:	ncurses-devel

%description
BCFtools implements utilities for variant calling (in conjunction with
SAMtools) and manipulating VCF and BCF files.  The program is intended
to replace the Perl-based tools from vcftools.

%prep
%setup -q -n %{pkgbase}-%{version}

%build
make CFLAGS="%{optflags} -fPIC" %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/%{name}/bin
mkdir -p %{buildroot}%{_libdir}/%{name}/man/man1
install -p bcftools plot-vcfstats vcfutils.pl %{buildroot}%{_libdir}/%{name}/bin
cp -p bcftools.1 %{buildroot}%{_libdir}/%{name}/man/man1/

# install modulefile
install -D -p -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE INSTALL
%{_libdir}/%{name}
%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%changelog
* Thu Sep 25 2014 Shane Sturrock <shane@biomatters.com> - 1.1-1
- Use in conjunction with samtools 1.1

* Mon Aug 18 2014 Shane Sturrock <shane@biomatters.com> - 1.0-1
- First release of HTSlib-based bcftools
- Use in conjunction with samtools 1.0
