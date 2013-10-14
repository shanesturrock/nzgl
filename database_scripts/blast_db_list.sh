# Lists updated databases not present in Galaxy loc files

blastdb="blastdb.loc"
blastdb_p="blastdb_p.loc"
blastdb_d="blastdb_d.loc"
blast_db_add="/usr/bin/blast_db_add.sh"

# Databases are listed in reverse desired order for the loc files

nucleotide_dbs=( refseq_rna refseq_genomic other_genomic human_genomic pdbnt patnt all_contig wgs tsa_nt sts htgs gss est_others est_mouse est_human est env_nt nt )
protein_dbs=( pataa pdbaa refseq_protein swissprot env_nr nr )

echo "Adding new databases to ${blastdb}"
for db_name in ${nucleotide_dbs[@]}
do
  ${blast_db_add} ${blastdb} ${db_name}
done

# Protein databases
echo "Adding new databases to ${blastdb_p}"
for db_name in ${protein_dbs[@]} 
do
  ${blast_db_add} ${blastdb_p} ${db_name}
done

# Domain databases
echo "Adding new databases to ${blastdb_d}"
${blast_db_add} ${blastdb_d} cdd_delta
