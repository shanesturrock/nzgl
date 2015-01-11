%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:             python-biopython
Version:          1.65
Release:          0%{?dist}
Summary:          Python tools for computational molecular biology
Source0:          http://biopython.org/DIST/biopython-%{version}.tar.gz
License:          MIT
Url:              http://www.biopython.org/
Group:            Development/Libraries
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:    python-devel
BuildRequires:    flex
BuildRequires:    python-reportlab
BuildRequires:    numpy
BuildRequires:    MySQL-python
BuildRequires:    python-psycopg2
Requires:         python-reportlab
Requires:         numpy
Requires:         MySQL-python
Requires:         python-psycopg2
Requires:         wise2

%description
A set of freely available Python tools for computational molecular
biology.

%prep
%setup -q -n biopython-%{version}
# enable build of Bio.PDB.mmCIF.MMCIFlex (requires flex)
#%patch0 -p0

# remove all execute bits from documentation and fix line endings
find Scripts -type f -exec chmod -x {} 2>/dev/null ';'
find Doc -type f -exec chmod -x {} 2>/dev/null ';'
find Doc -type f -exec sed -i 's/\r//' {} 2>/dev/null ';'

# remove execute bits from Python modules
find Bio -type f -exec chmod -x {} 2>/dev/null ';'
# remove she-bang lines in .py files to keep rpmlint happy
find Bio -type f -name "*.py" -exec sed -i '/^#![ ]*\/usr\/bin\/.*$/ d' {} 2>/dev/null ';'

%build
env CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT --install-data=%{_datadir}/python-biopython

