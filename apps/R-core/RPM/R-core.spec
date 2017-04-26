%global pkgbase R
%define priority 340

Name:           R-core
Version:        3.4.0
Release:        10%{?dist}
Summary:        R-core

Group:          Applications/Engineering
License:	GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        R-2.15.3.modulefile
Source1:        R-3.0.3.modulefile
Source2:        R-3.1.3.modulefile
Source3:        R-3.2.5.modulefile
Source4:        R-3.3.3.modulefile
Source5:        R-%{version}.modulefile
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
install -D -p -m 0644 %SOURCE4 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/3.3.3
install -D -p -m 0644 %SOURCE5 %{buildroot}%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%clean
rm -rf %{buildroot}

%post
alternatives \
  --install %{_bindir}/R R /home/R-network/R-3.2.5/bin/R 325 \
  --slave %{_bindir}/Rscript Rscript /home/R-network/R-3.2.5/bin/Rscript; \
alternatives \
  --install %{_bindir}/R R /home/R-network/R-%{version}/bin/R %{priority} \
  --slave %{_bindir}/Rscript Rscript /home/R-network/R-%{version}/bin/Rscript; \
alternatives --set R /home/R-network/R-3.2.5/bin/R

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
%{_sysconfdir}/modulefiles/%{pkgbase}/3.3.3
%{_sysconfdir}/modulefiles/%{pkgbase}/%{version}

%changelog
* Wed Apr 26 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 3.4.0-10
- SIGNIFICANT USER-VISIBLE CHANGES
  - (Unix-alike) The default methods for download.file() and url() now choose
    "libcurl" except for file:// URLs. There will be small changes in the
    format and wording of messages, including in rare cases if an issue is a
    warning or an error. For example, when HTTP re-direction occurs, some 
    messages refer to the final URL rather than the specified one.

    Those who use proxies should check that their settings are compatible (see
    ?download.file: the most commonly used forms work for both "internal" and
    "libcurl").
  - table() has been amended to be more internally consistent and become back
    compatible to R <= 2.7.2 again. Consequently, table(1:2, exclude = NULL) no
    longer contains a zero count for <NA>, but useNA = "always" continues to 
    do so.
  - summary.default() no longer rounds, but its print method does resulting in
    less extraneous rounding, notably of numbers in the ten thousands.
  - factor(x, exclude = L) behaves more rationally when x or L are character
    vectors. Further, exclude = <factor> now behaves as documented for long.
  - Arithmetic, logic (&, |) and comparison (aka ‘relational’, e.g., <, ==)
    operations with arrays now behave consistently, notably for arrays of
    length zero.
  - Arithmetic between length-1 arrays and longer non-arrays had silently
    dropped the array attributes and recycled. This now gives a warning and
    will signal an error in the future, as it has always for logic and 
    comparison operations in these cases (e.g., compare matrix(1,1) + 2:3 and 
    matrix(1,1) < 2:3).
  - The JIT (‘Just In Time’) byte-code compiler is now enabled by default at
    its level 3. This means functions will be compiled on first or second use
    and top-level loops will be compiled and then run. (Thanks to Tomas Kalibera
    for extensive work to make this possible.)
  - For now, the compiler will not compile code containing explicit calls to
    browser(): this is to support single stepping from the browser() call.
  - JIT compilation can be disabled for the rest of the session using
    compiler::enableJIT(0) or by setting environment variable R_ENABLE_JIT to
    0.
  - xtabs() works more consistently with NAs, also in its result no longer
    setting them to 0. Further, a new logical option addNA allows to count NAs
    where appropriate. Additionally, for the case sparse = TRUE, the result's
    dimnames are identical to the default case's.
  - Matrix products now consistently bypass BLAS when the inputs have NaN/Inf
    values. Performance of the check of inputs has been improved. Performance
    when BLAS is used is improved for matrix/vector and vector/matrix
    multiplication (DGEMV is now used instead of DGEMM).
  - One can now choose from alternative matrix product implementations via
    options(matprod = ). The "internal" implementation is not optimized for
    speed but consistent in precision with other summations in R (using long 
    double accumulators where available). "blas" calls BLAS directly for best 
    speed, but usually with undefined behavior for inputs with NaN/Inf.
  - factor() now uses order() to sort its levels, not sort.list(). This makes
    factor() support custom vector-like objects if methods for the appropriate
    generics are defined. This change has the side effect of making factor()
    succeed on empty or length-one non-atomic vector(-like) types (e.g., list),
    where it failed before.
