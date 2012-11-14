Name:		bfast
Version:	0.7.0a
Release:	1%{?dist}
Summary:	Blat-like Fast Accurate Search Tool
Group:		Applications/Engineering
License:	GPLv2
URL:		http://bfast.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/bfast/bfast/0.7.0/bfast-0.7.0a.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRequires:	automake

%description
BFAST facilitates the fast and accurate mapping of short reads to reference sequences. Some advantages of BFAST include:
Speed: enables billions of short reads to be mapped quickly.
Accuracy: A priori probabilities for mapping reads with defined set of variants.
An easy way to measurably tune accuracy at the expense of speed.

%prep
%setup -q

%build
sh autogen.sh
./configure --prefix=/usr
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
/usr/share/doc/bfast/*

%changelog
* Mon Sep 24 2012 Carl Jones <carl@biomatters.com> - 1.02.00-1
- Initial release.
