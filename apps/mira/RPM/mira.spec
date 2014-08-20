%define debug_package %{nil}

Name:        mira
Version:     4.0.2
Release:     1
Summary:     MIRA whole genome shotgun and EST sequence assembler
Exclusiveos: linux
Group:       Applications/Engineering
License:     GPLv2
URL:         http://sourceforge.net/projects/mira-assembler/
Source0:     %{name}_%{version}_linux-gnu_x86_64_static.tar.bz2
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:   x86_64

%description
MIRA is a whole genome shotgun and EST sequence assembler for Sanger,
454, Solexa (Illumina), IonTorrent data and PacBio (the later at the
moment only CCS and error-corrected CLR reads). It can be seen as a
Swiss army knife of sequence assembly developed and used in the past
16 years to get assembly jobs done efficiently - and especially
accurately. That is, without actually putting too much manual work
into finishing the assembly.

%prep 
%setup -q -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/bin/mira %{buildroot}/%{_bindir}/mira
/bin/ln -sf mira %{buildroot}/%{_bindir}/mirabait
/bin/ln -sf mira %{buildroot}/%{_bindir}/miraconvert
/bin/ln -sf mira %{buildroot}/%{_bindir}/miramem
# install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/bin/mirabait %{buildroot}/%{_bindir}/mirabait
# install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/bin/miraconvert %{buildroot}/%{_bindir}/miraconvert
# install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/bin/miramem %{buildroot}/%{_bindir}/miramem
install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/scripts/fasta2frag.tcl %{buildroot}%{_bindir}/fasta2frag.tcl
install -m 0755 %{name}_%{version}_linux-gnu_x86_64_static/scripts/fixACE4consed.tcl %{buildroot}%{_bindir}/fixACE4consed.tcl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mira
%{_bindir}/mirabait
%{_bindir}/miraconvert
%{_bindir}/miramem
%{_bindir}/fasta2frag.tcl
%{_bindir}/fixACE4consed.tcl

%changelog
* Thu Aug 21 2014 Shane Sturrock <shane@biomatters.com> - 4.0.2-1
- Initial import of MIRA
