Name:		bismark
Version:	0.7.11
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
install -m 0755 bedGraph2cytosine %{buildroot}/%{_bindir}
install -m 0755 bismark2bedGraph %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Bismark_User_Guide.pdf license.txt RELEASE_NOTES.txt RRBS_Guide.pdf
%{_bindir}/bismark
%{_bindir}/bismark2bedGraph
%{_bindir}/bedGraph2cytosine
%{_bindir}/bismark_genome_preparation
%{_bindir}/bismark_methylation_extractor

%changelog
* Mon Apr 23 2013 Shane Sturrock <shane@biomatters.com> - 0.7.11-1
- New upstream release including some new bed tools

* Mon Apr 22 2013 Shane Sturrock <shane@biomatters.com> - 0.7.10-1
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
