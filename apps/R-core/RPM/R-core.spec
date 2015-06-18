%global pkgbase R
%define priority 321

Name:           R-core
Version:        3.2.1
Release:        10%{?dist}
Summary:        R-core

Group:          Applications/Engineering
License:	GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        R-2.15.3.modulefile
Source1:        R-3.0.3.modulefile
Source2:        R-3.1.3.modulefile
Source3:        R-3.2.1.modulefile
Provides:	libR.so()(64bit) libRblas.so()(64bit) libRlapack.so()(64bit)

# Post requires alternatives to install tool alternatives.
Requires(post):   %{_sbindir}/alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): %{_sbindir}/alternatives

%description

NZGL R installer

%install

# install modulefiles
install -D -p -m 0644 %SOURCE0 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/2.15.3
install -D -p -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/3.0.3
install -D -p -m 0644 %SOURCE2 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/3.1.3
install -D -p -m 0644 %SOURCE3 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/3.2.1

%clean
rm -rf %{buildroot}

%post
alternatives \
  --install %{_bindir}/R R /home/R-network/R-%{version}/bin/R %{priority} \
  --slave %{_bindir}/Rscript Rscript /home/R-network/R-%{version}/bin/Rscript

%postun
if [ $1 -eq 0 ]
then
  alternatives --remove R /home/R-network/R-%{version}/bin/R
fi

%files
%defattr(-,root,root,-)
%{_sysconfdir}/modulefiles/%{pkgbase}/2.15.3
%{_sysconfdir}/modulefiles/%{pkgbase}/3.0.3
%{_sysconfdir}/modulefiles/%{pkgbase}/3.1.3
%{_sysconfdir}/modulefiles/%{pkgbase}/3.2.1

%changelog
* Fri Jun 18 2015 Shane Sturrock <shane@biomatters.com> - 3.2.1-10
- NEW FEATURES:
  - utf8ToInt() now checks that its input is valid UTF-8 and returns
    NA if it is not.
  - install.packages() now allows type = "both" with repos = NULL if
    it can infer the type of file.
  - nchar(x, *) and nzchar(x) gain a new argument keepNA which
    governs how the result for NAs in x is determined.  For the R
    3.2.x series, the default remains FALSE which is fully back
    compatible.  From R 3.3.0, the default will change to keepNA = NA
    and you are advised to consider this for code portability.
  - news() more flexibly extracts dates from package NEWS.Rd files.
  - lengths(x) now also works (trivially) for atomic x and hence can
    be used more generally as an efficient replacement of sapply(x,
    length) and similar.
  - The included version of PCRE has been updated to 8.37, a bug-fix
    release.
  - diag() no longer duplicates a matrix when extracting its
    diagonal.
  - as.character.srcref() gains an argument to allow characters
    corresponding to a range of source references to be extracted.
- BUG FIXES:
  - acf() and ccf() now guarantee values strictly in [-1,1] (instead
    of sometimes very slightly outside). PR#15832.
  - as.integer("111111111111") now gives NA (with a warning) as it
    does for the corresponding numeric or negative number coercions.
    Further, as.integer(M + 0.1) now gives M (instead of NA) when M
    is the maximal representable integer.
  - On some platforms nchar(x, "c") and nchar(x, "w") would return
    values (possibly NA) for inputs which were declared to be UTF-8
    but were not, or for invalid strings without a marked encoding in
    a multi-byte locale, rather than give an error.  Additional
    checks have been added to mitigate this.
  - apply(a, M, function(u) c(X = ., Y = .)) again has dimnames
    containing "X" and "Y" (as in R < 3.2.0).
  - (Windows only) In some cases, the --clean option to R CMD INSTALL
    could fail.  (PR#16178)
  - (Windows only) choose.files() would occasionally include
    characters from the result of an earlier call in the result of a
    later one.  (PR#16270)
  - A change in RSiteSearch() in R 3.2.0 caused it to submit invalid
    URLs.  (PR#16329)
  - Rscript and command line R silently ignored incomplete statements
    at the end of a script; now they are reported as parse errors.
    (PR#16350)
  - Parse data for very long strings was not stored.  (PR#16354)
  - plotNode(), the workhorse of the plot method for "dendrogram"s is
    no longer recursive, thanks to Suharto Anggono, and hence also
    works for deeply nested dendrograms.  (PR#15215)
  - The parser could overflow internally when given numbers in
    scientific format with extremely large exponents.  (PR#16358)
  - If the CRAN mirror was not set, install.packages(type = "both")
    and related functions could repeatedly query the user for it.
    (Part of PR#16362)
  - The low-level functions .rowSums() etc. did not check the length
    of their argument, so could segfault. (PR#16367)
  - The quietly argument of library() is now correctly propagated
    from .getRequiredPackages2().
  - Under some circumstances using the internal PCRE when building R
    fron source would cause external libs such as -llzma to be
    omitted from the main link.
  - The .Primitive default methods of the logic operators, i.e., !, &
    and |, now give correct error messages when appropriate, e.g.,
    for `&`(TRUE) or `!`().  (PR#16385)
  - cummax(x) now correctly propagates NAs also when x is of type
    integer and begins with an NA.
  - summaryRprof() could fail when the profile contained only two
    records.  (PR#16395)
  - HTML vignettes opened using vignette() did not support links into
    the rest of the HTML help system.  (Links worked properly when
    the vignette was opened using browseVignettes() or from within
    the help system.)
  - arima(*, xreg = .) (for d >= 1) computes estimated variances
    based on a the number of effective observations as in R version
    3.0.1 and earlier.  (PR#16278)
  - slotNames(.) is now correct for "signature" objects (mostly used
    internally in methods).
  - On some systems, the first string comparison after a locale
    change would result in NA.

* Mon Jun 08 2015 Shane Sturrock <shane@biomatters.com> - 3.2.0-5
- Override Centos provided update

* Wed Apr 29 2015 Shane Sturrock <shane@biomatters.com> - 3.2.0-1
- Upstream update

* Tue Mar 10 2015 Shane Sturrock <shane@biomatters.com> - 3.1.3-1
- Upstream update

* Mon Nov 03 2014 Shane Sturrock <shane@biomatters.com> - 3.1.2-1
- Upstream update

* Wed Aug 06 2014 Shane Sturrock <shane@biomatters.com> - 3.1.1-1
- Package installer to replace system provided R
