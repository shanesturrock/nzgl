Name:		EdenaV3
Version:	131028
Release:	1%{?dist}
Summary:	Overlaps-graph nbased assembler
Group:		Applications/Engineering
License:	GPL3
URL:		http://www.genomic.ch/edena/
Source0:	EdenaV3.%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}.%{version}-%{release}-root-%(%{__id_u} -n)

%description 
Edena is an overlaps-graph based de novo assembler dedicated to
process the Illumina GA paired-end (short inserts) and mate-pairs (long
inserts) dataset. 

%prep
%setup -q -n %{name}.%{version}

%build
make compile

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/edena %{buildroot}%{_bindir}/edena

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING referenceManual.pdf
%{_bindir}/edena

%changelog
* Thu May 01 2014 Shane Sturrock <shane@biomatters.com> - 131028-1
- Initial import
