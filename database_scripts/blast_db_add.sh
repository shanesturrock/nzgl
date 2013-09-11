#!/bin/bash

set -e
path=`pwd`
tooldata_path='/home/galaxy/galaxy-dist/tool-data'

if [ $# -lt 1 ]; then
	echo "$0 <dbname>"
	exit 1
fi

db="${1}"

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
echo -e "${name}\t${db} (${database}) ${day} ${month} ${year}\t${path}/${db}"
