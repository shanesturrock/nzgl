Name:           perl-bioperl
Version:        1.6.901
Release:        1%{?dist}
Summary:        Perl tools for computational molecular biology

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://www.bioperl.org/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CJ/CJFIELDS/BioPerl-%{version}.tar.gz
Patch0:         bioperl-1.6.901-paths.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Ace)
BuildRequires:  perl(Class::AutoClass) >= 1
BuildRequires:  perl(Clone)
BuildRequires:  perl(Convert::Binary::C)
BuildRequires:  perl(Data::Stag::XMLWriter)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(GD) >= 1.3
BuildRequires:  perl(GD::SVG)
BuildRequires:  perl(Graph)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Stringy)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(PostScript::TextBlock)
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(Spreadsheet::ParseExcel)
BuildRequires:  perl(Storable)
BuildRequires:  perl(SVG) >= 2.26
BuildRequires:  perl(SVG::Graph) >= 0.01
BuildRequires:  perl(Text::Shellwords)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::DOM::XPath) >= 0.13
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Parser::PerlSAX)
BuildRequires:  perl(XML::SAX) >= 0.14
BuildRequires:  perl(XML::SAX::Writer)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(XML::Writer) > 0.4
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Array::Compare)
BuildRequires:  perl(GraphViz)
# disable the following BRs until they are packaged for Fedora
#BuildRequires: perl(Math::Random)
#BuildRequires: perl(Algorithm::Munkres)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Packages perl-bioperl and perl-bioperl-run require each other.  To break
# this circular edependency (e.g., for bootstrapping), filter out all
# Bio::Tools::Run::* module requirements; they are either self-satisfied
# (and thus redundant) or they bring dependency on perl-bioperl-run.
## be careful when commenting this out: macros are expanded even in comments
#%%filter_from_requires /perl(Bio::Tools::Run::/d
#%%?perl_default_filter

%description
BioPerl is a toolkit of Perl modules useful in building bioinformatics
solutions in Perl. It is built in an object-oriented manner so that
many modules depend on each other to achieve a task.


%{?filter_setup:
%filter_from_requires /perl(Bio::Expression.*)/d
%{?perl_default_filter}
}

%prep
%setup -q -n BioPerl-%{version}
%patch0 -p1

# temporarily remove PhyloNetwork before compiling until upstream says
# they are ready for primetime and deps Math::Random and
# Algorithm::Munkres are also packaged
rm -r Bio/PhyloNetwork*
rm -r t/Tree/PhyloNetwork

# remove all execute bits from the doc stuff
find examples -type f -exec chmod -x {} ';'

%build
%{__perl} Build.PL --installdirs vendor << EOF
n
a
n
EOF

./Build

# make sure the man page is UTF-8...
cd blib/libdoc
for i in Bio::Tools::GuessSeqFormat.3pm Bio::Tools::Geneid.3pm; do
    iconv --from=ISO-8859-1 --to=UTF-8 $i > new
    mv new $i
done


%install
rm -rf $RPM_BUILD_ROOT
#make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
perl Build pure_install --destdir=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -a \( -name .packlist \
  -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
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
## don't distribute "doc" subdirectory,  doesn't contain docs
%doc examples models
%doc AUTHORS BUGS Changes DEPRECATED INSTALL LICENSE README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
* Tue Feb 15 2011 Marcela Maslanova <mmaslano@redhat.com> - 1.6.1-7
- fix filter for RPM4.9
