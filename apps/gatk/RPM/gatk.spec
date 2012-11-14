%define upstream 1.6-13-g91f02df

Name:		gatk
Version:	1.6.13.g91f02df
Release:	3%{?dist}
Summary:	The Genome Analysis Toolkit (GATK) is a structured software library.
Group:		Applications/Engineering
License:	BSD style
URL:		http://www.broadinstitute.org/gsa/wiki/index.php/Main_Page
Source0:	ftp://ftp.broadinstitute.org/pub/gsa/GenomeAnalysisTK/GenomeAnalysisTK-%{upstream}.tar.bz2
Requires:	java-1.6.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
The GATK is a structured software library that makes writing efficient analysis 
tools using next-generation sequencing data very easy, and second it's a suite 
of tools for working with human medical resequencing projects such as 1000 Genomes 
and The Cancer Genome Atlas. These tools include things like a depth of coverage analyzers, 
a quality score recalibrator, a SNP/indel caller and a local realigner.

%prep
%setup -q -n GenomeAnalysisTK-%{upstream}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_javadir}/%{name}
install -m 0644 AnalyzeCovariates.jar %{buildroot}/%{_javadir}/%{name}
install -m 0644 GenomeAnalysisTK.jar %{buildroot}/%{_javadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc resources/
%{_javadir}/%{name}/GenomeAnalysisTK.jar
%{_javadir}/%{name}/AnalyzeCovariates.jar


%changelog
* Fri Sep 21 2012 Carl Jones <carl@biomatters.com> - %{upstream}-3
- Move JARs to %{_javadir}/%{name}

* Tue Jul 31 2012 Carl Jones <carl@biomatters.com> - %{upstream}-3
- Fix permissions on installed JARs.

* Tue Jul 31 2012 Carl Jones <carl@biomatters.com> - %{upstream}-1
- Initial build.