- NEW FEATURES
  - User errors such as integrate(f, 0:1, 2) are now caught.
  - Add signature argument to debug(), debugonce(), undebug() and isdebugged()
    for more conveniently debugging S3 and S4 methods. (Based on a patch by
    Gabe Becker.)
  - Add utils::debugcall() and utils::undebugcall() for debugging the function
    that would be called by evaluating the given expression. When the call is
    to an S4 generic or standard S3 generic, debugcall() debugs the method that
    would be dispatched. A number of internal utilities were added to support 
    this, most notably utils::isS3stdGeneric(). (Based on a patch by Gabe 
    Becker.)
  - Add utils::strcapture(). Given a character vector and a regular expression
    containing capture expressions, strcapture() will extract the captured
    tokens into a tabular data structure, typically a data.frame.
  - str() and strOptions() get a new option drop.deparse.attr with improved but
    changed default behaviour for expressions. For expression objects x, str(x)
    now may remove extraneous white space and truncate long lines.
  - str(<looooooooong_string>) is no longer very slow; inspired by Mikko
    Korpela's proposal in PR#16527.
  - str(x)'s default method is more “accurate” and hence somewhat more generous
    in displaying character vectors; this will occasionally change R outputs
    (and need changes to some ‘*.Rout(.save)’ files). For a classed integer 
    vector such as x <- xtabs(~ c(1,9,9,9)), str(x) now shows both the class 
    and "int", instead of only the latter.
  - isSymmetric(m) is much faster for large asymmetric matrices m via pre-tests
    and a new option tol1 (with which strict back compatibility is possible but
    not the default).
  - The result of eigen() now is of class "eigen" in the default case when
    eigenvectors are computed.
  - Zero-length date and date-time objects (of classes "POSIX[cl]?t") now
    print() “recognizably”.
  - xy.coords() and xyz.coords() get a new setLab option.
  - The method argument of sort.list(), order() and sort.int() gains an "auto"
    option (the default) which should behave the same as before when method was
    not supplied.
  - stopifnot(E, ..) now reports differences when E is a call to all.equal()
    and that is not true.
  - boxplot(<formula>, *) gain optional arguments drop, sep, and lex.order to
    pass to split.default() which itself gains an argument lex.order to pass to
    interaction() for more flexibility.
  - The plot() method for ppr() has enhanced default labels (xmin and main).
  - sample.int() gains an explicit useHash option (with a back compatible
    default).
  - identical() gains an ignore.srcref option which drops "srcref" and similar
    attributes when true (as by default).
  - diag(x, nrow = n) now preserves typeof(x), also for logical, integer and
    raw x (and as previously for complex and numeric).
  - smooth.spline() now allows direct specification of lambda, gets a
    hatvalues() method and keeps tol in the result, and optionally parts of the
    internal matrix computations.
  - addNA() is faster now, e.g. when applied twice. (Part of PR#16895.)
  - New option rstandard(<lm>, type = "predicted") provides the “PRESS”–related
    leave-one-out cross-validation errors for linear models.
  - After seven years of deprecation, duplicated factor levels now produce a
    warning when printed and an error in levels<- instead of a warning.
  - Invalid factors, e.g., with duplicated levels (invalid but constructable)
    now give a warning when printed, via new function .valid.factor().
  - sessionInfo() has been updated for Apple's change in OS naming as from
    ‘10.12’ (‘macOS Sierra’ vs ‘OS X El Capitan’).
  - Its toLatex() method now includes the running component.
  - options(interrupt=) can be used to specify a default action for user
    interrupts. For now, if this option is not set and the error option is set,
    then an unhandled user interrupt invokes the error option. (This may be 
    dropped in the future as interrupt conditions are not error conditions.)
  - In most cases user interrupt handlers will be called with a "resume"
    restart available. Handlers can invoke this restart to resume computation.
    At the browser prompt the r command will invoke a "resume" restart if one is
    available. Some read operations cannot be resumed properly when interrupted 
    and do not provide a "resume" restart.
  - Radix sort is now chosen by method = "auto" for sort.int() for double
    vectors (and hence used for sort() for unclassed double vectors), excluding
    ‘long’ vectors.
  - sort.int(method = "radix") no longer rounds double vectors.
  - The default and data.frame methods for stack() preserve the names of empty
    elements in the levels of the ind column of the return value. Set the new
    drop argument to TRUE for the previous behavior.
  - Speedup in simplify2array() and hence sapply() and mapply() (for the case
    of names and common length > 1), thanks to Suharto Anggono's PR#17118.
  - table(x, exclude = NULL) now sets useNA = "ifany" (instead of "always").
    Together with the bug fixes for this case, this recovers more consistent
    behaviour compatible to older versions of R. As a consequence, summary() 
    for a logical vector no longer reports (zero) counts for NA when there are 
    no NAs.
  - dump.frames() gets a new option include.GlobalEnv which allows to also dump
    the global environment, thanks to Andreas Kersting's proposal in PR#17116.
  - system.time() now uses message() instead of cat() when terminated early,
    such that suppressMessages() has an effect; suggested by Ben Bolker.
  - citation() supports ‘inst/CITATION’ files from package source trees, with
    lib.loc pointing to the directory containing the package.
  - try() gains a new argument outFile with a default that can be modified via
    options(try.outFile = .), useful notably for Sweave.
  - The unexported low-level functions in package parallel for passing
    serialized R objects to and from forked children now support long vectors
    on 64-bit platforms. This removes some limits on higher-level functions 
    such as mclapply() (but returning gigabyte results from forked processes 
    via serialization should be avoided if at all possible).
  - Connections now print() without error even if invalid, e.g. after having
    been destroyed.
  - apropos() and find(simple.words = FALSE) no longer match object names
    starting with . which are known to be internal objects (such as
    .__S3MethodsTable__.).
  - Convenience function hasName() has been added; it is intended to replace
    the common idiom !is.null(x$name) without the usually unintended partial
    name matching.
  - strcapture() no longer fixes column names nor coerces strings to factors
    (suggested by Bill Dunlap).
  - strcapture() returns NA for non-matching values in x (suggested by Bill
    Dunlap).
  - source() gets new optional arguments, notably exprs; this is made use of in
    the new utility function withAutoprint().
  - sys.source() gets a new toplevel.env argument. This argument is useful for
    frameworks running package tests; contributed by Tomas Kalibera.
  - Sys.setFileTime() and file.copy(copy.date = TRUE) will set timestamps with
    fractions of seconds on platforms/filesystems which support this.
  - (Windows only.) file.info() now returns file timestamps including fractions
    of seconds; it has done so on other platforms since R 2.14.0. (NB: some
    filesystems do not record modification and access timestamps to sub-second
    resolution.)
  - The license check enabled by options(checkPackageLicense = TRUE) is now
    done when the package's namespace is first loaded.
  - ppr() and supsmu() get an optional trace argument, and ppr(.., sm.method =
    ..spline) is no longer limited to sample size n <= 2500.
  - The POSIXct method for print() gets optional tz and usetz arguments, thanks
    to a report from Jennifer S. Lyon.
  - New function check_packages_in_dir_details() in package tools for analyzing
    package-check log files to obtain check details.
  - Package tools now exports function CRAN_package_db() for obtaining
    information about current packages in the CRAN package repository, and
    several functions for obtaining the check status of these packages.
  - The (default) Stangle driver Rtangle allows annotate to be a function and
    gets a new drop.evalFALSE option.
  - The default method for quantile(x, prob) should now be monotone in prob,
    even in border cases, see PR#16672.
  - bug.report() now tries to extract an email address from a BugReports field,
    and if there is none, from a Contacts field.
  - The format() and print() methods for object.size() results get new options
    standard and digits; notably, standard = "IEC" and standard = "SI" allow
    more standard (but less common) abbreviations than the default ones, e.g. 
    for kilobytes. (From contributions by Henrik Bengtsson.)
  - If a reference class has a validity method, validObject will be called
    automatically from the default initialization method for reference classes.
  - tapply() gets new option default = NA allowing to change the previously
    hardcoded value.
  - read.dcf() now consistently interprets any ‘whitespace’ to be stripped to
    include newlines.
  - The maximum number of DLLs that can be loaded into R e.g. via dyn.load()
    can now be increased by setting the environment variable R_MAX_NUM_DLLS
    before starting R.
  - Assigning to an element of a vector beyond the current length now
    over-allocates by a small fraction. The new vector is marked internally as
    growable, and the true length of the new vector is stored in the truelength
    field. This makes building up a vector result by assigning to the next 
    element beyond the current length more efficient, though pre-allocating is 
    still preferred. The implementation is subject to change and not intended 
    to be used in packages at this time.
  - Loading the parallel package namespace no longer sets or changes the
    .Random.seed, even if R_PARALLEL_PORT is unset. NB: This can break
    reproducibility of output, and did for a CRAN package.
  - Methods "wget" and "curl" for download.file() now give an R error rather
    than a non-zero return value when the external command has a non-zero
    status.
  - Encoding name "utf8" is mapped to "UTF-8". Many implementations of iconv
    accept "utf8", but not GNU libiconv (including the late 2016 version 1.15).
  - sessionInfo() shows the full paths to the library or executable files
    providing the BLAS/LAPACK implementations currently in use (not available
    on Windows).
  - The binning algorithm used by bandwidth selectors bw.ucv(), bw.bcv() and
    bw.SJ() switches to a version linear in the input size n for n > nb/2. (The
    calculations are the same, but for larger n/nb it is worth doing the 
    binning in advance.)
  - There is a new option PCRE_study which controls when grep(perl = TRUE) and
    friends ‘study’ the compiled pattern. Previously this was done for 11 or
    more input strings: it now defaults to 10 or more (but most examples need 
    many more for the difference from studying to be noticeable).
  - grep(perl = TRUE) and friends can now make use of PCRE's Just-In-Time
    mechanism, for PCRE >= 8.20 on platforms where JIT is supported. It is used
    by default whenever the pattern is studied (see the previous item). (Based 
    on a patch from Mikko Korpela.)

    This is controlled by a new option PCRE_use_JIT.

    Note that in general this makes little difference to the speed, and may
    take a little longer: its benefits are most evident on strings of thousands 
    of characters. As a side effect it reduces the chances of C stack overflow 
    in the PCRE library on very long strings (millions of characters, but see 
    next item).

    Warning: segfaults were seen using PCRE with JIT enabled on 64-bit Sparc
    builds.
  - There is a new option PCRE_limit_recursion for grep(perl = TRUE) and
    friends to set a recursion limit taking into account R's estimate of the
    remaining C stack space (or 10000 if that is not available). This reduces 
    the chance of C stack overflow, but because it is conservative may report a
    non-match (with a warning) in examples that matched before. By default it is
    enabled if any input string has 1000 or more bytes. (PR#16757)
  - getGraphicsEvent() now works on X11(type = "cairo") devices. Thanks to
    Frederick Eaton (for reviving an earlier patch).
  - There is a new argument onIdle for getGraphicsEvent(), which allows an R
    function to be run whenever there are no pending graphics events. This is
    currently only supported on X11 devices. Thanks to Frederick Eaton.
  - The deriv() and similar functions now can compute derivatives of log1p(),
    sinpi() and similar one-argument functions, thanks to a contribution by
    Jerry Lewis.
  - median() gains a formal ... argument, so methods with extra arguments can
    be provided.
  - strwrap() reduces indent if it is more than half width rather than giving
    an error. (Suggested by Bill Dunlap.)
  - When the condition code in if(.) or while(.) is not of length one, an error
    instead of a warning may be triggered by setting an environment variable,
    see the help page.
  - Formatting and printing of bibliography entries (bibentry) is more flexible
    and better documented. Apart from setting options(citation.bibtex.max = 99)
    you can also use print(<citation>, bibtex=TRUE) (or format(..)) to get the
    BibTeX entries in the case of more than one entry. This also affects
    citation(). Contributions to enable style = "html+bibtex" are welcome.
- C-LEVEL FACILITIES
  - Entry points R_MakeExternalPtrFn and R_ExternalPtrFn are now declared in
    header ‘Rinternals.h’ to facilitate creating and retrieving an R external
    pointer from a C function pointer without ISO C warnings about the 
    conversion of function pointers.
  - There was an exception for the native Solaris C++ compiler to the dropping
    (in R 3.3.0) of legacy C++ headers from headers such as ‘R.h’ and ‘Rmath.h’
    — this has now been removed. That compiler has strict C++98 compliance hence
    does not include extensions in its (non-legacy) C++ headers: some packages 
    will need to request C++11 or replace non-C++98 calls such as lgamma: see 
    §1.6.4 of ‘Writing R Extensions’.

    Because it is needed by about 70 CRAN packages, headers ‘R.h’ and ‘Rmath.h’
    still declare

    use namespace std;

    when included on Solaris.
  - When included from C++, the R headers now use forms such as std::FILE
    directly rather than including the line

    using std::FILE;

    C++ code including these headers might be relying on the latter.
  - Headers ‘R_ext/BLAS.h’ and ‘R_ext/Lapack.h’ have many improved declarations
    including const for double-precision complex routines. Inter alia this
    avoids warnings when passing ‘string literal’ arguments from C++11 code.
  - Headers for Unix-only facilities ‘R_ext/GetX11Image.h’,
    ‘R_ext/QuartzDevice.h’ and ‘R_ext/eventloop.h’ are no longer installed on
    Windows.
  - No-longer-installed headers ‘GraphicsBase.h’, ‘RGraphics.h’,
    ‘Rmodules/RX11.h’ and ‘Rmodules/Rlapack.h’ which had a LGPL license no
    longer do so.
  - HAVE_UINTPTR_T is now defined where appropriate by Rconfig.h so that it can
    be included before Rinterface.h when CSTACK_DEFNS is defined and a C
    compiler (not C++) is in use. Rinterface.h now includes C header ‘stdint.h’
    or C++11 header ‘cstdint’ where needed.
  - Package tools has a new function
    package_native_routine_registration_skeleton() to assist adding
    native-symbol registration to a package. See its help and §5.4.1 of 
    ‘Writing R Extensions’ for how to use it. (At the time it was added it 
    successfully automated adding registration to over 90% of CRAN packages 
    which lacked it.  Many of the failures were newly-detected bugs in the 
    packages, e.g. 50 packages called entry points with varying numbers of 
    arguments and 65 packages called entry points not in the package.)
- INSTALLATION on a UNIX-ALIKE
  - readline headers (and not just the library) are required unless configuring
    with --with-readline=no.
  - configure now adds a compiler switch for C++11 code, even if the compiler
    supports C++11 by default. (This ensures that g++ 6.x uses C++11 mode and
    not its default mode of C++14 with ‘GNU extensions’.)
  - The tests for C++11 compliance are now much more comprehensive. For gcc <
    4.8, the tests from R 3.3.0 are used in order to maintain the same
    behaviour on Linux distributions with long-term support.
  - An alternative compiler for C++11 is now specified with CXX11, not CXX1X.
    Likewise C++11 flags are specified with CXX11FLAGS and the standard (e.g.,
    -std=gnu++11 is specified with CXX11STD.
  - configure now tests for a C++14-compliant compiler by testing some basic
    features. This by default tries flags for the compiler specified by CXX11,
    but an alternative compiler, options and standard can be specified by 
    variables CXX14, CXX14FLAGS and CXX14STD (e.g., -std=gnu++14).
  - There is a new macro CXXSTD to help specify the standard for C++ code, e.g.
    -std=c++98. This makes it easier to work with compilers which default to a
    later standard: for example, with CXX=g++6 CXXSTD=-std=c++98 configure will
    select commands for g++ 6.x which conform to C++11 and C++14 where specified
    but otherwise use C++98.
  - Support for the defunct IRIX and OSF/1 OSes and Alpha CPU has been removed.
  - configure checks that the compiler specified by $CXX $CXXFLAGS is able to
    compile C++ code.
  - configure checks for the required header ‘sys/select.h’ (or ‘sys/time.h’ on
    legacy systems) and system call select and aborts if they are not found.
  - If available, the POSIX 2008 system call utimensat will be used by
    Sys.setFileTime() and file.copy(copy.date = TRUE). This may result in
    slightly more accurate file times. (It is available on Linux and FreeBSD but
    not macOS.)
  - The minimum version requirement for libcurl has been reduced to 7.22.0,
    although at least 7.28.0 is preferred and earlier versions are little
    tested. (This is to support Debian 7 ‘Wheezy’ LTS and Ubuntu ‘Precise’ 12.04
    LTS, although the latter is close to end-of-life.)
  - configure tests for a C++17-compliant compiler. The tests are experimental
    and subject to change in the future.
- INCLUDED SOFTWARE
  - (Windows only) Tcl/Tk version 8.6.4 is now included in the binary builds.
    The ‘tcltk*.chm’ help file is no longer included; please consult the online
    help at http://www.tcl.tk/man/ instead.
  - The version of LAPACK included in the sources has been updated to 3.7.0: no
    new routines have been added to R.
- PACKAGE INSTALLATION
  - There is support for compiling C++14 or C++17 code in packages on suitable
    platforms: see ‘Writing R Extensions’ for how to request this.
  - The order of flags when LinkingTo other packages has been changed so their
    include directories come earlier, before those specified in CPPFLAGS. This
    will only have an effect if non-system include directories are included 
    with -I flags in CPPFLAGS (and so not the default -I/usr/local/include 
    which is treated as a system include directory on most platforms).
  - Packages which register native routines for .C or .Fortran need to be
    re-installed for this version (unless installed with R-devel SVN revision
    r72375 or later).
  - Make variables with names containing CXX1X are deprecated in favour of
    those using CXX11, but for the time being are still made available via file
    ‘etc/Makeconf’. Packages using them should be converted to the new forms and
    made dependent on R (>= 3.4.0).
- UTILITIES
  - Running R CMD check --as-cran with _R_CHECK_CRAN_INCOMING_REMOTE_ false now
    skips tests that require remote access. The remaining (local) tests
    typically run quickly compared to the remote tests.
  - R CMD build will now give priority to vignettes produced from files in the
    ‘vignettes’ directory over those in the ‘inst/doc’ directory, with a
    warning that the latter are being ignored.
  - R CMD config gains a --all option for printing names and values of all
    basic configure variables.
  - It now knows about all the variables used for the C++98, C++11 and C++14
    standards.
  - R CMD check now checks that output files in ‘inst/doc’ are newer than the
    source files in ‘vignettes’.
  - For consistency with other package subdirectories, files named ‘*.r’ in the
    ‘tests’ directory are now recognized as tests by R CMD check. (Wish of
    PR#17143.)
  - R CMD build and R CMD check now use the union of R_LIBS and .libPaths().
    They may not be equivalent, e.g., when the latter is determined by
    R_PROFILE.
  - R CMD build now preserves dates when it copies files in preparing the
    tarball. (Previously on Windows it changed the dates on all files; on Unix,
    it changed some dates when installing vignettes.)
  - The new option R CMD check --no-stop-on-test-error allows running the
    remaining tests (under ‘tests/’) even if one gave an error.
  - Check customization via environment variables to detect side effects of
    .Call() and .External() calls which alter their arguments is described in
    §8 of the ‘R Internals’ manual.
  - R CMD check now checks any BugReports field to be non-empty and a suitable
    single URL.
  - R CMD check --as-cran now NOTEs if the package does not register its native
    routines or does not declare its intentions on (native) symbol search.
    (This will become a WARNING in due course.)
- DEPRECATED AND DEFUNCT
  - (Windows only) Function setInternet2() is defunct.
  - Installation support for readline emulations based on editline (aka
    libedit) is deprecated.
  - Use of the C/C++ macro NO_C_HEADERS is defunct and silently ignored.
  - unix.time(), a traditional synonym for system.time(), has been deprecated.
  - structure(NULL, ..) is now deprecated as you cannot set attributes on NULL.
  - Header ‘Rconfig.h’ no longer defines SUPPORT_OPENMP; instead use _OPENMP
    (as documented for a long time).
  - (C-level Native routine registration.) The deprecated styles member of the
    R_CMethodDef and R_FortranMethodDef structures has been removed. Packages
    using these will need to be re-installed for R 3.4.0.
  - The deprecated support for PCRE versions older than 8.20 will be removed in
    R 3.4.1. (Versions 8.20–8.31 will still be accepted but remain deprecated.)
- BUG FIXES
  - Getting or setting body() or formals() on non-functions for now signals a
    warning and may become an error for setting.
  - match(x, t), duplicated(x) and unique(x) work as documented for complex
    numbers with NAs or NaNs, where all those containing NA do match, whereas
    in the case of NaN's both real and imaginary parts must match, compatibly 
    with how print() and format() work for complex numbers.
  - deparse(<complex>, options = "digits17") prints more nicely now, mostly
    thanks to a suggestion by Richie Cotton.
  - Rotated symbols in plotmath expressions are now positioned correctly on
    x11(type = "Xlib"). (PR#16948)
  - as<-() avoids an infinite loop when a virtual class is interposed between a
    subclass and an actual superclass.
  - Fix level propagation in unlist() when the list contains zero-length lists
    or factors.
  - Fix S3 dispatch on S4 objects when the methods package is not attached.
  - Internal S4 dispatch sets .Generic in the method frame for consistency with
    standardGeneric(). (PR#16929)
  - Fix order(x, decreasing = TRUE) when x is an integer vector containing
    MAX_INT. Ported from a fix Matt Dowle made to data.table.
  - Fix caching by callNextMethod(), resolves PR#16973 and PR#16974.
  - grouping() puts NAs last, to be consistent with the default behavior of
    order().
  - Point mass limit cases: qpois(-2, 0) now gives NaN with a warning and
    qgeom(1, 1) is 0. (PR#16972)
  - table() no longer drops an "NaN" factor level, and better obeys exclude =
    <chr>, thanks to Suharto Anggono's patch for PR#16936. Also, in the case of
    exclude = NULL and NAs, these are tabulated correctly (again).
  - Further, table(1:2, exclude = 1, useNA = "ifany") no longer erroneously
    reports <NA> counts.
  - Additionally, all cases of empty exclude are equivalent, and useNA is not
    overwritten when specified (as it was by exclude = NULL).
  - wilcox.test(x, conf.int=TRUE) no longer errors out in cases where the
    confidence interval is not available, such as for x = 0:2.
  - droplevels(f) now keeps <NA> levels when present.
  - In integer arithmetic, NULL is now treated as integer(0) whereas it was
    previously treated as double(0).
  - The radix sort considers NA_real_ and NaN to be equivalent in rank (like
    the other sort algorithms).
  - When index.return=TRUE is passed to sort.int(), the radix sort treats NAs
    like sort.list() does (like the other sort algorithms).
  - When in tabulate(bin, nbin) length(bin) is larger than the maximal integer,
    the result is now of type double and hence no longer silently overflows to
    wrong values. (PR#17140)
  - as.character.factor() respects S4 inheritance when checking the type of its
    argument. (PR#17141)
  - The factor method for print() no longer sets the class of the factor to
    NULL, which would violate a basic constraint of an S4 object.
  - formatC(x, flag = f) allows two new flags, and signals an error for invalid
    flags also in the case of character formatting.
  - Reading from file("stdin") now also closes the connection and hence no
    longer leaks memory when reading from a full pipe, thanks to Gábor Csárdi,
    see thread starting at
    https://stat.ethz.ch/pipermail/r-devel/2016-November/073360.html.
  - Failure to create file in tempdir() for compressed pdf() graphics device no
    longer errors (then later segfaults). There is now a warning instead of
    error and compression is turned off for the device. Thanks to Alec Wysoker
    (PR#17191).
  - Asking for methods() on "|" returns only S3 methods. See
    https://stat.ethz.ch/pipermail/r-devel/2016-December/073476.html.
  - dev.capture() using Quartz Cocoa device (macOS) returned invalid components
    if the back-end chose to use ARGB instead of RGBA image format. (Reported
    by Noam Ross.)
  - seq("2", "5") now works too, equivalently to "2":"5" and seq.int().
  - seq.int(to = 1, by = 1) is now correct, other cases are integer (instead of
    double) when seq() is integer too, and the "non-finite" error messages are
    consistent between seq.default() and seq.int(), no longer mentioning NaN 
    etc.
  - rep(x, times) and rep.int(x, times) now work when times is larger than the
    largest value representable in an integer vector. (PR#16932)
  - download.file(method = "libcurl") does not check for URL existence before
    attempting downloads; this is more robust to servers that do not support
    HEAD or range-based retrieval, but may create empty or incomplete files for
    aborted download requests.
  - Bandwidth selectors bw.ucv(), bw.bcv() and bw.SJ() now avoid integer
    overflow for large sample sizes.
  - str() no longer shows "list output truncated", in cases that list was not
    shown at all. Thanks to Neal Fultz (PR#17219)
  - Fix for cairo_pdf() (and svg() and cairo_ps()) when replaying a saved
    display list that contains a mix of grid and graphics output. (Report by
    Yihui Xie.)
  - The str() and as.hclust() methods for "dendrogram" now also work for deeply
    nested dendrograms thanks to non-recursive implementations by Bradley
    Broom.
  - sample() now uses two uniforms for added precision when the uniform
    generator is Knuth-TAOCP, Knuth-TAOCP-2002, or a user-defined generator and
    the population size is 2^25 or greater.
  - If a vignette in the ‘vignettes’ directory is listed in ‘.Rbuildignore’, R
    CMD build would not include it in the tarball, but would include it in the
    vignette database, leading to a check warning. (PR#17246)
  - tools::latexToUtf8() infinite looped on certain inputs. (PR#17138)
  - terms.formula() ignored argument names when determining whether two terms
    were identical. (PR#17235)
  - callNextMethod() was broken when called from a method that augments the
    formal arguments of a primitive generic.
  - Coercion of an S4 object to a vector during sub-assignment into a vector
    failed to dispatch through the as.vector() generic (often leading to a
    segfault).
  - Fix problems in command completion: Crash (PR#17222) and junk display in
    Windows, handling special characters in filenames on all systems.

* Mon Mar 13 2017 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 3.3.3-10
- NEW FEATURES
  - Changes when redirection of a http:// URL to a https:// URL is encountered:
    - The internal methods of download.file() and url() now report that they
      cannot follow this (rather than failing silently).
    - (Unix-alike) download.file(method = "auto") (the default) re-tries with
      method = "libcurl".
    - (Unix-alike) url(method = "default") with an explicit open argument
      re-tries with method = "libcurl". This covers many of the usages, e.g.
      readLines() with a URL argument.
- INSTALLATION on a UNIX-ALIKE
  - The configure check for the zlib version is now robust to versions longer
    than 5 characters, including 1.2.11.
- UTILITIES
  - Environmental variable _R_CHECK_TESTS_NLINES_ controls how R CMD check
    reports failing tests (see §8 of the ‘R Internals’ manual).
- DEPRECATED AND DEFUNCT
  - (C-level Native routine registration.) The undocumented styles field of the
    components of R_CMethodDef and R_FortranMethodDef is deprecated.
- BUG FIXES
  - vapply(x, *) now works with long vectors x. (PR#17174)
  - isS3method("is.na.data.frame") and similar are correct now. (PR#17171)
  - grepRaw(<long>, <short>, fixed = TRUE) now works, thanks to a patch by
    Mikko Korpela. (PR#17132)
  - Package installation into a library where the package exists via symbolic
    link now should work wherever Sys.readlink() works, resolving PR#16725.
  - "Cincinnati" was missing an "n" in the precip dataset.
  - Fix buffer overflow vulnerability in pdf() when loading an encoding file.
    Reported by Talos (TALOS-2016-0227).
  - getDLLRegisteredRoutines() now produces its warning correctly when multiple
    DLLs match, thanks to Matt Dowle's PR#17184.
  - Sys.timezone() now returns non-NA also on platforms such as Ubuntu 14.04.5
    LTS, thanks to Mikko Korpela's PR#17186.
  - format(x) for an illegal "POSIXlt" object x no longer segfaults.
  - methods(f) now also works for f "(" or "{".
  - (Windows only) dir.create() did not check the length of the path to create,
    and so could overflow a buffer and crash R. (PR#17206)
  - On some systems, very small hexadecimal numbers in hex notation would
    underflow to zero. (PR#17199)
  - pmin() and pmax() now work again for ordered factors and 0-length S3
    classed objects, thanks to Suharto Anggono's PR#17195 and PR#17200.
  - bug.report() did not do any validity checking on a package's BugReports
    field. It now ignores an empty field, removes leading whitespace and only
    attempts to open http:// and https:// URLs, falling back to emailing the
    maintainer.
  - Bandwidth selectors bw.ucv() and bw.SJ() gave incorrect answers or
    incorrectly reported an error (because of integer overflow) for inputs
    longer than 46341. Similarly for bw.bcv() at length 5793.
  - Another possible integer overflow is checked and may result in an error
    report (rather than an incorrect result) for much longer inputs (millions
    for a smooth distribution).
  - findMethod() failed if the active signature had expanded beyond what a
    particular package used. (Example with packages XR and XRJulia on CRAN.)
  - qbeta() underflowed too early in some very asymmetric cases. (PR#17178)
  - R CMD Rd2pdf had problems with packages with non-ASCII titles in ‘.Rd’
    files (usually the titles were omitted).

* Thu Nov 03 2016 Shane Sturrock <shane.sturrock@nzgenomics.co.nz> - 3.3.2-10
- NEW FEATURES:
  - extSoftVersion() now reports the version (if any) of the readline library
    in use.
  - The version of LAPACK included in the sources has been updated to 3.6.1, a
    bug-fix release including a speedup for the non-symmetric case of eigen().
  - Use options(deparse.max.lines=) to limit the number of lines recorded in
    .Traceback and other deparsing activities.
  - format(<AsIs>) looks more regular, also for non-character atomic matrices.
  - abbreviate() gains an option named = TRUE.
  - The online documentation for package methods is extensively rewritten.  The
    goals are to simplify documentation for basic use, to note old features not
    recommended and to correct out-of-date information.
  - Calls to setMethod() no longer print a message when creating a generic
    function in those cases where that is natural: S3 generics and primitives.
- INSTALLATION and INCLUDED SOFTWARE:
  - Versions of the readline library >= 6.3 had been changed so that terminal
    window resizes were not signalled to readline: code has been added using a
    explicit signal handler to work around that (when R is compiled against
    readline >= 6.3).  (PR#16604)
  - configure works better with Oracle Developer Studio 12.5.
- UTILITIES:
  - R CMD check reports more dubious flags in files src/Makevars[.in],
    including -w and -g.
  - R CMD check has been set up to filter important warnings from recent
    versions of gfortran with -Wall -pedantic: this now reports non-portable
    GNU extensions such as out-of-order declarations.
  - R CMD config works better with paths containing spaces, even those of home
    directories (as reported by Ken Beath).
- DEPRECATED AND DEFUNCT:
  - Use of the C/C++ macro NO_C_HEADERS is deprecated (no C headers are
    included by R headers from C++ as from R 3.3.0, so it should no longer be
    needed).
- BUG FIXES:
  - The check for non-portable flags in R CMD check could be stymied by
    src/Makevars files which contained targets.  (Windows only) When using
    certain desktop themes in Windows 7 or higher, Alt-Tab could cause Rterm to
    stop accepting input.  (PR#14406; patch submitted by Jan Gleixner.)
  - pretty(d, ..) behaves better for date-time d (PR#16923).
  - When an S4 class name matches multiple classes in the S4 cache, perform a
    dynamic search in order to obey namespace imports.  This should eliminate
    annoying messages about multiple hits in the class cache.  Also, pass along 
    the package from the ClassExtends object when looking up superclasses in 
    the cache.
  - sample(NA_real_) now works.
  - Packages using non-ASCII encodings in their code did not install data
    properly on systems using different encodings.
  - merge(df1, df2) now also works for data frames with column names "na.last",
    "decreasing", or "method".  (PR#17119)
  - contour() caused a segfault if the labels argument had length zero.
    (Reported by Bill Dunlap.)
  - unique(warnings()) works more correctly, thanks to a new
    duplicated.warnings() method.
  - findInterval(x, vec = numeric(), all.inside = TRUE) now returns 0s as
    documented.  (Reported by Bill Dunlap.)
  - (Windows only) R CMD SHLIB failed when a symbol in the resulting library
    had the same name as a keyword in the .def file.  (PR#17130)
  - pmax() and pmin() now work with (more ?)  classed objects, such as "Matrix"
    from the Matrix package, as documented for a long time.
  - axis(side, x = D) and hence Axis() and plot() now work correctly for "Date"
    and time objects D, even when “time goes backward”, e.g., with decreasing
    xlim.  (Reported by William May.)
  - str(I(matrix(..))) now looks as always intended.
  - plot.ts(), the plot() method for time series, now respects cex, lwd and
    lty.  (Reported by Greg Werbin.)
  - parallel::mccollect() now returns a named list (as documented) when called
    with wait = FALSE.  (Reported by Michel Lang.)
  - If a package added a class to a class union in another package, loading the
    first package gave erroneous warnings about “undefined subclass”.
  - c()'s argument use.names is documented now, as belonging to the (C
    internal) default method.  In “parallel”, argument recursive is also moved
    from the generic to the default method, such that the formal argument list 
    of base generic c() is just (...).  rbeta(4, NA) and similarly rgamma() and
    rnbinom() now return NaN's with a warning, as other r<dist>(), and as
    documented.  (PR#17155)
  - Using options(checkPackageLicense = TRUE) no longer requires acceptance of
    the licence for non-default standard packages such as compiler.  (Reported
    by Mikko Korpela.)
  - split(<very_long>, *) now works even when the split off parts are long.
    (PR#17139)
  - min() and max() now also work correctly when the argument list starts with
    character(0).  (PR#17160)
  - Subsetting very large matrices (prod(dim(.)) >= 2^31) now works thanks to
    Michael Schubmehl's PR#17158.
  - bartlett.test() used residual sums of squares instead of variances, when
    the argument was a list of lm objects.  (Reported by Jens Ledet Jensen).
  - plot(<lm>, which = *) now correctly labels the contour lines for the
    standardized residuals for which = 6.  It also takes the correct p in case
    of singularities (also for which = 5).  (PR#17161)
  - xtabs(~ exclude) no longer fails from wrong scope, thanks to Suharto
    Anggono's PR#17147.
  - Reference class calls to methods() did not re-analyse previously defined
    methods, meaning that calls to methods defined later would fail. (Reported
    by Charles Tilford).
  - findInterval(x, vec, left.open = TRUE) misbehaved in some cases.  (Reported
    by Dmitriy Chernykh.)

* Wed Sep 07 2016 Shane Sturrock <shane@biomatters.com> - 3.3.1-11
- Fixed an issue where a fresh install wouldn't get R 3.2.5 set.

* Mon Jul 11 2016 Shane Sturrock <shane@biomatters.com> - 3.3.1-10
- BUG FIXES:
  - R CMD INSTALL and hence install.packages() gave an internal error
    installing a package called description from a tarball on a
    case-insensitive file system.
  - match(x, t) (and hence x %in% t) failed when x was of length one, and
    either character and x and t only differed in their Encoding or when x and
    t where complex with NAs or NaNs.  (PR#16885.)
  - unloadNamespace(ns) also works again when ns is a 'namespace', as from
    getNamespace().
  - rgamma(1,Inf) or rgamma(1, 0,0) no longer give NaN but the correct limit.
  - length(baseenv()) is correct now.
  - pretty(d, ..) for date-time d rarely failed when "halfmonth" time steps
    were tried (PR#16923) and on 'inaccurate' platforms such as 32-bit windows
    or a configuration with --disable-long-double; see comment #15 of PR#16761.
  - In text.default(x, y, labels), the rarely(?) used default for labels is now
    correct also for the case of a 2-column matrix x and missing y.
  - as.factor(c(a = 1L)) preserves names() again as in R < 3.1.0.
  - strtrim(""[0], 0[0]) now works.
  - Use of Ctrl-C to terminate a reverse incremental search started by Ctrl-R
    in the readline-based Unix terminal interface is now supported for readline
    >= 6.3 (Ctrl-G always worked).  (PR#16603)
  - diff(<difftime>) now keeps the "units" attribute, as subtraction already
    did, PR#16940.

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
