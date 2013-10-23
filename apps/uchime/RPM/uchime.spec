Name:		uchime
Version:	4.2.40
Release:	1%{?dist}
Summary:	Computational microbial ecology tool
Group:		Applications/Engineering
License:	GPLv3
URL:		http://http://drive5.com/uchime/uchime_download.html
Source0:	%{name}%{version}_src.tar.gz
BuildRoot:	%{_tmppath}/%{name}%{version}_src-%{release}-root-%(%{__id_u} -n)
BuildRequires:	glibc-static

%description
UCHIME is an algorithm for detecting chimeric sequences. It is implemented in the uchime_ref and uchime_denovo commands. See UCHIME in practice for a detailed discussion of the assumptions and limitations of the method.

%prep
%setup -q -n %{name}%{version}_src

%build
make 

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Wed Oct 23 2013 Shane Sturrock <shane@biomatters.com> - 4.2.40-1
- Initial build.
