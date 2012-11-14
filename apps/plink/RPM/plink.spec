Name:		plink
Version:	1.07
Release:	1%{?dist}
Summary:	Whole genome association analysis toolset
Group:		Applications/Engineering
License:	GPLv2
URL:		http://pngu.mgh.harvard.edu/~purcell/plink/index.shtml
Source0:	http://pngu.mgh.harvard.edu/~purcell/plink/dist/plink-%{version}-src.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	zlib-devel
%define __jar_repack 0

%description
PLINK is a free, open-source whole genome association analysis toolset, 
designed to perform a range of basic, large-scale analyses in a computationally 
efficient manner.

%prep
%setup -q -n %{name}-%{version}-src

%build
sed -i 's/FORCE_DYNAMIC =/FORCE_DYNAMIC = 1/g' Makefile
sed -i 's/WITH_WEBCHECK = 1/WITH_WEBCHECK = 0/g' Makefile
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_javadir}/%{name}
mkdir -p %{buildroot}/%{_bindir}
install -m 0644 gPLINK.jar %{buildroot}/%{_javadir}/%{name}/gPLINK.jar
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING.txt README.txt
%{_bindir}/%{name}
/usr/share/java/plink/gPLINK.jar

%changelog
* Tue Sep 25 2012 Carl Jones <carl@biomatters.com> - 1.07-1
- Initial release.
