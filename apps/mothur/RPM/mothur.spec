Name:		mothur
Version:	1.32.1
Release:	1%{?dist}
Summary:	Computational microbial ecology tool
Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.mothur.org/w/images/b/bc/Mothur.1.32.1.zip
Source0:	Mothur.%{version}.zip
patch0:		makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	readline-devel ncurses-devel gcc-gfortran glibc-static

%description
The mothur project was initiated by Dr. Patrick Schloss and his
software development team in the Department of Microbiology &
Immunology at The University of Michigan. This project seeks to
develop a single piece of open-source, expandable software to fill the
bioinformatics needs of the microbial ecology community. The authors
have incorporated the functionality of dotur, sons, treeclimber,
s-libshuff, unifrac, and much more. In addition to improving the
flexibility of these algorithms, they have added a number of other
features including calculators and visualization tools.

%prep
#Deal with mistakenly included OS X files
%setup -q   -n Mothur.source
rm -rf __MACOSX* .DS_Store
%patch0 -p0

%build
#makefile doesn't support SMP builds
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/%{name}

%changelog
* Thu Oct 17 2013 Shane Sturrock <shane@biomatters.com> - 1.32.1-1
- Upstream update, no details of why.
* Thu Oct 03 2013 Shane Sturrock <shane@biomatters.com> - 1.32.0-1
- Upstream update - see http://www.mothur.org/wiki/Mothur_v.1.32.0
* Thu Sep 05 2013 Shane Sturrock <shane@biomatters.com> - 1.31.2-1
- Initial build.
