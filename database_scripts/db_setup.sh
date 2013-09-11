#!/bin/bash

set -e
index_path='/databases/indexes'
tooldata_path='/home/galaxy/galaxy-dist/tool-data'

if [ $# -lt 2 ]; then
	echo "$0 <input 2bit file> <long name>"
	exit 1
fi

input_file="${1}"
long_name="${2}"
base_filename="$(echo ${input_file} | sed s/\.2bit//g)"
base_path="${index_path}/${base_filename}"
fasta_file="${base_path}/seq/${base_filename}.fa"

echo "${input_file} ${long_name} ${base_filename}"

if [ ! -e ${tooldata_path} ]; then
	echo "Tool Data directory ${tooldata_path} does not exist."
	exit 1
fi

if [ ! -e ${base_path} ]; then
	echo "Base index directory ${base_path} does not exist."
	exit 1
fi

if [ ! -e "${base_path}/seq/${input_file}" ]; then
	echo "Input file ${base_path}/seq/${input_file} does not exist."
	exit 1
fi

# Convert 2bit to fasta, if it does not exist
if [ ! -e ${fasta_file} ]; then
	cd ${base_path}/seq
	twoBitToFa ${input_file} ${fasta_file}
fi


# Format databases in parallel
{
  # Create bowtie indexes
  mkdir -p ${base_path}/bowtie_index
  cd ${base_path}/bowtie_index
  ln -sf ${fasta_file} .
  {
    bowtie-build -f ${fasta_file} ${base_filename}
    grep -qai "${base_filename}" ${tooldata_path}/bowtie_indices.loc &>/dev/null || \
      echo -e "${base_filename}\t${base_filename}\t${long_name}\t${base_path}/bowtie_index/${base_filename}" >> ${tooldata_path}/bowtie_indices.loc
    bismark_genome_preparation --verbose ${base_path}/bowtie_index/
  } &


  # Create bowtie2 indexes
  mkdir -p ${base_path}/bowtie2_index
  cd ${base_path}/bowtie2_index
  ln -sf ${fasta_file} .
  {
    bowtie2-build -f ${fasta_file} ${base_filename}
    grep -qai "${base_filename}" ${tooldata_path}/bowtie2_indices.loc &>/dev/null || \
      echo -e "${base_filename}\t${base_filename}\t${long_name}\t${base_path}/bowtie2_index/${base_filename}" >> ${tooldata_path}/bowtie2_indices.loc
    bismark_genome_preparation --bowtie2 --verbose ${base_path}/bowtie2_index/
  } &

  # Create bwa indexes
  mkdir -p ${base_path}/bwa_index
  cd ${base_path}/bwa_index
  ln -sf ${fasta_file} .
  {
    bwa index -a bwtsw $(basename ${fasta_file})
    grep -qai "${base_filename}" ${tooldata_path}/bwa_index.loc &>/dev/null || \
      echo -e "${base_filename}\t${base_filename}\t${long_name}\t${base_path}/bwa_index/${base_filename}.fa" >> ${tooldata_path}/bwa_index.loc
  } &

  # Create bwa indexes for 0.59 needed by galaxy
  mkdir -p ${base_path}/bwa_index_059
  cd ${base_path}/bwa_index_059
  ln -sf ${fasta_file} .
  {
    /home/galaxy/galaxy-dist/tool-dependencies/bwa/0.5.9/devteam/bwa_wrappers/150b3fe44caa/bin/bwa index -a bwtsw $(basename ${fasta_file})
    grep -qai "${base_filename}" ${tooldata_path}/bwa_index.loc &>/dev/null || \
      echo -e "${base_filename}\t${base_filename}\t${long_name}\t${base_path}/bwa_index_059/${base_filename}.fa" >> ${tooldata_path}/bwa_index.loc
  } &


  # Create sam indexes
  mkdir -p ${base_path}/sam_index
  cd ${base_path}/sam_index
  ln -sf ${fasta_file} .
  {
    samtools faidx $(basename ${fasta_file})
    grep -qai "${base_filename}" ${tooldata_path}/sam_fa_indices.loc &>/dev/null || \
      echo -e "index\t${base_filename}\t${base_path}/sam_index/${base_filename}.fa" >> ${tooldata_path}/sam_fa_indices.loc
  } &

  # Need to wait until all jobs complete
  wait
}

echo "Databases formatted"
