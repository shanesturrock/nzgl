%global pkgbase bwa
%global versuffix 062
# Alternatives priority needs to be an integer and not start 
# with 0 so replace letters with numbers and add a release number
%define priority 6203
Name:           %{pkgbase}%{versuffix}
Version:        0.6.2
Release:        3%{?dist}
Summary:        Burrows-Wheeler Alignment tool

Group:          Applications/Engineering
License:        GPLv3
URL:            http://bio-bwa.sourceforge.net/
Source0:        http://downloads.sourceforge.net/bio-%{pkgbase}/%{pkgbase}-%{version}.tar.bz2
Source1:        %{name}.modulefile
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  zlib-devel
# Post requires alternatives to install tool alternatives.
Requires(post):   %{_sbindir}/alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): %{_sbindir}/alternatives

%description

BWA is a program for aligning sequencing reads against a large
reference genome (e.g. human genome). It has two major components, one
for read shorter than 150bp and the other for longer reads.

%prep
%setup -q -n %{pkgbase}-%{version}


%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/%{name}/bin
mkdir -p %{buildroot}%{_libdir}/%{name}/man/man1

install -m 0755 bwa %{buildroot}%{_libdir}/%{name}/bin
install -m 0755 solid2fastq.pl %{buildroot}%{_libdir}/%{name}/bin
install -m 0755 qualfa2fq.pl %{buildroot}%{_libdir}/%{name}/bin
install -m 0755 xa2multi.pl %{buildroot}%{_libdir}/%{name}/bin

install -m 0644 bwa.1 %{buildroot}%{_libdir}/%{name}/man/man1/bwa.1

# install modulefile
install -D -p -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%clean
rm -rf %{buildroot}

%post
alternatives \
   --install %{_bindir}/bwa bwa %{_libdir}/%{name}/bin/bwa %{priority} \
   --slave %{_bindir}/solid2fastq.pl solid2fastq.pl %{_libdir}/%{name}/bin/solid2fastq.pl \
   --slave %{_bindir}/qualfa2fq.pl qualfa2fq.pl %{_libdir}/%{name}/bin/qualfa2fq.pl \
   --slave %{_bindir}/xa2multi.pl xa2multi.pl %{_libdir}/%{name}/bin/xa2multi.pl \
   --slave %{_mandir}/man1/bwa.1 bwa.1 %{_libdir}/%{name}/man/man1/bwa.1

%postun
if [ $1 -eq 0 ]
then
  alternatives --remove bwa %{_libdir}/%{name}/bin/bwa 
fi

%files
%defattr(-,root,root,-)
%doc COPYING 
%{_libdir}/%{name}
%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%changelog
* Wed Jul 30 2014 Shane Sturrock <shane@biomatters.com> - 0.6.2-3
- Built for module and alternatives support
