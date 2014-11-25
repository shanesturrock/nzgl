Name:		cutadapt
Version:	1.7.1
Release:	1%{?dist}
Summary:	A tool that removes adapter sequences from DNA sequencing reads
Group:		Applications/Engineering
License:	MIT License
URL:		http://code.google.com/p/cutadapt/
Source0:	http://cutadapt.googlecode.com/files/cutadapt-%{version}.tar.gz
BuildRequires:	python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
cutadapt removes adapter sequences from high-throughput sequencing data. This is usually 
necessary when the read length of the sequencing machine is longer than the molecule 
that is sequenced, for example when sequencing microRNAs.

%prep
%setup -q

%build
python setup.py build_ext -i
python setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_prefix}
python setup.py install --prefix=%{buildroot}/%{_prefix}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst
%{_bindir}/cutadapt
%{_libdir}/python2.6/site-packages/cutadapt/*
%{_libdir}/python2.6/site-packages/cutadapt-%{version}-py2.6.egg-info

%changelog
* Wed Nov 26 2014 Shane Sturrock <shane@biomatters.com> - 1.7.1-1
- IUPAC characters are now supported. For example, use ``-a YACGT`` for an
  adapter that matches both ``CACGT`` and ``TACGT`` with zero errors. Disable
  with ``-N``. By default, IUPAC characters in the read are not interpreted in
  order to avoid matches in reads that consist of many (low-quality) ``N``
  bases. Use ``--match-read-wildcards`` to enable them also in the read.
- Support for demultiplexing was added. This means that reads can be written to
  different files depending on which adapter was found. See `the section in the
  documentation for how to use it. This is currently only supported for 
  single-end reads.
- Add support for anchored 3' adapters. Append ``$`` to the adapter sequence to
  force the adapter to appear in the end of the read (as a suffix). Closes
  issue #81.
- Option ``--cut`` (``-u``) can now be specified twice, once for each end of the
  read. Thanks to Rasmus Borup Hansen for the patch!
- Options ``--minimum-length``/``--maximum-length`` (``-m``/``-M``) can be used
  standalone. That is, cutadapt can be used to filter reads by length without
  trimming adapters.
- Fix bug: Adapters read from a FASTA file can now be anchored.

* Thu Oct 09 2014 Sidney Markowitz <sidney@biomatters.com> - 1.6-1
- Bug fix, ensure --format=... can be used even with paired-end input
- Bug fix, some output files would be missing last part of output
- Alignment algorithm is slightly faster
- For 3' adapters, statistics about the bases preceding the trimmed adapter
  are collected and printed. If one of the bases is overrepresented,
  a warning is shown since this points to an incomplete adapter sequence.
  This happens, for example, when a TruSeq adapter is used but the A
  overhang is not taken into account when running cutadapt.
- A change in behavior: If you use --discard-trimmed or --discard-untrimmed
  in combination with --too-short-output or --too-long-output, then cutadapt
  now writes also the discarded reads to the output files given by the
  --too-short or --too-long options.

* Wed Sep 17 2014 Shane Sturrock <shane@biomatters.com> - 1.5-1
- Adapter sequences can now be read from a FASTA file. For example, write
  `-a file:adapters.fasta` to read 3' adapters from `adapters.fasta`. This 
  works also for `-b` and `-g`.
- Add the option `--mask-adapter`, which can be used to not remove adapters,
  but to instead mask them with `N` characters. Thanks to Vittorio Zamboni
  for contributing this feature!
- U characters in the adapter sequence are automatically converted to T.
- Do not run Cython at installation time unless the --cython option is 
  provided.
- Add the option -u/--cut, which can be used to unconditionally remove a 
  number of bases from the beginning or end of each read.
- Make `--zero-cap` the default for colorspace reads.
- When the new option `--quiet` is used, no report is printed after all reads
  have been processed.
- When processing paired-end reads, cutadapt now checks whether the reads are
  properly paired.
- To properly handle paired-end reads, an option --untrimmed-paired-output was
  added.

* Thu Jul 31 2014 Shane Sturrock <shane@biomatters.com> - 1.4.2-1
- Reading and writing of FASTQ files is faster (thanks to Cython).
- Reading and writing of gzipped files is faster (up to 2x) on systems
  where the gzip program is available.
- The quality trimming function is four times faster (also due to
  Cython).
- Fix the statistics output for 3' colorspace adapters: The reported
  lengths were one too short. Thanks to Frank Wessely for reporting
  this.
- Support the --no-indels option. This disallows insertions and
  deletions while aligning the adapter. Currently, the option is only
  available for anchored 5' adapters. This fixes  issue 69 .
- As a sideeffect of implementing the --no-indels option: For
  colorspace, the length of a read (for --minimum- and --maximum-length)
  is now computed after primer base removal (when --trim-primer is
  specified).
- Added one column to the info file that contains the name of the found
  adapter.

* Mon Nov 11 2013 Shane Sturrock <shane@biomatters.com> - 1.3-1
- Preliminary paired-end support with the --paired-output option (contributed by
  James Casbon). See the README section on how to use it.
- Improved statistics.
- Fix incorrectly reported amount of quality-trimmed Mbp (issue 57, fix by 
  Chris Penkett)
- Add the `--too-long-output` option.
- Add the `--no-trim` option, contributed by Dave Lawrence.
- Port handwritten C alignment module to Cython.
- Fix the `--rest-file` option (issue 56)
- Slightly speed up alignment of 5' adapters.
- Support bzip2-compressed files.
* Mon Dec 03 2012 Carl Jones <carl@biomatters.com> - 1.2.1-1
- New upstream release
* Fri Jul 27 2012 Carl Jones <carl@biomatters.com> - 1.1-2
- Add BuildRoot
- Add BuildRequires
* Fri Jul 27 2012 Carl Jones <carl@biomatters.com> - 1.1-1
- Initial build.
