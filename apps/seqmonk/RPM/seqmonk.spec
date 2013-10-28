Name:		seqmonk
Version:	0.26.0
Release:	1%{?dist}
Summary:	A tool to visualise and analyse high throughput mapped sequence data
Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.bioinformatics.babraham.ac.uk/projects/seqmonk/
Source0:	http://www.bioinformatics.babraham.ac.uk/projects/seqmonk/seqmonk_v%{version}.zip
Source1:	seqmonk-icons.tar.gz
Source2:	seqmonk.desktop
Patch0:		seqmonk-classpath.patch
Requires:	java-1.6.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
SeqMonk is a program to enable the visualisation and analysis of mapped sequence data. It was written 
for use with mapped next generation sequence data but can in theory be used for any dataset which can 
be expressed as a series of genomic positions.

%prep
%setup -q -n SeqMonk
%patch0 -p0

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 seqmonk %{buildroot}/%{_bindir}
/bin/cp -r uk/ %{buildroot}/%{_javadir}/%{name}/
/bin/cp -r com/ %{buildroot}/%{_javadir}/%{name}/

# Icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/
tar xf %{SOURCE1} -C %{buildroot}%{_datadir}/icons/hicolor/

# .desktop
mkdir -p %{buildroot}%{_datadir}/applications/
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet /usr/share/icons/hicolor
fi

%files
%defattr(-,root,root,-)
%doc README.txt LICENSE.txt RELEASE_NOTES.txt
/usr/bin/seqmonk
/usr/share/java/seqmonk/*
/usr/share/applications/seqmonk.desktop
/usr/share/icons/hicolor/*

%changelog
* Tue Oct 29 2013 Shane Sturrock <shane@biomatters.com> - 0.26.0-1
- SeqMonk v0.26.0 adds a critical fix for the new OSX Mavericks release
  and also adds some new functionality to make it easier to deal with 
  incomplete genome assemblies or other custom genomes.
- Fixed the launcher on OSX to adapt to changes in OSX Mavericks
  which broke the auto configuration code.
- Fixed a bug which caused the program to hang after downloading
  a new genome in response to opening an existing seqmonk project.
- Added a new graphical tool to aid in the creation of custom genomes
  meaning that you can now create custom genomes including pseudo
  chromosomes from either a collection of fasta files or a GTF file.
* Tue Sep 10 2013 Shane Sturrock <shane@biomatters.com> - 0.25.0-1
- Added a quantitation trend plot to allow the examination of complex pattersn around features
- Added a muti-lane chi-square test for allele specific analysis and other applications
- Improved the options in the feature probe generator
- Allow multiple data stores in the aligned probes plot and allow custom sorting
- Allow filtering of reads against features when re-importing
- Added nice colour options to the hierarchical cluster plot
- Added a domainogram plot to look at quantitations at different levels
- Added an option to find sets of features using a list of search terms
- Added the ability to add comments to probe lists so you can remember why you did what you did
- Added a probe list description report to completely record the results of an analysis
- Added a subset normalisation quantitation method
- Reorganised the relative quantitation method to allow for specific pairings of references and samples
- Lots of other bug fixes and improvements
* Mon Feb 25 2013 Carl Jones <carl@biomatters.com> - 0.24.1-0
- New upstream release

* Thu Jan 24 2013 Carl Jones <carl@biomatters.com> - 0.24-0
- New upstream release

* Thu Jan 24 2013 Carl Jones <carl@biomatters.com> - 0.23.1-2
- Add desktop icons, menu

* Wed Dec 12 2012 Carl Jones <carl@biomatters.com> - 0.23.1-1
- New upstream release
* Wed Dec 05 2012 Carl Jones <carl@biomatters.com> - 0.23.0-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 0.22.0-2
- Use 0.22 tarball rather than 0.21
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 0.22.0-1
- New upstream release
* Fri Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.21.0-3
- Fixed Java paths
* Fri Aug 02 2012 Carl Jones <carl@biomatters.com> - 0.21.0-2
- Move bin/seqmonk to seqmonk.
* Fri Aug 02 2012 Carl Jones <carl@biomatters.com> - 0.21.0-1
- Initial build.
