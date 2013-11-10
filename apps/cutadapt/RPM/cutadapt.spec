Name:		cutadapt
Version:	1.3
Release:	1%{?dist}
Summary:	A tool that removes adapter sequences from DNA sequencing reads
Group:		Applications/Engineering
License:	MIT License
URL:		http://code.google.com/p/cutadapt/
Source0:	http://cutadapt.googlecode.com/files/cutadapt-%{version}.tar.gz
BuildRequires:	python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
cutadapt removes adapter sequences from high-throughput sequencing data. This is usually 
necessary when the read length of the sequencing machine is longer than the molecule 
that is sequenced, for example when sequencing microRNAs.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_prefix}
python setup.py install --prefix=%{buildroot}/%{_prefix}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/cutadapt
%{_libdir}/python2.6/site-packages/cutadapt/*
%{_libdir}/python2.6/site-packages/cutadapt-%{version}-py2.6.egg-info

%changelog

* Mon Nov 11 2013 Shane Sturrock <shane@biomatters.com> - 1.3-1
- Preliminary paired-end support with the --paired-output option (contributed by
  James Casbon). See the README section on how to use it.
- Improved statistics.
- Fix incorrectly reported amount of quality-trimmed Mbp (issue 57, fix by 
  Chris Penkett)
- Add the `--too-long-output` option.
- Add the `--no-trim` option, contributed by Dave Lawrence.
- Port handwritten C alignment module to Cython.
- Fix the `--rest-file` option (issue 56)
- Slightly speed up alignment of 5' adapters.
- Support bzip2-compressed files.
* Mon Dec 03 2012 Carl Jones <carl@biomatters.com> - 1.2.1-1
- New upstream release
* Fri Jul 27 2012 Carl Jones <carl@biomatters.com> - 1.1-2
- Add BuildRoot
- Add BuildRequires
* Fri Jul 27 2012 Carl Jones <carl@biomatters.com> - 1.1-1
- Initial build.
