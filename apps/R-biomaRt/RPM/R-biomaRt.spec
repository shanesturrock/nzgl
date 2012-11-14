%global packname  biomaRt

Name:             R-%{packname}
Version:          2.14.0
Release:          1%{?dist}
Summary:          R Interface to BioMart databases
Group:            Applications/Productivity
License:          Artistic 2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/biomaRt.html
Source0:          http://www.bioconductor.org/packages/2.9/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-core >= 2.7.0, texlive-latex, R-XML, R-RCurl
BuildRequires:    R-devel >= 2.7.0, R-XML, R-RCurl
BuildArch:        noarch

%description
In recent years a wealth of biological data has become available in public 
data repositories. Easy access to these valuable data resources and firm 
integration with data analysis is needed for comprehensive bioinformatics data 
analysis. biomaRt provides an interface to a growing collection of databases 
implementing the BioMart software suite (http://www.biomart.org). The package 
enables retrieval of large amounts of data in a uniform way without the need 
to know the underlying database schemas or write complex SQL queries. Examples 
of BioMart databases are Ensembl, COSMIC, Uniprot, HGNC, Gramene, Wormbase and 
dbSNP mapped to Ensembl. These major databases give biomaRt users direct 
access to a diverse set of data and enable a wide range of powerful online 
queries from gene annotation to database mining.

%prep
%setup -c -q -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_datadir}/R/library
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_datadir}/R/library/R.css

%check
# Enable if R-annotate ever arrives in Fedora.
# %%{_bindir}/R CMD check %%{packname}

%files
%dir %{_datadir}/R/library/%{packname}/
%doc %{_datadir}/R/library/%{packname}/doc/
%doc %{_datadir}/R/library/%{packname}/html/
%doc %{_datadir}/R/library/%{packname}/DESCRIPTION
%doc %{_datadir}/R/library/%{packname}/CITATION
%{_datadir}/R/library/%{packname}/NAMESPACE
%{_datadir}/R/library/%{packname}/INDEX
%{_datadir}/R/library/%{packname}/Meta/
%{_datadir}/R/library/%{packname}/R/
%{_datadir}/R/library/%{packname}/help/
%{_datadir}/R/library/%{packname}/scripts/

%changelog
* Wed Oct 31 2012 Carl Jones <carl@biomatters.com> - 2.14.0-1
- New upstream release
* Wed Aug 29 2012 Carl Jones <carl@biomatters.com> - 2.12.0-1
- New upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Tom "spot" Callaway <tcallawa@redhat.com> 2.10.0-1
- initial package for Fedora
