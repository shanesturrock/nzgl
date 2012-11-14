Name:		srma
Version:	0.1.15
Release:	1%{?dist}
Summary:	Short Read Micro re-Aligner
Group:		Applications/Engineering
License:	GPL
URL:		http://sourceforge.net/projects/srma/
Source0:	http://downloads.sourceforge.net/project/srma/srma/0.1/srma-0.1.15.jar
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
SRMA aims to perform a re-alignment of each read to a graphical representation of 
all alignments within a local region to provide a better overall base-resolution consensus.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_javadir}/%{name}
install -m 0644 %{SOURCE0} %{buildroot}/%{_javadir}/%{name}/%{name}.jar

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/srma/srma.jar

%changelog
* Mon Sep 24 2012 Carl Jones <carl@biomatters.com> - 0.1.15-1
- Initial release.
