#!/bin/bash

set -e
index_path='/home/galaxy/galaxy-dist/indexes'
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

# Create bowtie2 indexes
mkdir -p ${base_path}/bowtie2_index
cd ${base_path}/bowtie2_index
ln -sf ${fasta_file} .
bowtie2-build -f ${fasta_file} ${base_filename}
grep -qai "${base_filename}" ${tooldata_path}/bowtie2_indices.loc &>/dev/null || \
  echo -e "${base_filename}\t${base_filename}\t${long_name}\t${base_path}/bowtie2_index" >> ${tooldata_path}/bowtie2_indices.loc

# Create bwa indexes
mkdir -p ${base_path}/bwa_index
cd ${base_path}/bwa_index
ln -sf ${fasta_file} .
bwa index -a bwtsw $(basename ${fasta_file})
grep -qai "${base_filename}" ${tooldata_path}/bwa_index.loc &>/dev/null || \
  echo -e "${base_filename}\t${base_filename}\t${long_name}\t${base_path}/bwa_index" >> ${tooldata_path}/bwa_index.loc

# Create sam indexes
mkdir -p ${base_path}/sam_index
cd ${base_path}/sam_index
ln -sf ${fasta_file} .
samtools faidx $(basename ${fasta_file})
grep -qai "${base_filename}" ${tooldata_path}/sam_fa_indices.loc &>/dev/null || \
  echo -e "index\t${base_filename}\t${base_path}/sam_index" >> ${tooldata_path}/sam_fa_indices.loc
