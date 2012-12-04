Name:		seqmonk
Version:	0.23.0
Release:	1%{?dist}
Summary:	A tool to visualise and analyse high throughput mapped sequence data
Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.bioinformatics.babraham.ac.uk/projects/seqmonk/
Source0:	http://www.bioinformatics.babraham.ac.uk/projects/seqmonk/seqmonk_v%{version}.zip
Patch0:		seqmonk-classpath.patch
Requires:	java-1.6.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
SeqMonk is a program to enable the visualisation and analysis of mapped sequence data. It was written 
for use with mapped next generation sequence data but can in theory be used for any dataset which can 
be expressed as a series of genomic positions.

%prep
%setup -q -n SeqMonk
%patch0 -p0

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 seqmonk %{buildroot}/%{_bindir}
/bin/cp -r uk/ %{buildroot}/%{_javadir}/%{name}/
/bin/cp -r com/ %{buildroot}/%{_javadir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt LICENSE.txt RELEASE_NOTES.txt
/usr/bin/seqmonk
/usr/share/java/seqmonk/*

%changelog
* Wed Dec 05 2012 Carl Jones <carl@biomatters.com> - 0.23.0-1
- New upstream release
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 0.22.0-2
- Use 0.22 tarball rather than 0.21
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> - 0.22.0-1
- New upstream release
* Fri Aug 09 2012 Carl Jones <carl@biomatters.com> - 0.21.0-3
- Fixed Java paths
* Fri Aug 02 2012 Carl Jones <carl@biomatters.com> - 0.21.0-2
- Move bin/seqmonk to seqmonk.
* Fri Aug 02 2012 Carl Jones <carl@biomatters.com> - 0.21.0-1
- Initial build.
