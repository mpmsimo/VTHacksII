#/usr/bin/bash
#usage format_xchat_log.sh raw_log.log file_out.txt

log_file=$1
parsed_data=$2

#Displays all lines of file...
#which contains the string "PRIVMSG" string in column 3.
#Then subsitutes columns 1, 2 and 3 with nothing an empty string.
#Afterwards deletes the first four characters from all lines in the file.

cat $log_file | awk '$3 == "PRIVMSG"' | awk '{$1=""; $2=""; $3=""; $4=""; sub("  ", " "); print}' | sed -r 's/^.{4}//' > $parsed_data