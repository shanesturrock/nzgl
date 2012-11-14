%global packname  ggplot2
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.9.2.1
Release:          1%{?dist}
Summary:          An implementation of the Grammar of Graphics

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-methods 
Requires:         R-plyr R-digest R-grid R-gtable R-reshape2 R-scales R-memoise R-proto R-MASS 

BuildRequires:    R-devel tex(latex) R-stats R-methods
BuildRequires:    R-plyr R-digest R-grid R-gtable R-reshape2 R-scales R-memoise R-proto R-MASS 


%description
An implementation of the grammar of graphics in R. It combines the
advantages of both base and lattice graphics: conditioning and shared axes
are handled automatically, and you can still build up a plot step by step
from multiple data sources. It also implements a sophisticated
multidimensional conditioning system and a consistent interface to map
data to aesthetic attributes. See the ggplot2 website for more
information, documentation and examples.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data/*
%{rlibdir}/%{packname}/test_ns/*
%{rlibdir}/%{packname}/tests/*

%changelog
* Mon Sep 24 2012 Carl Jones <carl@biomatters.com> 0.9.2.1-1
- initial package
