echo "Put these in blast.loc"
/usr/bin/blast_db_add.sh nt
/usr/bin/blast_db_add.sh env_nt
/usr/bin/blast_db_add.sh est
/usr/bin/blast_db_add.sh est_human
/usr/bin/blast_db_add.sh est_mouse
/usr/bin/blast_db_add.sh est_others
/usr/bin/blast_db_add.sh gss
/usr/bin/blast_db_add.sh htgs
/usr/bin/blast_db_add.sh sts
/usr/bin/blast_db_add.sh tsa_nt
/usr/bin/blast_db_add.sh wgs
/usr/bin/blast_db_add.sh all_contig
/usr/bin/blast_db_add.sh patnt
/usr/bin/blast_db_add.sh pdbnt
/usr/bin/blast_db_add.sh human_genomic
/usr/bin/blast_db_add.sh other_genomic
/usr/bin/blast_db_add.sh refseq_genomic
/usr/bin/blast_db_add.sh refseq_rna

# Protein databases
echo "Put these in blast_p.loc"
/usr/bin/blast_db_add.sh nr
/usr/bin/blast_db_add.sh env_nr
/usr/bin/blast_db_add.sh swissprot
/usr/bin/blast_db_add.sh refseq_protein
/usr/bin/blast_db_add.sh pdbaa
/usr/bin/blast_db_add.sh pataa

# Domain databases
echo "Put these in blast_d.loc"
/usr/bin/blast_db_add.sh cdd_delta
