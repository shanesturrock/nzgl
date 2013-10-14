#!/bin/bash

set -e
path=`pwd`
tooldata_path='/home/galaxy/galaxy-dist/tool-data/'

if [ $# -lt 2 ]; then
	echo "$0 <loc_file> <dbname>"
	exit 1
fi

loc_file="${tooldata_path}${1}"
# echo $loc_file
db="${2}"

databaseline=`blastdbcmd -info -db ${db} | grep "Database"`
database=${databaseline#"Database: "}
dateline=`blastdbcmd -info -db ${db} | grep "Date"`
date=${dateline#"Date: "}

declare -a array
array=(${date// / })
month=${array[0]}
day=${array[1]%?}
year=${array[2]}

name="${db}_${day}_${month}_${year}"

database_check="${name}	${db}"
database_line="${name}\t${db} (${database}) ${day} ${month} ${year}\t${path}/${db}"
# echo "Checking ${loc_file} for ${database_check}"
# Search for matching database and delete if already known
if grep "${database_check}" ${loc_file} > /dev/null
then
  # Database is already known so delete previous matching line 
  sed -i "/${database_check}/d" ${loc_file}
fi
# Add database to top of file so they're always in most recent order
sed -i "1i$database_line" $loc_file
