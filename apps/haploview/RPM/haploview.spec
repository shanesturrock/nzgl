Name:		haploview
Version:	4.1
Release:	1%{?dist}
Summary:	HaploView is a Java based tool for use by biologists in the study of genetic haplotype data
Group:		Applications/Engineering
License:	MIT
URL:		http://sourceforge.net/projects/haploview/
Source0:	http://downloads.sourceforge.net/project/haploview/haploview-source/4.1/Haploview%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	ant
%define __jar_repack 0

%description
Haploview is designed to simplify and expedite the process of haplotype 
analysis by providing a common interface to several tasks relating to such analyses. 

%prep
%setup -q -n Haploview%{version}

%build
ant %{name}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_javadir}/%{name}
install -m 0644 Haploview.jar %{buildroot}/%{_javadir}/%{name}/%{name}.jar

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/haploview/haploview.jar

%changelog
* Mon Sep 24 2012 Carl Jones <carl@biomatters.com> - 4.1-1
- Initial release.
