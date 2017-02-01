Name:		SOAPdenovo2
Version:	241
Release:	1%{?dist}
Summary:	SOAPdenovo is a novel short-read assembly method
Group:		Applications/Engineering
License:	GPL
URL:		http://soap.genomics.org.cn/soapdenovo.htm
Source0:	SOAPdenovo2-src-r241.tgz
BuildRoot:	%{_tmppath}/%{name}-2.04-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	zlib-devel kernel-devel

%description
SOAPdenovo is a novel short-read assembly method that can build a de novo 
draft assembly for the human-sized genomes. The program is specially designed 
to assemble Illumina GA short reads. It creates new opportunities for building 
reference sequences and carrying out accurate analyses of unexplored genomes 
in a cost effective way.  

%prep
%setup -q -n %{name}-r%{version}

%build
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 SOAPdenovo-127mer %{buildroot}%{_bindir}/SOAPdenovo-127mer
install -m 0755 SOAPdenovo-63mer %{buildroot}%{_bindir}/SOAPdenovo-63mer
install -m 0755 SOAPdenovo-fusion %{buildroot}%{_bindir}/SOAPdenovo-fusion

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE 
%{_bindir}/SOAPdenovo-127mer
%{_bindir}/SOAPdenovo-63mer
%{_bindir}/SOAPdenovo-fusion

%changelog
* Thu Feb 02 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - r240
- Added a scaffolding preparation module.

* Wed Jul 17 2013 Shane Sturrock <shane@biomatters.com> - 2.04-r240
- New upstream release

* Thu Jun 27 2013 Shane Sturrock <shane@biomatters.com> - 2.04-r239
- Initial build.