## disable tests for the moment
%check
%{?_with_check:%{__python} setup.py test --no-gui || :}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Doc Scripts
%doc CONTRIB DEPRECATED LICENSE NEWS README
%{python_sitearch}/*egg-info
%dir %{python_sitearch}/Bio
%{python_sitearch}/Bio/*
%dir %{python_sitearch}/BioSQL
%{python_sitearch}/BioSQL/*

%changelog
* Fri Dec 19 2014 Shane Sturrock <shane@biomatters.com> - 1.65-1
- This release of Biopython supports Python 2.6, 2.7, 3.3 and 3.4. It is
  also tested on PyPy 2.0 to 2.4, PyPy3 version 2,4, and Jython 2.7b2.
- The most visible change is that the Biopython sequence objects now
  use string comparison, rather than Python’s object comparison. This
  has been planned for a long time with warning messages in place
  (under Python 2, the warnings were sadly missing under Python 3).
- The Bio.KEGG and Bio.Graphics modules have been expanded with
  support for the online KEGG REST API, and parsing, representing
  and drawing KGML pathways.
- The Pterobranchia Mitochondrial genetic code has been added to
  Bio.Data (and the translation functionality), which is the new NCBI
  genetic code table 24.
- The Bio.SeqIO parser for the ABI capillary file format now exposes
  all the raw data in the SeqRecord’s annotation as a dictionary. This
  allows further in-depth analysis by advanced users.
- Bio.SearchIO QueryResult objects now allow Hit retrieval using its
  alternative IDs (any IDs listed after the first one, for example as
  used with the NCBI BLAST NR database).
- Bio.SeqUtils.MeltingTemp has been rewritten with new functionality.
- The new experimental module Bio.CodonAlign has been renamed
  Bio.codonalign (and similar lower case PEP8 style module names
  have been used for the sub-modules within this).
- Bio.SeqIO.index_db(…) and Bio.SearchIO.index_db(…) now store
  any relative filenames relative to the index file, rather than (as
  before) relative to the current directory at the time the index was
  built. This makes the indexes less fragile, so that they can be used
  from other working directories. NOTE: This change is backward
  compatible (old index files work as before), however relative paths
  in new indexes will not work on older versions of Biopython!
- Behind the scenes, we have done a lot of work applying PEP8
  coding styles to Biopython, and improving the formatting of the
  source code documentation (PEP257 docstrings).

* Fri May 30 2014 Shane Sturrock <shane@biomatters.com> - 1.64-1
- This release of Biopython supports Python 2.6 and 2.7, 3.3 and also
  the new 3.4 version. It is also tested on PyPy 2.0 to 2.3, and Jython
  2.7b2.
- The new experimental module Bio.CodonAlign facilitates building
  codon alignment and further analysis upon it. This work is from the
  Google Summer of Code (GSoC) project by Zheng Ruan.
- Bio.Phylo now has tree construction and consensus modules, from on
  the GSoC work by Yanbo Ye.
- Bio.Entrez will now automatically download and cache new NCBI DTD
  files for XML parsing under the user’s home directory (using
  ~/.biopython on Unix like systems, and $APPDATA/biopython on Windows).
- Bio.Sequencing.Applications now includes a wrapper for the samtools
  command line tool.
- Bio.PopGen.SimCoal now also supports fastsimcoal.
- SearchIO hmmer3-text, hmmer3-tab, and hmmer3-domtab now support
  output from hmmer3.1b1.
- BioSQL can now use the mysql-connector package (available for Python
  2, 3 and PyPy) as an alternative to MySQLdb (Python 2 only) to connect
  to a MySQL database.

* Mon Dec 09 2013 Shane Sturrock <shane@biomatters.com> - 1.63-1
- First release of biopython which officially supports Python 3.
- Now uses the Python 3 style built-in next function in place of the Python 
  2 style iterators’ .next() method.
- The current version removed the requirement of the 2to3 library.

* Fri Aug 30 2013 Shane Sturrock <shane@biomatters.com> - 1.62-1
- Final release with support for Python 2.5.  
- Adds warnings when translating partial codons.
- Modifies handling of joins and complex features in GenBank/EMBL files.
- Phylo module gains NeXML and CDAO format support.
- Newick parser faster and can extract bootstrap values from Newick comments.
- New Bio.UniPro module.
- BioSQL module supported in Jython.
- Feature labels on circular GenomeDiagram now support label_position.
- 3D structure parsing in mmCIF files updated.
- Bio.Sequencing.Applications module now includes BWA wrapper.
- Bio.motifs supports JASPAR format files.
- Other minor bug fixes and unit tests.

* Thu Feb 07 2013 Carl Jones <carl@biomatters.com> - 1.61-1
- New upstream release

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 1.60-2
- Rebuild

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 1.60-1
- New upstream version

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  9 2012 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.59-1
- Update to latest upstream (1.59) (#797872)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.58-1
- Update to upstream 1.58

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.55-0.2.b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.55-0.1.b
- Update to 1.55 beta
- BuildRequires: flex-static, libraries are now split out

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri May 21 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.54-1
- Update to upstream 1.54

* Tue Apr  6 2010 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.54-0.1.b
- Update to 1.54 beta

* Tue Dec 15 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.53-1
- Update to upstream 1.53

* Thu Oct 15 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.52-1
- Update to latest upstream (1.52)

* Tue Aug 18 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.51-1
- Update to upstream 1.51
- Drop mx {Build}Requires, no longer used upstream
- Remove Martel modules, no longer distributed upstream
- Add flex to BuildRequires, patch setup to build
  Bio.PDB.mmCIF.MMCIFlex as per upstream:
  http://bugzilla.open-bio.org/show_bug.cgi?id=2619

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  1 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.49-1
- Update to latest upstream (1.49) uses numpy and new API for psycopg2
- [Build]Requires python-numeric -> numpy 
- [Build]Requires python-psycopg -> python-psycopg2
- Remove interactive question hack, no longer needed

* Sun Nov 30 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.48-3
- Temporarily disable python-psycopg dependency until it is rebuilt
  for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.48-2
- Rebuild for Python 2.6

* Mon Sep 29 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.48-1
- Update to latest upstream (1.48)

* Fri Jul  4 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.47-1
- Update to latest upstream (1.47)

* Sun Mar 23 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.45-1
- Update to latest upstream (1.45)

* Sat Feb  9 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.44-4
- rebuilt for GCC 4.3 as requested by Fedora Release Engineering

* Thu Dec 13 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.44-3
- Include eggs in file list for F9+

* Sun Oct 28 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.44-2
- Drop patch to setup.py, applied upstream

* Sun Oct 28 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.44-1
- Update to latest upstream (1.44).

* Mon Aug 27 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.43-5
- Used "MIT" as short license name as the "Biopython License
  Agreement" is the same as the CMU MIT variant.

* Mon Apr 25 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.43-4
- Add wise2 Requires since the Wise biopython module uses the
  command-line behind-the-scenes.

* Mon Apr 17 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.43-3
- Use python_sitearch macro to enable x86_64 builds work.

* Mon Apr 16 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.43-2
- Fix Source0 URL as per suggestion from Parag AN on #235989.

* Mon Apr 02 2007 Alex Lancaster <alexlan[AT]fedoraproject.org> 1.43-1
- Initial Fedora package.


