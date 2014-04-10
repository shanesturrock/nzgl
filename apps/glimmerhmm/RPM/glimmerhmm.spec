Name:		glimmerhmm
Version:	3.0.2
Release:	3%{?dist}
Summary:	GlimmerHMM is a new gene finder based on a Generalized Hidden Markov Model (GHMM).
Group:		Applications/Engineering
License:	Artistic clarified
URL:		http://www.cbcb.umd.edu/software/GlimmerHMM/
Source0:	ftp://ftp.cbcb.umd.edu/pub/software/glimmerhmm/GlimmerHMM-%{version}.tar.gz
Patch1:		trainGlimmerHMM.patch
Patch2:		score.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv:	no

%description
GlimmerHMM is a new gene finder based on a Generalized Hidden Markov Model (GHMM). Although 
the gene finder conforms to the overall mathematical framework of a GHMM, additionally it 
incorporates splice site models adapted from the GeneSplicer program and a decision 
tree adapted from GlimmerM. It also utilizes Interpolated Markov Models for the 
coding and noncoding models . Currently, GlimmerHMM's GHMM structure includes introns 
of each phase, intergenic regions, and four types of exons (initial, internal, final, 
and single)

%prep
%setup -q -n GlimmerHMM
%patch1 -p0
%patch2 -p0

%clean
rm -rf %{buildroot}

%build
cd train && /bin/rm -f build-icm build-icm-noframe build1 build2 falsecomp \
  findsites karlin score score2 scoreATG scoreATG2 scoreSTOP scoreSTOP2 \
  erfapp splicescore && cd ..
make -C sources %{?_smp_mflags} CXXFLAGS="$RPM_OPT_FLAGS"
make -C train %{?_smp_mflags} CXXFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
mkdir -p %{buildroot}/%{perl_vendorarch}

install -m 0755 sources/glimmerhmm %{buildroot}/%{_bindir}
install -m 0755 bin/glimmhmm.pl %{buildroot}/%{_bindir}
install -m 0755 train/trainGlimmerHMM %{buildroot}/%{_bindir}

cd train && /bin/cp build-icm build-icm-noframe build1 build2 falsecomp \
  findsites karlin score score2 scoreATG scoreATG2 scoreSTOP scoreSTOP2 \
  erfapp splicescore %{buildroot}/%{_libexecdir}/%{name} && cd .. 
cd train && /bin/cp *.pm mkdir -p %{buildroot}/%{perl_vendorarch} && cd ..

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/*
%{_libexecdir}/%{name}/*
%{perl_vendorarch}/*.pm

%changelog
* Wed Apr 10 2014 Shane Sturrock <shane@biomatters.com> - 3.0.2-3
- Moving into stable
* Tue Apr 23 2013 Shane Sturrock <shane@biomatters.com> - 3.0.2-1
* Wed Apr 24 2013 Shane Sturrock <shane@biomatters.com> - 3.0.2-2
- Patching to fix score.c
* Tue Apr 23 2013 Shane Sturrock <shane@biomatters.com> - 3.0.2-1
- New upstream release
* Tue Apr 23 2013 Shane Sturrock <shane@biomatters.com> - 3.0.1-4
- Correcting build problems with previous version
- New usptream release
- Correct version numbering (3.01 -> 3.0.1)
* Wed Sep 05 2012 Carl Jones <carl@biomatters.com> - 3.0.1-2
- Include Perl modules
- Patch trainGlimmerHMM perl script
