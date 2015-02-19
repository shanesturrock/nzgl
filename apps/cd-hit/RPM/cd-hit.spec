%define rel_date 2012-08-27

Name:		cd-hit
Version:	4.6.1
Release:	1%{?dist}
Summary:	A program for clustering and comparing protein or nucleotide sequences.
Group:		Applications/Engineering
License:	GPLv2
URL:		http://weizhong-lab.ucsd.edu/cd-hit/
Source0:	https://cdhit.googlecode.com/files/%{name}-v%{version}-%{rel_date}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
CD-HIT is a very widely used program for clustering and comparing protein or nucleotide 
sequences. CD-HIT was originally developed by Dr. Weizhong Li at Dr. Adam Godzik's Lab 
at the Burnham Institute (now Sanford-Burnham Medical Research Institute).

%prep
%setup -q -n %{name}-v%{version}-%{rel_date}

%build
make %{?_smp_mflags} openmp=yes

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
make install PREFIX=%{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/cdhit-user-guide.pdf ChangeLog README license.txt
%{_bindir}/cd-hit
%{_bindir}/cd-hit-2d
%{_bindir}/cd-hit-2d-para.pl
%{_bindir}/cd-hit-454
%{_bindir}/cd-hit-div
%{_bindir}/cd-hit-div.pl
%{_bindir}/cd-hit-est
%{_bindir}/cd-hit-est-2d
%{_bindir}/cd-hit-para.pl
%{_bindir}/clstr2tree.pl
%{_bindir}/clstr_merge_noorder.pl
%{_bindir}/clstr_merge.pl
%{_bindir}/clstr_reduce.pl
%{_bindir}/clstr_renumber.pl
%{_bindir}/clstr_rev.pl
%{_bindir}/clstr_sort_by.pl
%{_bindir}/clstr_sort_prot_by.pl
%{_bindir}/make_multi_seq.pl
%{_bindir}/plot_2d.pl
%{_bindir}/plot_len1.pl
%{_bindir}/psi-cd-hit-2d-g1.pl
%{_bindir}/psi-cd-hit-2d.pl
%{_bindir}/psi-cd-hit-local.pl
%{_bindir}/psi-cd-hit.pl
%{_bindir}/clstr2txt.pl
%{_bindir}/clstr2xml.pl
%{_bindir}/clstr_cut.pl
%{_bindir}/clstr_quality_eval.pl
%{_bindir}/clstr_quality_eval_by_link.pl
%{_bindir}/clstr_rep.pl
%{_bindir}/clstr_reps_faa_rev.pl
%{_bindir}/clstr_select.pl
%{_bindir}/clstr_select_rep.pl
%{_bindir}/clstr_size_histogram.pl
%{_bindir}/clstr_size_stat.pl
%{_bindir}/clstr_sql_tbl.pl
%{_bindir}/clstr_sql_tbl_sort.pl

%changelog

* Thu Aug 30 2012 Carl Jones <carl@biomatters.com> - 4.6.1-1
- New upstream release.

* Thu Aug 09 2012 Carl Jones <carl@biomatters.com> - 4.5.7-1
- New upstream release.

* Thu Jul 26 2012 Carl Jones <carl@biomatters.com> - 4.5.4-1
- Initial build.
