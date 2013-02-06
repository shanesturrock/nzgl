Name:		circos
Version:	0.63
Release:	1%{?dist}
Summary:	Circos is a software package for visualizing data and information.
Group:		Applications/Engineering
License:	GPL
URL:		http://circos.ca/
Source0:	http://circos.ca/distribution/circos-%{version}.tgz
Source1:	circos.sh

%description
Circos is a software package for visualizing data and information. It visualizes 
data in a circular layout — this makes Circos ideal for exploring relationships 
between objects or positions. Circos is ideal for creating publication-quality 
infographics  and illustrations with a high data-to-ink ratio, richly layered 
data and pleasant symmetries. 

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/opt/circos
mkdir -p %{buildroot}/etc/profile.d
/bin/cp %{SOURCE1} %{buildroot}/etc/profile.d/
/bin/cp -r bin/ data/ error/ etc/ example/ fonts/ lib/ tiles/ %{buildroot}/opt/circos/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README 
/opt/*
/etc/profile.d/circos.sh

%changelog

* Thu Feb 07 2013 Carl Jones <carl@biomatters.com> - 0.63-1
- New upstream release

* Wed Sep 19 2012 Carl Jones <carl@biomatters.com> - 0.62.1-1
- Fix version number
* Thu Jul 25 2012 Carl Jones <carl@biomatters.com> - 0.6.2.1-1
- Initial build.
