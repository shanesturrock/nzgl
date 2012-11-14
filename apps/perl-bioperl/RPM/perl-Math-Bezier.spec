# $Id: perl-Math-Bezier.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Andy Wardley <cpan$wardley,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Bezier

Summary: Solution of Bezier Curves
Name: perl-Math-Bezier
Version: 0.01
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Bezier/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/modules/by-module/Math/Math-Bezier-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements the algorithm for the solution of Bezier
curves as presented by Robert D. Miller in Graphics Gems V,
"Quick and Simple Bezier Curve Drawing".

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Math/
%{perl_vendorlib}/Math/Bezier.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2 - 7981/dag
- Rebuild for Fedora Core 5.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
