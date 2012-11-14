Name:		clustalw
Version:	2.1
Release:	1%{?dist}
Summary:	Clustal W is a general purpose multiple alignment program for DNA or proteins
Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.clustal.org/clustal2/
Source0:	ftp://ftp.ebi.ac.uk/pub/software/clustalw2/2.1/clustalw-2.1.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Clustal is a widely used multiple sequence alignment computer program.
ClustalW is the command line version.

%prep
%setup -q

%build
./configure
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/clustalw2 %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README clustalw_help
%{_bindir}/clustalw2

%changelog
* Mon Sep 24 2012 Carl Jones <carl@biomatters.com> - 2.1-1
- Initial release.
