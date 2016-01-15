#!/bin/bash

function usage() {
	cat << EOF
Usage: ${0} [-r] -f <filename>

	-r Write report of deletions planned to send to Spark (Optional)
        -f File containing project IDs (Required)

<filename> contains a list of project IDs. The script will write out to
stdout and this can be redirected into a file to use as the deletion
script. Use the -r flag to change the output to just a list of deletions
of archive and active which can be sent to Spark for checking against
backups.
EOF
}

if [ $# -lt 2 ]; then
	usage
	exit 1
fi

REPORT=0
while getopts f:r flag; do
	case $flag in
		f) FILENAME=$OPTARG
		  ;;
		r) REPORT=1
		  ;;
		?)
		  usage
		  exit 1
		  ;;
	esac
done

PROJECTLIST="$FILENAME"
DATE=`date +%Y-%m-%d`
# echo $DATE
OUTPUT="delete_script_$DATE"
# echo $OUTPUT
DELETEDDIR="deleted_$DATE"
# echo $DELETEDDIR
if [ $REPORT -eq 0 ]; then
	echo "mkdir /active/deleted/$DELETEDDIR"
	echo "mkdir /archive/deleted/$DELETEDDIR"
fi

while read -r LINE
do
        # Get the project ID and convert to lowercase if necessary
	PROJECT=${LINE,,}
	# echo $PROJECT
	COMMAND=""
        if [ $REPORT -eq 0 ]; then
        	# Check archive, active, scratch and outgoing exist
        	if [ -d "/archive/$PROJECT" ]; then
			COMMAND="mv /archive/$PROJECT /archive/deleted/$DELETEDDIR/$PROJECT"
		fi
        	if [ -d "/active/$PROJECT" ]; then
			COMMAND="$COMMAND ; mv /active/$PROJECT /active/deleted/$DELETEDDIR/$PROJECT"
		fi
        	if [ -d "/scratch/$PROJECT" ]; then
			COMMAND="$COMMAND ; rm -rf /scratch/$PROJECT"
        	fi
        	if [ -d "/archive/outgoing/$PROJECT" ]; then
			COMMAND="$COMMAND ; rm -rf /archive/outgoing/$PROJECT"
        	fi
	else
        	if [ -d "/archive/$PROJECT" ]; then
			COMMAND="/archive/$PROJECT"
		fi
        	if [ -d "/active/$PROJECT" ]; then
			COMMAND="$COMMAND /active/$PROJECT"
		fi
        fi
        if [ ! -z "$COMMAND" ]; then 
		echo $COMMAND
	fi
done < $PROJECTLIST
