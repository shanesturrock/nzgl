Name:		solexaqa
Version:	2.2
Release:	2%{?dist}
Summary:	Calculates quality statistics and creates visual representations of data quality from FASTQ files.
Group:		Applications/Engineering
License:	GPLv3
URL:		http://solexaqa.sourceforge.net/
Source0:	SolexaQA_v.%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	matrix2png

%description
SolexaQA is a Perl-based software package that calculates quality statistics and creates visual representations of 
data quality from FASTQ files generated by Illumina second-generation sequencing technology (“Solexa”).

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
install -m 0755 SolexaQA_v.%{version}/SolexaQA.pl %{buildroot}/%{_bindir}
install -m 0755 SolexaQA_v.%{version}/DynamicTrim.pl %{buildroot}/%{_bindir}
install -m 0755 SolexaQA_v.%{version}/LengthSort.pl %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/SolexaQA.pl
/usr/bin/DynamicTrim.pl
/usr/bin/LengthSort.pl

%changelog
* Thu Jun 27 2013 Shane Sturrock <shane@biomatters.com> - 2.2-2
- Earlier release didn't include DynamicTrim and LengthSort

* Fri Apr 12 2013 Simon Buxton <simon@biomatters.com> - 2.2-1
- New upstream release

* Mon Jan 21 2013 Carl Jones <carl@biomatters.com> - 2.1-1
- New upstream release

* Mon Dec 17 2012 Carl Jones <carl@biomatters.com> - 2.0-1
- New upstream release
* Fri Aug 09 2012 Carl Jones <carl@biomatters.com> - 1.13-2
- Fix source file
* Fri Aug 03 2012 Carl Jones <carl@biomatters.com> - 1.13-1
- Initial build.
