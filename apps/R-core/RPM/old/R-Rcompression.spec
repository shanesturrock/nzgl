%global packname  Rcompression
%global packver   0.93
%global packrel   2

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          5%{?dist}
Summary:          R Package for in-memory compression
Group:            Applications/Productivity
License:          zlib
URL:              http://www.omegahat.org/Rcompression/
Source0:          http://www.omegahat.org/Rcompression/%{packname}_%{packver}-%{packrel}.tar.gz
Patch0:           R-Rcompression-system-minizip.patch
Requires:         R-core, texlive-latex
BuildRequires:    R-devel, zlib-devel, bzip2-devel, autoconf, minizip-devel
BuildRequires:    automake, libtool

%description
This package is a basic R interface to the zlib and bzip2 facilities for 
compressing and uncompressing data that are in memory rather than in files.

%prep
%setup -c -q -n %{packname}
%patch0 -p1 -b .system-minizip
cd %{packname}
autoreconf -if

# Delete bundled minizip sources
# minizip.c is based on the minizip binary, not the library, so it needs to stay
cd src/
rm -rf crypt.h ioapi.c ioapi.h minigzip.c miniunz.c miniunzip.h unzip.c unzip.h zip.c zip.h

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

# Delete pointless sampleData directory full of test files
rm -rf %{buildroot}%{_libdir}/R/library/%{packname}/sampleData/

%check
# Recursive loop with RCurl
# Also, the tests seem to be broken.
# %{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/LICENSE
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/

%changelog
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Tom Callaway <spot@fedoraproject.org> 0.93.2-3
- delete sampleData/ because it is full of useless junk
- add missing BR

* Fri Nov 11 2011 Tom Callaway <spot@fedoraproject.org> 0.93.2-2
- unbundle minizip and use system copy

* Thu Nov 10 2011 Tom "spot" Callaway <tcallawa@redhat.com> 0.93.2-1
- initial package for Fedora
