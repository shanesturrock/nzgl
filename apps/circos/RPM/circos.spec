%define ver 0.67
%define issue 7

Name:		circos
Version:	%{ver}.%{issue}
Release:	1%{?dist}
Summary:	Circos is a software package for visualizing data and information.
Group:		Applications/Engineering
License:	GPL
URL:		http://circos.ca/
Source0:	http://circos.ca/distribution/circos-%{ver}-%{issue}.tgz
Source1:	circos.sh
Requires:	perl-Statistics-Basic,perl-Math-Bezier

%description
Circos is a software package for visualizing data and information. It 
visualizes data in a circular layout — this makes Circos ideal for 
exploring relationships between objects or positions. Circos is ideal 
for creating publication-quality infographics and illustrations with a 
high data-to-ink ratio, richly layered data and pleasant symmetries. 
%prep
%setup -q -n %{name}-%{ver}-%{issue}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/opt/circos
mkdir -p %{buildroot}/etc/profile.d
/bin/cp %{SOURCE1} %{buildroot}/etc/profile.d/
/bin/cp -r bin/ data/ error/ etc/ example/ fonts/ lib/ tiles/ %{buildroot}/opt/circos/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README 
/opt/*
/etc/profile.d/circos.sh

%changelog
* Wed Mar 18 2015 Shane Sturrock <shane@biomatters.com> - 0.67.7-1
- Fixed a color bug that was ignoring transparency values in color definitions 
  in data files.

* Mon Mar 02 2015 Shane Sturrock <shane@biomatters.com> - 0.67.6-1
- Experimental support for superscripts and subscripts in SVG output.
    a_i
    a_{ijk}
    a^2
    a^{234}
- Baseline and font size shifts are defined in etc/housekeeping.conf using 
  sub_baseline_shift and sub_fontsize and analogous for sup_*.

* Thu Feb 19 2015 Shane Sturrock <shane@biomatters.com> - 0.67.5-2
- Fixes to get it working on CentOS 6

* Wed Jan 21 2015 Shane Sturrock <shane@biomatters.com> - 0.67.5-1
- Added arrows to symbols font.
- Fixed bug that was making Circos look for a file named after the 
  'background' parameter in <image>.
- Fixed bug with ideogram rules and labels. Now ideogram_label can be altered 
  by arule.

* Mon Dec 01 2014 Shane Sturrock <shane@biomatters.com> - 0.67.4-1
- Ideograms can now be filled with a pattern. In <ideogram> use
    fill_pattern = checker

* Thu Nov 27 2014 Shane Sturrock <shane@biomatters.com> - 0.67.3-1
- New stable release

* Thu Nov 20 2014 Shane Sturrock <shane@biomatters.com> - 0.67.2-1
- New stable release

* Fri Oct 02 2014 Shane Sturrock <shane@biomatters.com> - 0.67-1
- New stable release

* Thu Apr 09 2014 Shane Sturrock <shane@biomatters.com> - 0.66-1
- New stable release

* Thu Aug 08 2013 Shane Sturrock <shane@biomatters.com> - 0.64-2
- Current stable release

* Mon May 06 2013 Shane Sturrock <shane@biomatters.com> - 0.64-1
- New upstream release

* Mon Feb 18 2013 Carl Jones <carl@biomatters.com> - 0.63.4-0
- New upstream release

* Fri Feb 15 2013 Carl Jones <carl@biomatters.com> - 0.63.3-1
- Fix tarball name

* Fri Feb 15 2013 Carl Jones <carl@biomatters.com> - 0.63.3-0
- New upstream release

* Thu Feb 14 2013 Carl Jones <carl@biomatters.com> - 0.63.2-0
- New upstream release

* Mon Feb 11 2013 Carl Jones <carl@biomatters.com> - 0.63.1-1
- New upstream release

* Thu Feb 07 2013 Carl Jones <carl@biomatters.com> - 0.63-1
- New upstream release

* Wed Sep 19 2012 Carl Jones <carl@biomatters.com> - 0.62.1-1
- Fix version number
* Thu Jul 25 2012 Carl Jones <carl@biomatters.com> - 0.6.2.1-1
- Initial build.
