#!/usr/bin/env sh

# file_csv:
# First Name,Last Name,E-mail Address,Home Address,Mobile Phone
# SKP002,,,,3218529944
# SKP006,,,,3218529947
# SKP106,,,,3218529951
# SKP010,,,,3113360932
# SKP015,,,,3113384435
# SKP005,,,,3137643171


file_csv=$1

for line in $(cat $1|awk -F',' '$5 ~ /^[0-9]/ {print $1","$5}'); do
	id=$(echo $line|awk -F',' '{print $1}')
	number=$(echo $line|awk -F',' '{print $2}')
	echo 'ID: '$id' - NUMBER: '$number
	
	psql -d rastree -c "UPDATE gps SET number_sim='$number' WHERE name='$id'"
done
