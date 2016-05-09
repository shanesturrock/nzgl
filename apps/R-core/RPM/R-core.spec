%global pkgbase R
%define priority 330

Name:           R-core
Version:        3.3.0
Release:        10%{?dist}
Summary:        R-core

Group:          Applications/Engineering
License:	GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        R-2.15.3.modulefile
Source1:        R-3.0.3.modulefile
Source2:        R-3.1.3.modulefile
Source3:        R-3.2.5.modulefile
Source4:        R-%{version}.modulefile
Provides:	libR.so()(64bit) libRblas.so()(64bit) libRlapack.so()(64bit)
#Obsoletes:	R-core-3.2.5

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
install -D -p -m 0644 %SOURCE3 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/3.2.5
install -D -p -m 0644 %SOURCE4 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%clean
rm -rf %{buildroot}

%post
alternatives \
  --install %{_bindir}/R R /home/R-network/R-%{version}/bin/R %{priority} \
  --slave %{_bindir}/Rscript Rscript /home/R-network/R-%{version}/bin/Rscript; \alternatives --set R /home/R-network/R-3.2.5/bin/R

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
%{_sysconfdir}/modulefiles/%{pkgbase}/3.2.5
%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%changelog
* Tue May 10 2016 Shane Sturrock <shane@biomatters.com> - 3.3.0-10
- Note R 3.2.5 is still default because 3.3.0 doesn’t work with rstudio with
  the most recent version that supports CentOS 6. You need to use module load
  R/3.3.0 to access this version.
- SIGNIFICANT USER-VISIBLE CHANGES:
  - nchar(x, *)'s argument keepNA governing how the result for NAs in
    x is determined, gets a new default keepNA = NA which returns NA
    where x is NA, except for type = "width" which still returns 2,
    the formatting / printing width of NA.
  - All builds have support for https: URLs in the default methods
    for download.file(), url() and code making use of them.
    Unfortunately that cannot guarantee that any particular https:
    URL can be accessed.  For example, server and client have to
    successfully negotiate a cryptographic protocol (TLS/SSL, ...)
    and the server's identity has to be verifiable _via_ the
    available certificates.  Different access methods may allow
    different protocols or use private certificate bundles: we
    encountered a https: CRAN mirror which could be accessed by one
    browser but not by another nor by download.file() on the same
    Linux machine.
