#/usr/bin/bash
filename=$1
test_file=$2
#test_file2="twitch_test2.log"
#test_file3="twitch_test3.log"

#Displays all data containing 'PRIVMSG' string in column 3.
#cat $filename | awk '$3 == "PRIVMSG"' > $test_file1

#Subsitute column 1, 2 and 3 with nothing. (>>, gibberish, PRIVMSG)
#awk '{$1=""; $2=""; $3=""; $4=""; sub("  ", " "); print}' $test_file1 > $test_file2

#Deletes channel name and colon.
#cat $test_file2 | sed -r 's/^.{4}//' > $test_file3

#combined all three into a one line prints out to $test_file1
cat $filename | awk '$3 == "PRIVMSG"' | awk '{$1=""; $2=""; $3=""; $4=""; sub("  ", " "); print}' | sed -r 's/^.{4}//' > $test_file