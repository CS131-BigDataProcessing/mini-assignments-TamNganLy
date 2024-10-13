#!/bin/bash

file_name=$1
num_of_col=$2

# Handle triling spaces/new lines.
sed 's/[[:space:]]\+$//' $1 > cleandata.csv

# Identify missing values
missing_rows=$(awk -F',' 'NF < $2' cleandata.csv | wc -l)

# If there are missing values, loop through each column and replace missing value by 'NA'
if [ $missing_rows -gt 0 ]; then
	awk -F',' -v OFS=',' '{
		for (i = 1; i <= NF; i++) {
			if ($i == "") $i = "NA";
		}
		print $0
	}' cleandata.csv > temp.csv && mv temp.csv cleandata.csv
fi

# Remove duplicate
sort -t',' -k 1 cleandata.csv | uniq > unique_data.csv


