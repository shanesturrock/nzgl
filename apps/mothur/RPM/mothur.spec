Name:		mothur
Version:	1.35.1
Release:	1%{?dist}
Summary:	Computational microbial ecology tool
Group:		Applications/Engineering
License:	GPLv3
URL:		http://www.mothur.org/w/images/b/bc/Mothur.%{version}.zip
Source0:	mothur-%{version}.tar.gz
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
%setup -q   -n mothur-%{version}/source
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
* Thu Jun 04 2015 Shane Sturrock <shane@biomatters.com> - 1.35.1-1
- New commands
  - get.mimarkspackage - create blank mimarks package form for sra command 
    (see Creating a new submission)
  - make.sra - create submission ready files (see Creating a new submission)
  - Added common command line options. Can now use -q or --quiet, -h or --help,
    -v or --version.
- Feature updates
  - set.dir - added seed parameter to allow the user to set the seed for the 
    random number generator
  - make.contigs - improved speed, added pandaseq-based quality score data, 
    added kmer aligning method
  - cluster.split - allows one to use the cluster.classic option if they set 
    the classic option to T. This is likely the most ideal option for people 
    using tax level 5 or 6.
  - make.biom - added relabund file as input.
  - pcr.seqs - added fdiffs and rdiffs comments
  - cluster, cluster.split, cluster.classic, phylotype, mgcluster - Clustering 
    commands did not include the count file info. when printing list file OTU 
    order. Only effects clustering commands. *.pick commands must preserve 
    otuLabels order.
  - classify.tree - added output parameter. Output=node or taxon. Default=node. 
    Output=taxon will label tree with consensus taxonomies.
  - get.coremicrobiome - the abundance option can now accept float values. 
    abundance=1 or abundance=0.01 produce same results. Abundance=0.005 or 
    other values between 0 and 1, instead of the 1% as the lowest value.
  - chop.seqs - added keepn parameter. Default=f.
  - Restructured source files on github for easier downloads and builds.
- Bug fixes
  - cluster.split - MPI version compile issue fixed in 1.34.1.
  - summary.seqs - multiple processors Windows. fixed 1.34.2
  - summary.seqs -MPI bug fixed 1.34.2
  - pcr.seqs - use of mothur's paired primer tag instead of forward and 
    reverse tags causing improper trimming fixed in 1.34.3.
  - sffinfo - parsed sff files giving corrupt error fixed 1.34.4
  - pcr.seqs - Windows multiple processors with start and end parameters 
    giving errors fixed 1.34.4
  - make.contigs - Bug in Windows paralell processing.
  - dist.seqs - bug introduced in 1.34.4
  - rarefaction.single - returning median instead of mean.
  - make.contigs - skipping groups if invalid fastq files provided.
  - make.contigs - bug that required barcodes to process.
  - metastats - infinite loop.
  - pcr.seqs - When sequence length < primer Length + pdiffs, basic_string 
    error occurred. Rare case.
  - mothur will now read over null strings to avoid pesky sequence not found 
    errors.
  - Fixes mismatch name issue with make.contigs in v1.35.0

* Mon Jan 12 2015 Shane Sturrock <shane@biomatters.com> - 1.34.4-1
- sffinfo - parsed sff files giving corrupt error.
- pcr.seqs - Windows multiple processors with start and end parameters giving 
  errors.

* Mon Dec 15 2014 Shane Sturrock <shane@biomatters.com> - 1.34.3-1
- pcr.seqs - use of mothur's paired primer tag instead of forward and 
  reverse tags causing improper trimming.

* Thu Dec 04 2014 Shane Sturrock <shane@biomatters.com> - 1.34.2-1
- cluster.split - MPI version compile issue
- summary.seqs - multiple processors Windows

* Wed Nov 26 2014 Shane Sturrock <shane@biomatters.com> - 1.34.1-1
- Upstream update

* Wed Nov 19 2014 Shane Sturrock <shane@biomatters.com> - 1.34.0-1
- New commands
  - Classify.svm - Rank OTUs using the support vector machine learning 
    algorithm
