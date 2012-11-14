Name:		macs
Version:	1.4.2
Release:	1%{?dist}
Summary:	Model-based Analysis for ChIP-Seq	
Group:		Applications/Engineering
License:	Artistic License
URL:		http://liulab.dfci.harvard.edu/MACS/
Source0:	https://github.com/downloads/taoliu/MACS/MACS-%{version}-1.tar.gz
BuildRequires:	python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
To address the lack of powerful ChIP-Seq analysis method, 
we present a novel algorithm, named Model-based Analysis of ChIP-Seq (MACS), 
for identifying transcript factor binding sites.

%prep
%setup -q -n MACS-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_prefix}
python setup.py install --prefix=%{buildroot}/%{_prefix}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README
/usr/lib/python2.6/site-packages/MACS14/*
/usr/lib/python2.6/site-packages/MACS-%{version}-py2.6.egg-info
%{_bindir}/elandexport2bed
%{_bindir}/elandmulti2bed
%{_bindir}/elandresult2bed
%{_bindir}/macs14
%{_bindir}/sam2bed
%{_bindir}/wignorm

%changelog
* Mon Sep 24 2012 Carl Jones <carl@biomatters.com> - 1.4.2-1
- Initial build.
