Name:		matrix2png
Version:	1.2.2
Release:	1%{?dist}
Summary:	A program for making visualizations of microarray data and other data types.
Group:		Applications/Engineering
License:	Apache
URL:		http://www.chibi.ubc.ca/matrix2png/
BuildRequires:	zlib-devel gd-devel libpng-devel
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Matrix2png is a simple but powerful program for making visualizations of 
microarray data and many other data types. It generates PNG formatted images 
from text files of data. It is fast, easy to use, and reasonably flexible. 
It can be used to generate publication-quality images, or to act as a image 
generator for web applications.

%prep
%setup -q

%build
./configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 matrix2png %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README AUTHORS
%{_bindir}/matrix2png

%changelog

* Thu Aug 2 2012 Carl Jones <carl@biomatters.com> - 1.2.2-1
- Initial build.
