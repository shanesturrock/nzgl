Name:		mothur
Version:	1.33.0
Release:	1%{?dist}
Summary:	Computational microbial ecology tool
Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.mothur.org/w/images/b/bc/Mothur.1.33.0.zip
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
%{_bindir}/%{name}

%changelog
* Thu Feb 20 2014 Shane Sturrock <shane@biomatters.com> - 1.33.0-1
- Feature updates
  - heatmap.bin - added otuLabels
  - make mothur "smarter" about OTULabels. OTU001 and OTU01 should be the same.
  - list.seqs, get.seqs and remove.seqs - added fastq as an option
  - add otulabels to list file
  - make.biom - added picrust and reftaxonomy parameters.
  - mothur will preserve information after sequence names in a fasta file.
  - venn - permute parameter can equal 1, 2, 3, or 4. 
  - get.oturep - changed otu numbers to be labels
  - deunique.seqs - added count table 
  - nmds - added group label to *.axes file 
  - fastq.info - added oligos, group, pdiffs, bdiffs, ldiffs, sdiffs, tdiffs 
    parameters so you can split fastq files by sample.
  - sffinfo - added group parameter so you can split sff files by group
  - dist.shared, collect.shared and summary.shared - added Jensen-Shannon 
    Divergence calculator, jsd.
  - dist.shared, collect.shared and summary.shared - added Square Root 
    Jensen-Shannon Divergence calculator, rjsd.
  - trim.seqs - added logtransform parameter to
  - trim.seqs - reorient parameter no longer requires paired barcodes and 
    primers
  - metastats, unifrac.weighted, unifrac.unweighted, parsimony, chimera.uchime,
    chimera.perseus, chimera.slayer, shhh.seqs and pre.cluster: improved work 
    balance load between processors for paralellized commands
  - get.communitytype - added dmm, pam and kmeans methods
  - get.communitytype - added calc, subsample, iters parameters for 
    calculations in pam and kmeans.
  - get.current - added directory information.
  - classify.seqs and summary.tax - added relabund parameter. relabund=t 
    outputs relative abundances to *.summary file instead of raw abundances. 
    Default=f.
- Bug fixes
  - chimera.uchime, chimera.perseus, chimera.slayer - with count table and 
    dereplicate=t caused total=0 error message.
  - sff.multiple - setting processors=1 for future commands. Not using file 
    redirects in commands it runs.
  - venn - fixed bug where command overwrote .sharedotu files when permute=t
  - pcr.seqs keepdots=f could cause an aligned template to become unaligned.
  - summary.shared - *.ave.dist matrix = 0 when processors > 2 when using the 
    subsample parameter and not using the distance parameter. 
  - classify.otu - error in *.tax.summary counts with basis=sequence when 
    using a count file. 
  - sffinfo - windows version with oligos file
  - set.current - setting processors option to 1, if not set.
  - trim.flows - printing trimmed number of flows to scrap file instead of 
    original number of flows. Caused error if you wanted to read scrapped flow 
    file.
  - get.oturep - countable caused sequence not found error.

* Thu Oct 17 2013 Shane Sturrock <shane@biomatters.com> - 1.32.1-1
- Upstream update, no details of why.

* Thu Oct 03 2013 Shane Sturrock <shane@biomatters.com> - 1.32.0-1
- Upstream update - see http://www.mothur.org/wiki/Mothur_v.1.32.0

* Thu Sep 05 2013 Shane Sturrock <shane@biomatters.com> - 1.31.2-1
- Initial build.
