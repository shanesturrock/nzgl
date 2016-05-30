Name:		tablet
Version:	1.15.09.01
Release:	2%{?dist}
Summary:	Lightweight, high-performance graphical viewer for next generation sequence assemblies and alignments.
Group:		Applications/Engineering
License:	BSD Modified
URL:		http://bioinf.scri.ac.uk/tablet/index.shtml
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.gz
Source2:	%{name}.desktop
Patch0:		%{name}-apphomefix.patch
#Patch1:		maqtoace-apphomefix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	java-1.8.0-openjdk

%description
Tablet is a lightweight, high-performance graphical viewer for next generation sequence assemblies and alignments.

%prep
%setup -q  -n Tablet
%patch0 -p0
#%patch1 -p0

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_javadir}/%{name}

install -m 0755 %{name} %{buildroot}/%{_bindir}
#install -m 0755 maqtoace %{buildroot}/%{_bindir}
/bin/cp -r lib/ %{buildroot}/%{_javadir}/%{name}
/bin/cp -r .install4j/ %{buildroot}/%{_javadir}/%{name}

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
%doc docs/*
/usr/bin/tablet
#/usr/bin/maqtoace
/usr/share/java/tablet/*
/usr/share/java/tablet/.install4j/*
/usr/share/applications/tablet.desktop
/usr/share/icons/hicolor/*

%changelog
* Fri May 27 2017 Shane Sturrock <shane@biomatters.com> - 1.15.09.01-2
- Fixed Java issue where tablet wouldn't start because the path was wrong.

* Wed Sep 02 2015 Shane Sturrock <shane@biomatters.com> - 1.15.09.01-1
- BUG: Reverted the included version of Java (because of JDK-8134827 that was
  breaking the scrollbars on large data sets).
- NEW: The read-shadower now highlights all read pairs in addition to reads
  under the mouse.
- NEW: Added SHIFT+mouse wheel support, that scrolls the canvas horizontally.
- NEW: Updated the installers for better Windows 10 and OS X compatibility.
- NEW: Updated the Java runtime included in the installers to the latest
  versions.
- CHG: Removed the write-file test when running installers as it’s not
  compatible with UAC situations.

* Wed Oct 22 2014 Shane Sturrock <shane@biomatters.com> - 1.14.10.21-1
- NEW: Fixed an installer bug that prevented Tablet from installing on Linux.
- NEW: Added a new colour scheme that handles read number concordance.
- NEW: Added experimental support for annotation in the GTF format.
- NEW: Packing (paired-pack) of data on large coverage is now significantly 
  faster.
- NEW: More information is provided during the various stages of loading a 
  contig’s data.
- NEW: Updated Picard to the latest version.
- BUG: Tablet no longer reloads a contig if simply changing the packing mode.
- BUG: CIGAR X was not being dealt with correctly in cases where read sequence 
  was provided.
- BUG: Parsing of BAI files was failing when relative input paths were used.
- BUG: History snapshot now respects packing mode changes.
- BUG: The application’s title bar didn’t reset its text after an open 
  assembly was closed.
- BUG: The assembly summary dialog was (sometimes) working with incorrect data.

* Fri Apr 11 2014 Shane Sturrock <shane@biomatters.com> - 1.14.04.10-1
- NEW: Added experimental support for annotation / features in the BED file 
  format.
= NEW: Added experimental support for annotation / features in the VCF file 
  format.
- CHG: Updated the Web Start files to conform to the new security requirements 
  of the latest version of Web Start.

* Wed Dec 18 2013 Shane Sturrock <shane@biomatters.com> - 1.13.12.17-1
- BUG: Fixed a critical issue that prevented Tablet from parsing SAM files 
  correctly.

* Mon Dec 16 2013 Shane Sturrock <shane@biomatters.com> - 1.13.12.13-1
- NEW: Added a new Assembly Summary dialog which can be launched from the 
  "More" link above the Contigs listing.
- NEW: Threaded off drag and drop file loading so that Windows Explorer no 
  longer appears to hang after performing the drop.
- BUG: Tablet's embedded samtools no longer worked with 64 bit Centos 6.
- BUG: JNLP launched Tablet (on OS X) wasn't loading BAM files correctly.
- BUG: Streaming BAM files when running under web start was failing.
- BUG: Altering the BAM window size or moving the BAM window didn't update 
  the features table.

* Thu Aug 01 2013 Shane Sturrock <shane@biomatters.com> - 1.13.07.31-1
- New upstream release

* Mon May 20 2013 Simon Buxton <simon@biomatters.com> - 1.13.05.17-1
- New upstream release

* Fri May 03 2013 Shane Sturrock <shane@biomatters.com> - 1.13.05.02-1
- New upstream release

* Tue Apr 23 2013 Shane Sturrock <shane@biomatters.com> - 1.13.04.22-1
- New upstream release

* Thu Feb 07 2013 Carl Jones <carl@biomatters.com> - 1.12.12.05-4
- Fix .desktop file 

* Thu Jan 24 2013 Carl Jones <carl@biomatters.com> - 1.12.12.05-3
- Fix desktop icons path

* Thu Jan 24 2013 Carl Jones <carl@biomatters.com> - 1.12.12.05-2
- Add desktop icons

* Thu Dec 06 2012 Carl Jones <carl@biomatters.com> - 1.12.12.05-1
- New upstream release
* Thu Sep 05 2012 Carl Jones <carl@biomatters.com> - 1.12.08.29-1
- Add Requries: java-1.7.0

* Thu Sep 05 2012 Carl Jones <carl@biomatters.com> - 1.12.08.29-1
- New upstream release

* Fri Aug 03 2012 Carl Jones <carl@biomatters.com> - 1.12.03.26-3
- Add app_home patch for /usr/bin/tablet and /usr/bin/maqtoace

* Fri Aug 03 2012 Carl Jones <carl@biomatters.com> - 1.12.03.26-2
- Fix Java paths.

* Fri Aug 03 2012 Carl Jones <carl@biomatters.com> - 1.12.03.26-1
- Initial build.
