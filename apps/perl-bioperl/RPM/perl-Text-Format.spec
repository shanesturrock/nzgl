Name:           perl-Text-Format
Version:        0.52
Release:        4%{?dist}
Summary:        Various subroutines to format text

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan/.org/dist/Text-Format/
Source0:        http://search.cpan.org/CPAN/authors/id/G/GA/GABOR/Text-Format%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch 
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
The format routine will format under all circumstances even if the width isn't
enough to contain the longest words. Text::Wrap will die under these
circumstances, although I am told this is fixed. If columns is set to a small
number and words are longer than that and the leading 'whitespace' than there
will be a single word on each line. This will let you make a simple word list
which could be indented or right aligned. There is a chance for croaking if you
try to subvert the module. If you don't pass in text then the internal text is
worked on, though not modified. Text::Format is meant for more powerful text
formatting than Text::Wrap allows.


%prep
%setup -q -n Text-Format%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.52-2
Rebuild for new perl

* Fri Feb 01 2008 Xavier Bachelot <xavier@bachelot.org> - 0.52-1
- Initial build.
