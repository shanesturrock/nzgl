Name:		libgtextutils
Version:	0.6.1
Release:	2%{?dist}
Summary:	Assaf Gordon text utilities    

Group:		System Environment/Libraries
License:	AGPLv3+
URL:		http://hannonlab.cshl.edu/fastx_toolkit/
Source0:	http://hannonlab.cshl.edu/fastx_toolkit/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides:	libgtextutils-0.6.so.0()(64bit)


%description
Text utilities library used by the fastx_toolkit, from the Hannon Lab

%package       devel
Summary:       Development files for %{name}
Group:	       Development/Libraries
Requires:      %{name} = %{version}-%{release}
Requires:      pkgconfig

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
#fix for unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'
cd %{buildroot}/%{_libdir} && ln -sf libgtextutils-0.6.1.so.0.0.0 libgtextutils-0.6.so.0

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README THANKS NEWS
%{_libdir}/libgtextutils-*.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/gtextutils
%{_libdir}/libgtextutils*.so
%{_libdir}/pkgconfig/gtextutils.pc

%changelog
* Fri Jul 27 2012 Carl Jones <carl@biomatters.com> - 0.6.1-2
- Add libgtextutils-0.6.so.0 symlink

* Fri Jul 27 2012 Carl Jones <carl@biomatters.com> - 0.6.1-1
- Upgrade to 0.6.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-7
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 14 2010 Adam Huffman <bloch@verdurin.com> - 0.6-4
- fix formatting and change license to AGPLv3+

* Wed Aug 25 2010 Adam Huffman <bloch@verdurin.com> - 0.6-3
- fix CXXFLAGS too
- use macros consistently
- fix files locations

* Thu Jun 24 2010 Adam Huffman <bloch@verdurin.com> - 0.6-2
- remove unnecessary BR
- fix CFLAGS

* Tue May 11 2010 Adam Huffman <bloch@verdurin.com> - 0.6-1
- initial version

