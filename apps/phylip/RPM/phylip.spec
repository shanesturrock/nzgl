# ----------------------------------------------------------------------------
#
#  PHYLIP
#
# ----------------------------------------------------------------------------

Name:      phylip
Version:   3.696
Release:   1%{?dist}
Summary:   Phylogeny Inference Package
Group:     Applications/BioInformatics
License:   Copyright University of Washington and Joseph Felsenstein
URL:       http://evolution.genetics.washington.edu/phylip.html
Source0:   http://evolution.gs.washington.edu/phylip/download/phylip-%{version}.tar.gz
#Source0:   ftp://evolution.genetics.washington.edu/pub/phylip/phylip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# BuildRoot: /var/tmp/%{name}-buildroot
BuildRequires: xorg-x11-server-devel libXt-devel libXaw-devel libX11-devel

%description
PHYLIP (the PHYLogeny Inference Package) is a package of programs for
inferring phylogenies (evolutionary trees). Methods that are available
in the package include parsimony, distance matrix, and likelihood methods,
including bootstrapping and consensus trees.
Data types that can be handled include molecular sequences, gene frequencies,
restriction sites, distance matrices, and 0/1 discrete characters.

Reference for PHYLIP:
Felsenstein, J. 1989.
PHYLIP - Phylogeny Inference Package (Version 3.2).
Cladistics 5: 164-166.

# ----------------------------------------------------------------------------

%prep
%setup -q

%build
cd src
make -f Makefile.unx all

%install
rm -rf %{buildroot}
cd src 
mkdir -p %{buildroot}/%{_bindir}/phylip
mkdir -p %{buildroot}/%{_datadir}/phylip
make -f Makefile.unx EXEDIR=%{buildroot}/%{_bindir}/phylip DATADIR=%{buildroot}/%{_datadir}/phylip install


%clean
rm -rf %{buildroot}

# ----------------------------------------------------------------------------

%files
%defattr(-,root,root)
%{_bindir}/phylip
%doc doc/*


%changelog
* Mon Sep 22 2014 Shane Sturrock <shane@biomatters.com> - 3.696-1
- New upstream release 

* Tue Jun 04 2013 Simon Buxton <simon@biomatters.com> - 3.695-1
- New upstream release 

* Fri May 17 2013 Shane Sturrock <shane@biomatters.com> - 3.69-1
- Imported into NZGL project

* Mon Oct 3 2005 gotero <gotero@linuxprophet.com>
-edited for phylip 3.65

* Thu Dec 30 2004 gotero <gotero@linuxprophet.com>
-edited for BioBrew

* Tue Aug 03 2004 Luc Ducazu <luc@biolinux.org>
- Build for phylip 3.61

* Tue Jul 20 2004 Luc Ducazu <luc@biolinux.org>
- Build for phylip 3.6

* Tue Apr 06 2004 Luc Ducazu <luc@biolinux.org>
- Build for phylip 3.6b
- Fonts moved to datadir

* Wed Dec 18 2002 Luc Ducazu <luc@biolinux.org>
- Program factor in /usr/bin conflicts with sh-utils, moved to /usr/local/bin

* Wed Dec 11 2002 Luc Ducazu <luc@biolinux.org>
- Initial build