- Feature updates
  - added shannonrange calculator to collect.single, summary.single, 
    rarefaction.single.
  - added shared parameter to count.seqs aka make.table command. Can be used 
    to transpose the shared file for use with other software packages.
  - consensus.seqs cutoff parameter can now be a float. cutoff=97.5.w
  - dist.shared - when subsample used *.ave distance matrix saved as current 
    phylip file
  - tree.shared - added Jensen-Shannon Divergence calculator, jsd and Square 
    Root Jensen-Shannon Divergence calculator, rjsd. 
    http://www.mothur.org/forum/viewtopic.php?f=5&t=2961
  - cluster.split - added the file option which allows you to enter
    your file containing your list of column and names/count files as well
    as the singleton file. This file is mothur generated, when you run
    cluster.split() with the cluster=f parameter. This can be helpful when
    you have a large dataset that you may be able to use all your
    processors for the splitting step, but have to reduce them for the
    cluster step due to RAM constraints. For example:
    cluster.split(fasta=yourFasta, taxonomy=yourTax, count=yourCount,
    taxlevel=3, cluster=f, processors=8) then cluster.split(file=yourFile,
    processors=4). This allows your to maximize your processors during the
    splitting step. Also, if you are unsure if the cluster step will have
    RAM issue with multiple processors, you can avoid running the first
    part of the command multiple times.
  - make.contigs - added checkorient parameter. 
    http://www.mothur.org/forum/viewtopic.php?f=3&t=2993.
  - fastq.info, sffinfo, trim.flows- added checkorient parameter.
  - trim.flows can now process paired barcodes and primers.
  - fastq.info - file option can parse 3 different file formats.
  - make.shared - can now handle taxon table biom files. 
    http://www.mothur.org/forum/viewtopic.php?f=3&t=3352
  - standard handling of mothur's oligos file across commands.
  - pcr.seqs reverse primers use pdiffs. 
    http://xn--ww-dcc.mothur.org/forum/viewtopic.php?f=4&t=3392
  - fastq.info, sffinfo, trim.flows, trim.seqs - pdiffs can be used with 
    removal of reverse primers.
  - update version of catchall to 4.0.
  - trim.seqs and make.contigs - added more output to fasta files about diffs.
  - classify.otu - added probs to unclassifieds to avoid error in make.biom 
    http://www.mothur.org/forum/viewtopic.php?f=3&t=2835&start=10
- Bug fixes
  - fastq.info stopped processing after 100001 seqs. 
    http://www.mothur.org/forum/viewtopic.php?f=4&t=2829 fixed 1.33.1
  - make.biom picrust couldn't handle unclassifieds 
    http://www.mothur.org/forum/viewtopic.php?f=4&t=2816 fixed 1.33.1
  - create.database OutLabel bug - "cannot convert Otu0001 to an integer" 
    fixed 1.33.3
  - merge.sfffiles -Windows version caused substring error on parse. 
    fixed 1.33.2 3/11 version.
  - chimera.slayer - "[megablast] FATAL ERROR: blast: Unable to open input file
    on linux version with multiple processors. fixed 1.33.3
  - rarefaction.single - *.groups.rarefaction file labels in wrong order 
    http://www.mothur.org/forum/viewtopic.php?f=4&t=2963 fixed 1.33.3
  - align.seqs - Windows align.seqs flip=t caused segfault 
    fixed 1.33.2 3/19 version
  - summary.shared subsample issue 
    http://www.mothur.org/forum/viewtopic.php?f=4&t=2861 fixed 1.33.3
  - seq.error was changing the current fasta file to the seq file. it 
    shouldn't change the current fasta file.
  - trim.seqs - qaverage bug scrapping seqs - fixed 1.33.3 4/4.
  - make.biom - "biom error: cannot convert null to a float"
  - get.seqs, remove.seqs, remove.lineage, get.lineage, screen.seqs, pcr.seqs 
    changed read of count file causing file mismatches with count files that 
    didn't include group data.
  - clearcut - distances out of range bug
  - dist.shared - http://www.mothur.org/forum/viewtopic.php?f=3&t=3186
  - make.contigs - rindex files 
    http://www.mothur.org/forum/viewtopic.php?f=3&t=3159&start=10#p9096
  - lefse - segfault if a sample only included 1 group.
  - cluster - nearest method caused crash.

* Mon Mar 24 2014 Shane Sturrock <shane@biomatters.com> - 1.33.3-1
- Upstream update, no details of what
* Wed Mar 05 2014 Shane Sturrock <shane@biomatters.com> - 1.33.2-1
- Remove unnecessary error messages.
* Thu Feb 26 2014 Shane Sturrock <shane@biomatters.com> - 1.33.1-1
- Fix bug in fastq.info misreporting the number of reads
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
