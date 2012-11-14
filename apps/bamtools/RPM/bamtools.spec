Name:		bamtools
Version:	1.0.2
Release:	2%{?dist}
Summary:	Tools for handing BAM files
Group:		Applications/Engineering
License:	MIT
URL:		https://github.com/pezmaster31/bamtools
Source0:	https://github.com/downloads/pezmaster31/bamtools/bamtools-1.0.2.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	cmake
BuildRequires:	zlib-devel

%description
BamTools provides both a programmer's API and an end-user's toolkit for handling
BAM files.

%prep
%setup -q

%build
mkdir build
cd build
cmake ..
make
cd ..

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -m 0755 bin/bamtools-%{version} %{buildroot}%{_bindir}/bamtools
/bin/cp -a lib/* %{buildroot}%{_libdir}
/bin/cp -a include/* %{buildroot}%{_includedir}
cd %{buildroot}%{_libdir}
ln -sf libbamtools.so.1.0.2 libbamtools.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README
%{_bindir}/bamtools
%{_libdir}/*
%{_includedir}/*

%changelog
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> 1.0.2-2
- Fix libbamtools.so symlink
* Thu Sep 20 2012 Carl Jones <carl@biomatters.com> 1.0.2-1
- Initial build.
