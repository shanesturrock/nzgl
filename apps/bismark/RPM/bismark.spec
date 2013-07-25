Name:		bismark
Version:	0.8.2
Release:	1%{?dist}
Summary:	A tool to map bisulfite converted sequence reads and determine cytosine methylation states.
Group:		Applications/Engineering
License:	GNU GPL v3
URL:		http://www.bioinformatics.babraham.ac.uk/projects/bismark/
Source0:	http://www.bioinformatics.babraham.ac.uk/projects/bismark/bismark_v%{version}.tar.gz
Requires:	bowtie
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

Bismark is a program to map bisulfite treated sequencing reads to a genome of interest 
and perform methylation calls in a single step. The output can be easily imported into
a genome viewer, such as SeqMonk, and enables a researcher to analyse the methylation
levels of their samples straight away.

%prep
%setup -q -n %{name}_v%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 bismark %{buildroot}/%{_bindir}
install -m 0755 bismark_genome_preparation %{buildroot}/%{_bindir}
install -m 0755 bismark_methylation_extractor %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Bismark_User_Guide_v%{version}.pdf license.txt RELEASE_NOTES.txt
%{_bindir}/bismark
%{_bindir}/bismark_genome_preparation
%{_bindir}/bismark_methylation_extractor

%changelog
* Fri Jul 26 2013 Shane Sturrock <shane@biomatters.com> - 0.8.2-1
- New upstream release

* Wed Jul 17 2013 Shane Sturrock <shane@biomatters.com> - 0.8.1-1
- New upstream release

* Mon Jul 15 2013 Shane Sturrock <shane@biomatters.com> - 0.8.0-1
- New upstream release

* Mon Mar 18 2013 Shane Sturrock <shane@biomatters.com> - 0.7.9-1
- New upstream release

* Mon Mar 4 2013 Shane Sturrock <shane@biomatters.com> - 0.7.8-1
- New upstream release

* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 0.7.7-1
- New upstream release

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.7.6-1
- New upstream release

* Wed Jul 24 2012 Carl Jones <carl@biomatters.com> - 0.7.5-1
- Initial build.
