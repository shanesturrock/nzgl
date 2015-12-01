Name:		igv
Version:	2.3.67
Release:	1%{?dist}
Summary:	Integrative Genomics Viewer
Group:		Applications/Engineering
License:	LGPL
URL:		http://www.broadinstitute.org/igv/home
Source0:	igv-%{version}.zip
Source1:	igv
Source2:	igv.desktop
Source3:	igv-icons.tar.gz
Patch0:		about.properties.patch
Requires:	java-1.7.0 dejavu-sans-fonts dejavu-sans-mono-fonts dejavu-serif-fonts
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	ant

%description
The Integrative Genomics Viewer (IGV) is a high-performance visualization tool 
for interactive exploration of large, integrated genomic datasets. It supports 
a wide variety of data types, including array-based and next-generation 
sequence data, and genomic annotations.

%prep
%setup -q
%patch0 -p0
# %setup -q -n IGV_%{version}

%build
/usr/bin/ant -Dinclude.libs=true

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_javadir}/%{name}/lib
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}
install -m 0644 igv.jar %{buildroot}/%{_javadir}/%{name}
install -m 0644 lib/*.jar %{buildroot}/%{_javadir}/%{name}/lib

# Icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/
tar xf %{SOURCE3} -C %{buildroot}%{_datadir}/icons/hicolor/

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
/usr/bin/igv
/usr/share/java/igv/lib/*.jar
/usr/share/java/igv/igv.jar
/usr/share/icons/hicolor/*
/usr/share/applications/igv.desktop

%changelog
* Wed Dec 02 2015 Shane Sturrock <shane@biomatters.com> - 2.3.67-1
- No details of changes

* Fri Nov 20 2015 Shane Sturrock <shane@biomatters.com> - 2.3.66-1
- No details of changes

* Mon Nov 09 2015 Shane Sturrock <shane@biomatters.com> - 2.3.65-1
- No details of changes

* Mon Nov 02 2015 Shane Sturrock <shane@biomatters.com> - 2.3.63-1
- No details of changes

* Wed Oct 21 2015 Shane Sturrock <shane@biomatters.com> - 2.3.61-1
- VCF and bed files not loadable from Google cloud storage (gs:// urls)

* Wed Sep 23 2015 Shane Sturrock <shane@biomatters.com> - 2.3.60-1
- Bug Fixes
  - Center position off-by-one when using "goto"
- New Features and Improvements
  - New option to render bed files as arcs connecting the start and end
    position.  To use specify "graphType=arc" on the track line. An initial
    height of at least 250 pixels is recommended (track line option height=250)
  - New bisulfite option to show all "C"s irrespective of context (context =
    None)
  - Session files now uses absolute resource paths by default. There is a new
    option to force use of relative paths in the "General" category of user
    preferences.

* Mon Aug 10 2015 Shane Sturrock <shane@biomatters.com> - 2.3.59-1
- Bug Fixes
  - Splice gaps in alignments sometimes drawn as deletion when show soft clips
    is on
- New Features and Improvements
  - User preference for customizing VCF colors
  - User preference for turning on "show all bases"

* Thu Aug 06 2015 Shane Sturrock <shane@biomatters.com> - 2.3.58-1
- Support for Encode gapped peak files (extension .gappedPeak).
- Update htsjdk to version 1.138

* Mon Jun 22 2015 Shane Sturrock <shane@biomatters.com> - 2.3.57-1
- Check for "null" gap types when computing splice junctions.

* Tue Jun 02 2015 Shane Sturrock <shane@biomatters.com> - 2.3.55-1
- Upstream update, no details

* Thu May 28 2015 Shane Sturrock <shane@biomatters.com> - 2.3.53-1
- Upstream update, no details

* Thu May 06 2015 Shane Sturrock <shane@biomatters.com> - 2.3.52-1
- BAM files fail to load and hang IGV if server returns a "302" status 
  code for file not found.

* Fri Apr 24 2015 Sidney Markowitz <sidney@biomatters.com> - 2.3.51-1
- Option to add gene lists in "bed" format
- Add  "count as pairs", "extension factor" options to igvtools input form
- Add option to scale fonts for very high resolution displays.
  If the screen resolution is > 1.5 times the design resolution of
  96 dpi all fonts are scaled proportionally.
  Option set on the "Genera" tab of preferences window, default off.

* Fri Apr 10 2015 Sidney Markowitz <sidney@biomatters.com> - 2.3.49-1
- Preference window problems -- too large for 800 pixel screens,
  no default button

* Wed Apr 08 2015 Sidney Markowitz <sidney@biomatters.com> - 2.3.47-1
- Add option to filter junctions on Sashimi plot by strand
- Fix SSL certification errors when running under Java 1.8

* Wed Mar 18 2015 Shane Sturrock <shane@biomatters.com> - 2.3.46-1
- Upstream update

* Thu Mar 12 2015 Shane Sturrock <shane@biomatters.com> - 2.3.44-1
- Upstream update

* Wed Mar 11 2015 Shane Sturrock <shane@biomatters.com> - 2.3.43-1
- Upstream update

* Tue Mar 10 2015 Shane Sturrock <shane@biomatters.com> - 2.3.42-1
- Upstream update

* Mon Mar 09 2015 Shane Sturrock <shane@biomatters.com> - 2.3.41-1
- Upstream update

* Wed Feb 25 2015 Shane Sturrock <shane@biomatters.com> - 2.3.40-2
- Switch to Java 7

* Tue Nov 04 2014 Shane Sturrock <shane@biomatters.com> - 2.3.40-1
- Upstream update

* Wed Oct 29 2014 Shane Sturrock <shane@biomatters.com> - 2.3.39-1
- Upstream update

* Tue Oct 28 2014 Shane Sturrock <shane@biomatters.com> - 2.3.38-1
- Upstream update

* Wed Oct 22 2014 Shane Sturrock <shane@biomatters.com> - 2.3.37-1
- Upstream update

* Thu Oct 09 2014 Sidney Markowitz <sidney@biomatters.com> - 2.3.36-1
- Upstream update - no release notes supplied

* Wed Oct 01 2014 Shane Sturrock <shane@biomatters.com> - 2.3.35-1
- Upstream update includes fix we patched last release to fix build

* Thu Jun 26 2014 Sidney Markowitz <sidney@biomatters.com> - 2.3.34-1
- Upstream update - no release notes supplied
- Added patch to fix build error that was in the upstream update

* Thu May 22 2014 Shane Sturrock <shane@biomatters.com> - 2.3.32-1
- Upstream update

* Wed Apr 09 2014 Shane Sturrock <shane@biomatters.com> - 2.3.14-2
- Migrating into stable

* Thu Aug 08 2013 Shane Sturrock <shane@biomatters.com> - 2.3.14-1
- New upstream release - no release notes, just fixing their borked zip

* Thu Aug 08 2013 Shane Sturrock <shane@biomatters.com> - 2.3.13-1
- New upstream release - no release notes

* Wed Jul 17 2013 Shane Sturrock <shane@biomatters.com> - 2.3.12-1
- Some bigwig files fail to load with a "null pointer exception"

* Thu Jul 11 2013 Shane Sturrock <shane@biomatters.com> - 2.3.11-1
- New upstream release

* Tue Jul 09 2013 Shane Sturrock <shane@biomatters.com> - 2.3.10-1
- New upstream release

* Tue Jun 11 2013 Simon Buxton <simon@biomatters.com> - 2.3.8-1
- New upstream release

* Wed May 29 2013 Simon Buxton <simon@biomatters.com> - 2.3.6-1
- New upstream release

* Wed May 15 2013 Simon Buxton <simon@biomatters.com> - 2.3.5-1
- New upstream release

* Thu May 02 2013 Shane Sturrock <shane@biomatters.com> - 2.3.3-1
- New upstream release

* Tue Apr 23 2013 Shane Sturrock <shane@biomatters.com> - 2.3.2-1
- New upstream release

* Mon Apr 22 2013 Shane Sturrock <shane@biomatters.com> - 2.3.1-1
- New upstream release

* Tue Apr 16 2013 Shane Sturrock <shane@biomatters.com> - 2.3.0-1
- New upstream release

* Wed Mar 27 2013 Shane Sturrock <shane@biomatters.com> - 2.2.13-1
- New upstream release

* Wed Mar 20 2013 Shane Sturrock <shane@biomatters.com> - 2.2.12-1
- New upstream release

* Mon Mar 18 2013 Shane Sturrock <shane@biomatters.com> - 2.2.11-1
- New upstream release

* Mon Mar 11 2013 Simon Buxton <simon@biomatters.com> - 2.2.9-0
- New upstream release

* Mon Mar 04 2013 Shane Sturrock <shane@biomatters.com> - 2.2.8-0
- New upstream release

* Thu Feb 21 2013 Carl Jones <carl@biomatters.com> - 2.2.6-0
- New upstream release

* Thu Feb 07 2013 Carl Jones <carl@biomatters.com> - 2.2.5-2
- Update .desktop file

* Tue Jan 29 2013 Carl Jones <carl@biomatters.com> - 2.2.5-1
- New upstream release

* Wed Jan 23 2013 Carl Jones <carl@biomatters.com> - 2.2.4-3
- Run gtk-update-icon-cache after install to enable desktop icons
- Fix icon paths

* Wed Jan 23 2013 Carl Jones <carl@biomatters.com> - 2.2.4-2
- Add icons, .desktop file

* Wed Jan 16 2013 Carl Jones <carl@biomatters.com> - 2.2.4-1
- New upstream release

* Tue Jan 15 2013 Carl Jones <carl@biomatters.com> - 2.2.3-1
- New upstream release

* Tue Jan 08 2013 Carl Jones <carl@biomatters.com> - 2.2.2-1
- New upstream release

* Thu Dec 20 2012 Carl Jones <carl@biomatters.com> - 2.2.0-1
- New upstream release

* Thu Dec 13 2012 Carl Jones <carl@biomatters.com> - 2.1.30-1
- New upstream release
* Fri Dec 07 2012 Carl Jones <carl@biomatters.com> - 2.1.29-1
- New upstream release
* Wed Nov 14 2012 Carl Jones <carl@biomatters.com> - 2.1.28-1
- New upstream release
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 2.1.27-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 2.1.24-1
- New upstream release

* Fri Aug 10 2012 Carl Jones <carl@biomatters.com> - 2.1.21-4
- Fix Java paths

* Wed Aug 1 2012 Carl Jones <carl@biomatters.com> - 2.1.21-3
- Fix font deps

* Wed Aug 1 2012 Carl Jones <carl@biomatters.com> - 2.1.21-3
- Include profile.d/igv.sh

* Wed Aug 1 2012 Carl Jones <carl@biomatters.com> - 2.1.21-1
- Initial build.
