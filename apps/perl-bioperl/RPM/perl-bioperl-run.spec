Name:           perl-bioperl-run
Version:        1.6.900
Release:        1%{?dist}
Summary:        Modules to provide a Perl interface to various bioinformatics applications

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://bioperl.org
Source0:        http://search.cpan.org/CPAN/authors/id/C/CJ/CJFIELDS/BioPerl-Run-%{version}.tar.gz
Patch0:         bioperl-run-1.006900-paths.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
# BuildRequires:  perl(Bio::Root::Version) >= 1.5.9
BuildRequires:  perl(Algorithm::Diff) >= 1
BuildRequires:  perl(XML::Parser::PerlSAX)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(Module::Build)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Bioperl-run contain modules that provide a Perl interface to various
bioinformatics applications. This allows various applications to be
used with common Bioperl objects.

%{?filter_setup:
%filter_from_requires /perl(Bio::Tools::Run::WrapperBase::CommandExts)/d
%filter_from_requires /perl(Bio::Tools::Run::StandAloneBlastPlus::BlastMethods)/d
%{?perl_default_filter}
}

%prep
# note that archive and tarball version numbers don't quite match in this release
%setup -q -n BioPerl-Run-1.006900
%patch0 -p1

# remove all execute bits from the doc stuff
chmod -x INSTALL INSTALL.PROGRAMS

%build
%{__perl} Build.PL --installdirs vendor << EOF
y
n
EOF

./Build

%install
rm -rf $RPM_BUILD_ROOT
perl Build pure_install --destdir=$RPM_BUILD_ROOT

# remove some spurious files
find $RPM_BUILD_ROOT -type f -a \( -name .packlist \
  -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'
# remove errant execute bit from the .pm's
find $RPM_BUILD_ROOT -type f -name '*.pm' -exec chmod -x {} 2>/dev/null ';'
# correct all binaries in /usr/bin to be 0755
find $RPM_BUILD_ROOT/%{_bindir} -type f -name '*.pl' -exec chmod 0755 {} 2>/dev/null ';'

%check
%{?_with_check:./Build test || :}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
## don't distribute "doc" "scripts" subdirectories, they don't contain docs
%doc AUTHORS Changes INSTALL INSTALL.PROGRAMS README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