- NEW FEATURES:
  - The print method for methods() gains a byclass argument.
  - New functions validEnc() and validUTF8() to give access to the
    validity checks for inputs used by grep() and friends.
  - Experimental new functionality for S3 method checking, notably
    isS3method().
    Also, the names of the R 'language elements' are exported as
    character vector tools::langElts.
  - str(x) now displays "Time-Series" also for matrix (multivariate)
    time-series, i.e. when is.ts(x) is true.
  - (Windows only) The GUI menu item to install local packages now
    accepts *.tar.gz files as well as *.zip files (but defaults to
    the latter).
  - New programmeR's utility function chkDots().
  - D() now signals an error when given invalid input, rather than
    silently returning NA.  (Request of John Nash.)
  - formula objects are slightly more "first class": e.g., formula()
    or new("formula", y ~ x) are now valid.  Similarly, for "table",
    "ordered" and "summary.table".  Packages defining S4 classes with
    the above S3/S4 classes as slots should be reinstalled.
  - New function strrep() for repeating the elements of a character
    vector.
  - rapply() preserves attributes on the list when how = "replace".
  - New S3 generic function sigma() with methods for extracting the
    estimated standard deviation aka "residual standard deviation"
    from a fitted model.
  - news() now displays R and package news files within the HTML help
    system if it is available.  If no news file is found, a visible
    NULL is returned to the console.
  - as.raster(x) now also accepts raw arrays x assuming values in
    0:255.
  - Subscripting of matrix/array objects of type "expression" is now
    supported.
  - type.convert("i") now returns a factor instead of a complex value
    with zero real part and missing imaginary part.
  - Graphics devices cairo_pdf() and cairo_ps() now allow non-default
    values of the cairographics 'fallback resolution' to be set.
    This now defaults to 300 on all platforms: that is the default
    documented by cairographics, but apparently was not used by all
    system installations.
  - file() gains an explicit method argument rather than implicitly
    using getOption("url.method", "default").
  - Thanks to a patch from Tomas Kalibera, x[x != 0] is now typically
    faster than x[which(x != 0)] (in the case where x has no NAs, the
    two are equivalent).
  - read.table() now always uses the names for a named colClasses
    argument (previously names were only used when colClasses was too
    short). (In part, wish of PR#16478.)
  - (Windows only) download.file() with default method = "auto" and a
    ftps:// URL chooses "libcurl" if that is available.
  - The out-of-the box Bioconductor mirror has been changed to one
    using https://: use chooseBioCmirror() to choose a http:// mirror
    if required.
  - The data frame and formula methods for aggregate() gain a drop
    argument.
  - available.packages() gains a repos argument.
  - The undocumented switching of methods for url() on https: and
    ftps: URLs is confined to method = "default" (and documented).
  - smoothScatter() gains a ret.selection argument.
  - qr() no longer has a ... argument to pass additional arguments to
    methods.
  - [ has a method for class "table".
  - It is now possible (again) to replayPlot() a display list
    snapshot that was created by recordPlot() in a different R
    session.
    It is still not a good idea to use snapshots as a persistent
    storage format for R plots, but it is now not completely silly to
    use a snapshot as a format for transferring an R plot between two
    R sessions.
    The underlying changes mean that packages providing graphics
    devices (e.g., Cairo, RSvgDevice, cairoDevice, tikzDevice) will
    need to be reinstalled.
    Code for restoring snapshots was contributed by Jeroen Ooms and
    JJ Allaire.
    Some testing code is available at <URL:
    https://github.com/pmur002/R-display-list>.
  - tools::undoc(dir = D) and codoc(dir = D) now also work when D is
    a directory whose normalizePath()ed version does not end in the
    package name, e.g. from a symlink.
  - abbreviate() has more support for multi-byte character sets - it
    no longer removes bytes within characters and knows about Latin
    vowels with accents.  It is still only really suitable for (most)
    European languages, and still warns on non-ASCII input.
    abbreviate(use.classes = FALSE) is now implemented, and that is
    more suitable for non-European languages.
  - match(x, table) is faster (sometimes by an order of magnitude)
    when x is of length one and incomparables is unchanged, thanks to
    Peter Haverty (PR#16491).
  - More consistent, partly not back-compatible behavior of NA and
    NaN coercion to complex numbers, operations less often resulting
    in complex NA (NA_complex_).
  - lengths() considers methods for length and [[ on x, so it should
    work automatically on any objects for which appropriate methods
    on those generics are defined.
  - The logic for selecting the default screen device on OS X has
    been simplified: it is now quartz() if that is available even if
    environment variable DISPLAY has been set by the user.
    The choice can easily be overridden _via_ environment variable
    R_INTERACTIVE_DEVICE.
  - On Unix-like platforms which support the getline C library
    function, system(*,intern = TRUE) no longer truncates (output)
    lines longer than 8192 characters, thanks to Karl Millar.
    (PR#16544)
  - rank() gains a ties.method = "last" option, for convenience (and
    symmetry).
  - regmatches(invert = NA) can now be used to extract both
    non-matched and matched substrings.
  - data.frame() gains argument fix.empty.names; as.data.frame.list()
    gets new cut.names, col.names and fix.empty.names.
  - plot(x ~ x, *) now warns that it is the same as plot(x ~ 1, *).
  - recordPlot() has new arguments load and attach to allow package
    names to be stored as part of a recorded plot.  replayPlot() has
    new argument reloadPkgs to load/attach any package names that
    were stored as part of a recorded plot.
  - S4 dispatch works within calls to .Internal(). This means
    explicit S4 generics are no longer needed for unlist() and
    as.vector().
  - Only font family names starting with "Hershey" (and not "Her" as
    before) are given special treatment by the graphics engine.
  - S4 values are automatically coerced to vector (via as.vector)
    when subassigned into atomic vectors.
  - findInterval() gets a left.open option.
  - The version of LAPACK included in the sources has been updated to
    3.6.0, including those 'deprecated' routines which were
    previously included.  _Ca_ 40 double-complex routines have been
    added at the request of a package maintainer.
    As before, the details of what is included are in
    src/modules/lapack/README and this now gives information on
    earlier additions.
  - tapply() has been made considerably more efficient without
    changing functionality, thanks to proposals from Peter Haverty
    and Suharto Anggono.  (PR#16640)
  - match.arg(arg) (the one-argument case) is faster; so is
    sort.int().  (PR#16640)
  - The format method for object_size objects now also accepts
    "binary" units such as "KiB" and e.g., "Tb".  (Partly from
    PR#16649.)
  - Profiling now records calls of the form foo::bar and some similar
    cases directly rather than as calls to <Anonymous>.  Contributed
    by Winston Chang.
  - New string utilities startsWith(x, prefix) and endsWith(x,
    suffix).  Also provide speedups for some grepl("^...",*) uses
    (related to proposals in PR#16490).
  - Reference class finalizers run at exit, as well as on garbage
    collection.
  - Avoid parallel dependency on stats for port choice and random
    number seeds.  (PR#16668)
  - The radix sort algorithm and implementation from data.table
    (forder) replaces the previous radix (counting) sort and adds a
    new method for order().  Contributed by Matt Dowle and Arun
    Srinivasan, the new algorithm supports logical, integer (even
    with large values), real, and character vectors.  It outperforms
    all other methods, but there are some caveats (see ?sort).
  - The order() function gains a method argument for choosing between
    "shell" and "radix".
  - New function grouping() returns a permutation that stably
    rearranges data so that identical values are adjacent.  The
    return value includes extra partitioning information on the
    groups.  The implementation came included with the new radix
    sort.
  - rhyper(nn, m, n, k) no longer returns NA when one of the three
    parameters exceeds the maximal integer.
  - switch() now warns when no alternatives are provided.
  - parallel::detectCores() now has default logical = TRUE on all
    platforms - as this was the default on Windows, this change only
    affects Sparc Solaris.
    Option logical = FALSE is now supported on Linux and recent
    versions of OS X (for the latter, thanks to a suggestion of Kyaw
    Sint).
  - hist() for "Date" or "POSIXt" objects would sometimes give
    misleading labels on the breaks, as they were set to the day
    before the start of the period being displayed.  The display
    format has been changed, and the shift of the start day has been
    made conditional on right = TRUE (the default).  (PR#16679)
  - R now uses a new version of the logo (donated to the R Foundation
    by RStudio).  It is defined in .svg format, so will resize
    without unnecessary degradation when displayed on HTML
    pages-there is also a vector PDF version.  Thanks to Dirk
    Eddelbuettel for producing the corresponding X11 icon.
  - New function .traceback() returns the stack trace which
    traceback() prints.
  - lengths() dispatches internally.
  - dotchart() gains a pt.cex argument to control the size of points
    separately from the size of plot labels.  Thanks to Michael
    Friendly and Milan Bouchet-Valat for ideas and patches.
  - as.roman(ch) now correctly deals with more diverse character
    vectors ch; also arithmetic with the resulting roman numbers
    works in more cases.  (PR#16779)
  - prcomp() gains a new option rank. allowing to directly aim for
    less than min(n,p) PC's.  The summary() and its print() method
    have been amended, notably for this case.
  - gzcon() gains a new option text, which marks the connection as
    text-oriented (so e.g. pushBack() works).  It is still always
    opened in binary mode.
  - The import() namespace directive now accepts an argument except
    which names symbols to exclude from the imports. The except
    expression should evaluate to a character vector (after
    substituting symbols for strings). See Writing R Extensions.
  - New convenience function Rcmd() in package tools for invoking R
    CMD tools from within R.
  - New functions makevars_user() and makevars_site() in package
    tools to determine the location of the user and site specific
    Makevars files for customizing package compilation.
- UTILITIES:
  - R CMD check has a new option --ignore-vignettes for use with
    non-Sweave vignettes whose VignetteBuilder package is not
    available.
  - R CMD check now by default checks code usage (_via_ codetools)
    with only the base package attached.  Functions from default
    packages other than base which are used in the package code but
    not imported are reported as undefined globals, with a suggested
    addition to the NAMESPACE file.
  - R CMD check --as-cran now also checks DOIs in package CITATION
    and Rd files.
  - R CMD Rdconv and R CMD Rd2pdf each have a new option
    --RdMacros=pkglist which allows Rd macros to be specified before
    processing.
- DEPRECATED AND DEFUNCT:
  - The previously included versions of zlib, bzip2, xz and PCRE have
    been removed, so suitable external (usually system) versions are
    required (see the 'R Installation and Administration' manual).
  - The unexported and undocumented Windows-only devices cairo_bmp(),
    cairo_png() and cairo_tiff() have been removed.  (These devices
    should be used as e.g. bmp(type = "cairo").)
  - (Windows only) Function setInternet2() has no effect and will be
    removed in due course.  The choice between methods "internal" and
    "wininet" is now made by the method arguments of url() and
    download.file() and their defaults can be set _via_ options.  The
    out-of-the-box default remains "wininet" (as it has been since R
    3.2.2).
  - [<- with an S4 value into a list currently embeds the S4 object
    into its own list such that the end result is roughly equivalent
    to using [[<-.  That behavior is deprecated.  In the future, the
    S4 value will be coerced to a list with as.list().
  - Package tools' functions package.dependencies(), pkgDepends(),
    etc are deprecated now, mostly in favor of package_dependencies()
    which is both more flexible and efficient.
- INSTALLATION and INCLUDED SOFTWARE:
  - Support for very old versions of valgrind (e.g., 3.3.0) has been
    removed.
  - The included libtool script (generated by configure) has been
    updated to version 2.4.6 (from 2.2.6a).
  - libcurl version 7.28.0 or later with support for the https
    protocol is required for installation (except on Windows).
  - BSD networking is now required (except on Windows) and so
    capabilities("http/ftp") is always true.
  - configure uses pkg-config for PNG, TIFF and JPEG where this is
    available.  This should work better with multiple installs and
    with those using static libraries.
  - The minimum supported version of OS X is 10.6 ('Snow Leopard'):
    even that has been unsupported by Apple since 2012.
  - The configure default on OS X is --disable-R-framework: enable
    this if you intend to install under /Library/Frameworks and use
    with R.app.
  - The minimum preferred version of PCRE has since R 3.0.0 been 8.32
    (released in Nov 2012).  Versions 8.10 to 8.31 are now deprecated
    (with warnings from configure), but will still be accepted until
    R 3.4.0.
  - configure looks for C functions __cospi, __sinpi and __tanpi and
    uses these if cospi _etc_ are not found.  (OS X is the main
    instance.)
  - (Windows) R is now built using gcc 4.9.3.  This build will
    require recompilation of at least those packages that include C++
    code, and possibly others.  A build of R-devel using the older
    toolchain will be temporarily available for comparison purposes.
    During the transition, the environment variable R_COMPILED_BY has
    been defined to indicate which toolchain was used to compile R
    (and hence, which should be used to compile code in packages).
    The COMPILED_BY variable described below will be a permanent
    replacement for this.
  - (Windows) A make and R CMD config variable named COMPILED_BY has
    been added.  This indicates which toolchain was used to compile R
    (and hence, which should be used to compile code in packages).
- PACKAGE INSTALLATION:
  - The make macro AWK which used to be made available to files such
    as src/Makefile is no longer set.
- C-LEVEL FACILITIES:
  - The API call logspace_sum introduced in R 3.2.0 is now remapped
    as an entry point to Rf_logspace_sum, and its first argument has
    gained a const qualifier.  (PR#16470)
    Code using it will need to be reinstalled.
    Similarly, entry point log1pexp also defined in Rmath.h is
    remapped there to Rf_log1pexp
  - R_GE_version has been increased to 11.
  - New API call R_orderVector1, a faster one-argument version of
    R_orderVector.
  - When R headers such as R.h and Rmath.h are called from C++ code
    in packages they include the C++ versions of system headers such
    as <cmath> rather than the legacy headers such as <math.h>.
    (Headers Rinternals.h and Rinterface.h already did, and inclusion
    of system headers can still be circumvented by defining
    NO_C_HEADERS, including as from this version for those two
    headers.)
    The manual has long said that R headers should *not* be included
    within an extern "C" block, and almost all the packages affected
    by this change were doing so.
  - Including header S.h from C++ code would fail on some platforms,
    and so gives a compilation error on all.
  - The deprecated header Rdefines.h is now compatible with defining
    R_NO_REMAP.
  - The connections API now includes a function R_GetConnection()
    which allows packages implementing connections to convert R
    connection objects to Rconnection handles used in the API. Code
    which previously used the low-level R-internal getConnection()
    entry point should switch to the official API.
- BUG FIXES:
  - C-level asChar(x) is fixed for when x is not a vector, and it
    returns "TRUE"/"FALSE" instead of "T"/"F" for logical vectors.
  - The first arguments of .colSums() etc (with an initial dot) are
    now named x rather than X (matching colSums()): thus error
    messages are corrected.
  - A coef() method for class "maov" has been added to allow vcov()
    to work with multivariate results. (PR#16380)
  - method = "libcurl" connections signal errors rather than
    retrieving HTTP error pages (where the ISP reports the error).
  - xpdrows.data.frame() was not checking for unique row names; in
    particular, this affected assignment to non-existing rows via
    numerical indexing. (PR#16570)
  - tail.matrix() did not work for zero rows matrices, and could
    produce row "labels" such as "[1e+05,]".
  - Data frames with a column named "stringsAsFactors" now format and
    print correctly.  (PR#16580)
  - cor() is now guaranteed to return a value with absolute value
    less than or equal to 1. (PR#16638)
  - Array subsetting now keeps names(dim(.)).
  - Blocking socket connection selection recovers more gracefully on
    signal interrupts.
  - The data.frame method of rbind() construction row.names works
    better in borderline integer cases, but may change the names
    assigned.  (PR#16666)
  - (X11 only) getGraphicsEvent() miscoded buttons and missed mouse
    motion events.  (PR#16700)
  - methods(round) now also lists round.POSIXt.
  - tar() now works with the default files = NULL.  (PR#16716)
  - Jumps to outer contexts, for example in error recovery, now make
    intermediate jumps to contexts where on.exit() actions are
    established instead of trying to run all on.exit() actions before
    jumping to the final target. This unwinds the stack gradually,
    releases resources held on the stack, and significantly reduces
    the chance of a segfault when running out of C stack space. Error
    handlers established using withCallingHandlers() and
    options("error") specifications are ignored when handling a C
    stack overflow error as attempting one of these would trigger a
    cascade of C stack overflow errors.  (These changes resolve
    PR#16753.)
  - The spacing could be wrong when printing a complex array.
    (Report and patch by Lukas Stadler.)
  - pretty(d, n, min.n, *) for date-time objects d works again in
    border cases with large min.n, returns a labels attribute also
    for small-range dates and in such cases its returned length is
    closer to the desired n.  (PR#16761) Additionally, it finally
    does cover the range of d, as it always claimed.
  - tsp(x) <- NULL did not handle correctly objects inheriting from
    both "ts" and "mts".  (PR#16769)
  - install.packages() could give false errors when
    options("pkgType") was "binary".  (Reported by Jose Claudio
    Faria.)
  - A bug fix in R 3.0.2 fixed problems with locator() in X11, but
    introduced problems in Windows.  Now both should be fixed.
    (PR#15700)
  - download.file() with method = "wininet" incorrectly warned of
    download file length difference when reported length was unknown.
    (PR#16805)
  - diag(NULL, 1) crashed because of missed type checking.
    (PR#16853)

* Mon Apr 18 2016 Shane Sturrock <shane@biomatters.com> - 3.2.5-10
- BUG FIXES:
  - format.POSIXlt() behaved incorrectly in R 3.2.4.  E.g. the output of
    format(as.POSIXlt(paste0(1940:2000,"-01-01"), tz = "CET"), usetz = TRUE)
    ended in two "CEST" time formats.
  - A typo in the Makefile for src/extra/xz prevented builds of liblzma.a.
    (Notice that this will become unbundled in 3.3.0.)

* Thu Mar 17 2016 Shane Sturrock <shane@biomatters.com> - 3.2.4-10
NEW FEATURES:
- install.packages() and related functions now give a more
  informative warning when an attempt is made to install a base
  package.
- summary(x) now prints with less rounding when x contains infinite
  values. (Request of PR#16620.)
- provideDimnames() gets an optional unique argument.
- shQuote() gains type = "cmd2" for quoting in cmd.exe in Windows.
  (Response to PR#16636.)
- The data.frame method of rbind() gains an optional argument
  stringsAsFactors (instead of only depending on
  getOption("stringsAsFactors")).
- smooth(x, *) now also works for long vectors.
- tools::texi2dvi() has a workaround for problems with the texi2dvi
  script supplied by texinfo 6.1.
  It extracts more error messages from the LaTeX logs when in
  emulation mode.
UTILITIES:
- R CMD check will leave a log file build_vignettes.log from the
  re-building of vignettes in the .Rcheck directory if there is a
  problem, and always if environment variable
  _R_CHECK_ALWAYS_LOG_VIGNETTE_OUTPUT_ is set to a true value.
DEPRECATED AND DEFUNCT:
- Use of SUPPORT_OPENMP from header Rconfig.h is deprecated in
  favour of the standard OpenMP define _OPENMP.
  (This has been the recommendation in the manual for a while now.)
- The make macro AWK which is long unused by R itself but recorded
  in file etc/Makeconf is deprecated and will be removed in R
  3.3.0.
- The C header file S.h is no longer documented: its use should be
  replaced by R.h.
BUG FIXES:
- kmeans(x, centers = <1-row>) now works. (PR#16623)
- Vectorize() now checks for clashes in argument names.  (PR#16577)
- file.copy(overwrite = FALSE) would signal a successful copy when
  none had taken place.  (PR#16576)
- ngettext() now uses the same default domain as gettext().
  (PR#14605)
- array(.., dimnames = *) now warns about non-list dimnames and,
  from R 3.3.0, will signal the same error for invalid dimnames as
  matrix() has always done.
- addmargins() now adds dimnames for the extended margins in all
  cases, as always documented.
- heatmap() evaluated its add.expr argument in the wrong
  environment.  (PR#16583)
- require() etc now give the correct entry of lib.loc in the
  warning about an old version of a package masking a newer
  required one.
- The internal deparser did not add parentheses when necessary,
  e.g. before [] or [[]].  (Reported by Lukas Stadler; additional
  fixes included as well).
- as.data.frame.vector(*, row.names=*) no longer produces
  'corrupted' data frames from row names of incorrect length, but
  rather warns about them.  This will become an error.
- url connections with method = "libcurl" are destroyed properly.
  (PR#16681)
- withCallingHandler() now (again) handles warnings even during S4
  generic's argument evaluation.  (PR#16111)
- deparse(..., control = "quoteExpressions") incorrectly quoted
  empty expressions.  (PR#16686)
- format()ting datetime objects ("POSIX[cl]?t") could segfault or
  recycle wrongly.  (PR#16685)
- plot.ts(<matrix>, las = 1) now does use las.
- saveRDS(*, compress = "gzip") now works as documented.
  (PR#16653)
- (Windows only) The Rgui front end did not always initialize the
  console properly, and could cause R to crash.  (PR#16998)
- dummy.coef.lm() now works in more cases, thanks to a proposal by
  Werner Stahel (PR#16665).  In addition, it now works for
  multivariate linear models ("mlm", manova) thanks to a proposal
  by Daniel Wollschlaeger.
- The as.hclust() method for "dendrogram"s failed often when there
  were ties in the heights.
- reorder() and midcache.dendrogram() now are non-recursive and
  hence applicable to somewhat deeply nested dendrograms, thanks to
  a proposal by Suharto Anggono in PR#16424.
- cor.test() now calculates very small p values more accurately
  (affecting the result only in extreme not statistically relevant
  cases).  (PR#16704)
- smooth(*, do.ends=TRUE) did not always work correctly in R
  versions between 3.0.0 and 3.2.3.
- pretty(D) for date-time objects D now also works well if range(D)
  is (much) smaller than a second.  In the case of only one unique
  value in D, the pretty range now is more symmetric around that
  value than previously.
  Similarly, pretty(dt) no longer returns a length 5 vector with
  duplicated entries for Date objects dt which span only a few
  days.
- The figures in help pages such as ?points were accidentally
  damaged, and did not appear in R 3.2.3.  (PR#16708)
- available.packages() sometimes deleted the wrong file when
  cleaning up temporary files.  (PR#16712)
- The X11() device sometimes froze on Red Hat Enterprise Linux 6.
  It now waits for MapNotify events instead of Expose events,
  thanks to Siteshwar Vashisht. (PR#16497)
- [dpqr]nbinom(*, size=Inf, mu=.) now works as limit case, for
  'dpq' as the Poisson.  (PR#16727)
  pnbinom() no longer loops infinitely in border cases.
- approxfun(*, method="constant") and hence ecdf() which calls the
  former now correctly "predict" NaN values as NaN.
- summary.data.frame() now displays NAs in Date columns in all
  cases.  (PR#16709)

* Fri Dec 11 2015 Shane Sturrock <shane@biomatters.com> - 3.2.3-10
NEW FEATURES:
- which.min(x) and which.max(x) may be much faster for logical and
  integer x and now also work for long vectors.
- The 'emulation' part of tools::texi2dvi() has been somewhat
  enhanced, including supporting quiet = TRUE.  It can be selected
  by texi2dvi = "emulation".
- loess(..., iterTrace=TRUE) now provides diagnostics for
  robustness iterations, and the print() method for
  summary(<loess>) shows slightly more.
- The included version of PCRE has been updated to 8.38, a bug-fix
  release.
- View() now displays nested data frames in a more friendly way.
  (Request with patch in PR#15915.)
INSTALLATION and INCLUDED SOFTWARE:
- The included configuration code for libintl has been updated to
  that from gettext version 0.19.5.1 - this should only affect how
  an external library is detected (and the only known instance is
  under OpenBSD).  (Wish of PR#16464.)
- configure has a new argument --disable-java to disable the checks
  for Java.
- The configure default for MAIN_LDFLAGS has been changed for the
  FreeBSD, NetBSD and Hurd OSes to one more likely to work with
  compilers other than gcc (FreeBSD 10 defaults to clang).
- configure now supports the OpenMP flags -fopenmp=libomp (clang)
  and -qopenmp (Intel C).
- Various macros can be set to override the default behaviour of
  configure when detecting OpenMP: see file config.site.
BUG FIXES:
- regexpr(pat, x, perl = TRUE) with Python-style named capture did
  not work correctly when x contained NA strings.  (PR#16484)
- The description of dataset ToothGrowth has been
  improved/corrected.  (PR#15953)
- model.tables(type = "means") and hence TukeyHSD() now support
  "aov" fits without an intercept term.  (PR#16437)
- close() now reports the status of a pipe() connection opened with
  an explicit open argument.  (PR#16481)
- Coercing a list without names to a data frame is faster if the
  elements are very long. (PR#16467)
- (Unix-only) Under some rare circumstances piping the output from
  Rscript or R -f could result in attempting to close the input
  file twice, possibly crashing the process.  (PR#16500)
- topenv(baseenv()) returns baseenv() again as in R 3.1.0 and
  earlier.  This also fixes compilerJIT(3) when used in .Rprofile.
- detach()ing the methods package keeps .isMethodsDispatchOn()
  true, as long as the methods namespace is not unloaded.
- Removed some spurious warnings from configure about the
  preprocessor not finding header files.  (PR#15989)
- rchisq(*, df=0, ncp=0) now returns 0 instead of NaN, and
  dchisq(*, df=0, ncp=*) also no longer returns NaN in limit cases
  (where the limit is unique).  (PR#16521)
- pchisq(*, df=0, ncp > 0, log.p=TRUE) no longer underflows (for
  ncp > ~60).
- nchar(x, "w") returned -1 for characters it did not know about
  (e.g. zero-width spaces): it now assumes 1.  It now knows about
  most zero-width characters and a few more double-width
  characters.
- Help for which.min() is now more precise about behavior with
  logical arguments.  (PR#16532)
- The print width of character strings marked as "latin1" or
  "bytes" was in some cases computed incorrectly.
- abbreviate() did not give names to the return value if minlength
  was zero, unlike when it was positive.
- When operating in a non-UTF-8 multibyte locale (e.g. an East
  Asian locale on Windows), grep() and related functions did not
  handle UTF-8 strings properly.  (PR#16264)
- read.dcf() sometimes misread lines longer than 8191 characters.
  (Reported by Herv'e Pag`es with a patch.)
- within(df, ..) no longer drops columns whose name start with a
  ".".
- The built-in HTTP server converted entire Content-Type to
  lowercase including parameters which can cause issues for
  multi-part form boundaries (PR#16541).
- Modifying slots of S4 objects could fail when the methods package
  was not attached. (PR#16545)
- splineDesign(*, outer.ok=TRUE) (splines) is better now
  (PR#16549), and interpSpline() now allows sparse=TRUE for speedup
  with non-small sizes.
- If the expression in the traceback was too long, traceback() did
  not report the source line number.  (Patch by Kirill M"uller.)
- The browser did not truncate the display of the function when
  exiting with options("deparse.max.lines") set.  (PR#16581)
- When bs(*, Boundary.knots=) had boundary knots inside the data
  range, extrapolation was somewhat off.  (Patch by Trevor Hastie.)
- var() and hence sd() warn about factor arguments which are
  deprecated now. (PR#16564)
- loess(*, weights = *) stored wrong weights and hence gave
  slightly wrong predictions for newdata.  (PR#16587)
- aperm(a, *) now preserves names(dim(a)).
- poly(x, ..) now works when either raw=TRUE or coef is specified.
  (PR#16597)
- data(package=*) is more careful in determining the path.
- prettyNum(*, decimal.mark, big.mark): fixed bug introduced when
  fixing PR#16411.

Tue Aug 18 2015 Shane Sturrock <shane@biomatters.com> - 3.2.2-10
NEW FEATURES
- cmdscale() gets new option list. for increased flexibility when a list
  should be returned.
- configure now supports texinfo version 6.0, which (unlike the change from
  4.x to 5.0) is a minor update. (Wish of PR#16456.)
- download.file() with default method = "auto" now chooses "libcurl" if that
  is available and a https:// or ftps:// URL is used.
- chooseCRANmirror() and chooseBioCmirror() now offer HTTPS mirrors in
  preference to HTTP mirrors. This changes the interpretation of their ind
  arguments: see their help pages.
- capture.output() gets optional arguments type and split to pass to sink(),
  and hence can be used to capture messages.
BUG FIXES
- The HTML help page links to demo code failed due to a change in R 3.2.0.
  (PR#16432)
- If the na.action argument was used in model.frame(), the original data
  could be modified. (PR#16436)
- getGraphicsEvent() could cause a crash if a graphics window was closed
  while it was in use. (PR#16438)
- matrix(x, nr, nc, byrow = TRUE) failed if x was an object of type
  "expression".
- strptime() could overflow the allocated storage on the C stack when the
  timezone had a non-standard format much longer than the standard formats.
  (Part of PR#16328.)
- options(OutDec = s) now signals a warning (which will become an error in
  the future) when s is not a string with exactly one character, as that has
  been a documented requirement.
- prettyNum() gains a new option input.d.mark which together with other
  changes, e.g., the default for decimal.mark, fixes some format()ting
  variants with non-default getOption("OutDec") such as in PR#16411.
- download.packages() failed for type equal to either "both" or "binary".
  (Reported by Dan Tenenbaum.)
- The dendrogram method of labels() is much more efficient for large
  dendrograms, now using rapply(). (Comment #15 of PR#15215)
- The "port" algorithm of nls() could give spurious errors. (Reported by
  Radford Neal.)
- Reference classes that inherited from reference classes in another package
  could invalidate methods of the inherited class. Fixing this requires
  adding the ability for methods to be “external”, with the object supplied
  explicitly as the first argument, named .self. See "Inter-Package 
  Superclasses" in the documentation.
- readBin() could fail on the SPARC architecture due to alignment issues.
  (Reported by Radford Neal.)
- qt(*, df=Inf, ncp=.) now uses the natural qnorm() limit instead of
  returning NaN. (PR#16475)
- Auto-printing of S3 and S4 values now searches for print() in the base
  namespace and show() in the methods namespace instead of searching the
  global environment.
- polym() gains a coefs = NULL argument and returns class "poly" just like
  poly() which gets a new simple=FALSE option. They now lead to correct
  predict()ions, e.g., on subsets of the original data.
- rhyper(nn, <large>) now works correctly. (PR#16489)
- ttkimage() did not (and could not) work so was removed. Ditto for
  tkimage.cget() and tkimage.configure(). Added two Ttk widgets and missing
  subcommands for Tk's image command: ttkscale(), ttkspinbox(), 
  tkimage.delete(), tkimage.height(), tkimage.inuse(), tkimage.type(), 
  tkimage.types(), tkimage.width(). (PR#15372, PR#16450)
- getClass("foo") now also returns a class definition when it is found in the
  cache more than once.

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
