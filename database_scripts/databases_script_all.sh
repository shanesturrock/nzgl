#!/bin/bash

DB_ROOT=/databases/indexes
DB_SETUP=$DB_ROOT/db_setup.sh

# Drosphila
cd $DB_ROOT/dm3/seq
$DB_SETUP dm3.2bit "D. melanogaster Apr. 2006 (BDGP R5/dm3): dm3"

# Human
cd $DB_ROOT/hg18/seq
$DB_SETUP hg18.2bit "Human (Homo sapiens): hg18"
cd $DB_ROOT/hg19/seq
$DB_SETUP hg19.2bit "Human (Homo sapiens): hg19"

# Mouse
cd $DB_ROOT/mm8/seq
$DB_SETUP mm8.2bit "Mouse (Mus musculus): mm8"
cd $DB_ROOT/mm9/seq
$DB_SETUP mm9.2bit "Mouse (Mus musculus): mm9"
cd $DB_ROOT/mm10/seq
$DB_SETUP mm10.2bit "Mouse (Mus musculus): mm10"

# Rat
cd $DB_ROOT/rn4/seq
$DB_SETUP rn4.2bit "Rat (Rattus norvegicus): rn4"
cd $DB_ROOT/rn5/seq
$DB_SETUP rn5.2bit "Rat (Rattus norvegicus): rn5"

# Arabidopsis
cd $DB_ROOT/Araly1/seq
$DB_SETUP Araly1.2bit "Arabidopsis lyrata: Araly1"
cd $DB_ROOT/Arabidopsis_thaliana_TAIR10/seq
$DB_SETUP Arabidopsis_thaliana_TAIR10.2bit "Mouse-ear Cress (Arabidopsis thaliana): Arabidopsis_thaliana_TAIR10"
cd $DB_ROOT/Arabidopsis_thaliana_TAIR9/seq
$DB_SETUP Arabidopsis_thaliana_TAIR9.2bit "Mouse-ear Cress (Arabidopsis thaliana): Arabidopsis_thaliana_TAIR9"

# E.coli
cd $DB_ROOT/eschColi_APEC_O1/seq
$DB_SETUP eschColi_APEC_O1.2bit "Escherichia coli (APEC O1): eschColi_APEC_O1"
cd $DB_ROOT/eschColi_CFT073/seq
$DB_SETUP eschColi_CFT073.2bit "Escherichia coli (CFT073): eschColi_CFT073"
cd $DB_ROOT/eschColi_K12/seq
$DB_SETUP eschColi_K12.2bit "Escherichia coli (str. K12 substr. MG1655): eschColi_K12"
cd $DB_ROOT/eschColi_EC4115/seq
$DB_SETUP eschColi_EC4115.2bit "Escherichia coli (str. O157H7 substr. EC4115): eschColi_EC4115"

cd $DB_ROOT/danRer7/seq
$DB_SETUP danRer7.2bit "Zebrafish (Danio rerio): danRer7"

cd $DB_ROOT/sacCer3/seq
$DB_SETUP sacCer3.2bit "Yeast (Saccharomyces cerevisiae): sacCer3"

cd $DB_ROOT/galGal4/seq
$DB_SETUP galGal4.2bit "Chicken (Gallus gallus): galGal4"

cd $DB_ROOT/ce10/seq
$DB_SETUP ce10.2bit "Caenorhabditis elegans: ce10"

cd $DB_ROOT/oviAri1/seq
$DB_SETUP oviAri1.2bit "Sheep (Ovis aries): oviAri1"

cd $DB_ROOT/Methanobrevibacter_smithii_NC_009515-1/seq
$DB_SETUP Methanobrevibacter_smithii_NC_009515-1.2bit "Methanobrevibacter smithii ATCC 35061 (NC_009515.1): Methanobrevibacter_smithii_NC_009515-1"

cd $DB_ROOT/Mycobacterium_tuberculosis_NC_000962-3/seq
$DB_SETUP Mycobacterium_tuberculosis_NC_000962-3.2bit "Mycobacterium tuberculosis H37Rv (NC_000962.3): Mycobacterium_tuberculosis_NC_000962-3"

cd $DB_ROOT/Enterobacteria_phage_NC_001422-1/seq
$DB_SETUP Enterobacteria_phage_NC_001422-1.2bit "Enterobacteria phage phiX174 (NC_001422.1): Enterobacteria_phage_NC_001422-1"

cd $DB_ROOT/Sulfolobus_islandicus_NC_012588-1/seq
$DB_SETUP Sulfolobus_islandicus_NC_012588-1.2bit "Sulfolobus islandicus M.14.25 (NC_012588.1): Sulfolobus_islandicus_NC_012588-1"

# Cow
cd $DB_ROOT/bosTau7/seq
$DB_SETUP bosTau7.2bit "Cow (Bos taurus): bosTau7"

# Chicker release 72
cd $DB_ROOT/galGal4_72/seq
$DB_SETUP galGal4_72.2bit "Chicken (Gallus gallus - release 72): Gallus_gallus.Galgal4.72"

