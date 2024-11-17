#!/bin/bash

file_name=$1
num_of_col=$2
outlier_col=$3

# Task 1: Identify missing values

# Handle trailing spaces/new lines.
awk -F, '{
    gsub(/^[[:space:]]+|[[:space:]]+$/, "", $0);
    gsub(/\t/, "", $0); # Remove tabs
    gsub(/\n/, "", $0); # Remove newlines
    print
}' "$file_name" > input_data.csv

# Identify missing values
awk -F, -v col=$2 'NF==col' input_data.csv > input_data1.csv



# Task 2: Remove rows with missing values

# If there are missing values, loop through each column and remove rows with missing values
awk -F',' -v OFS=',' '
{
	missing = 0;
	for (i=1; i<=NF; i++) {
		if ($i == "") {missing = 1; break}
    	}
	if (missing == 0) { print $0 };
}' input_data1.csv > clean_data.csv



# Task 3:  Remove duplicate

# Extract the header and store it temporarily
head -n 1 clean_data.csv > unique_data.csv

# Sort and remove duplicates from the remaining rows, then append to the file
tail -n +2 clean_data.csv | sort -t',' -k 1,1 | uniq >> unique_data.csv



# Task 4: Identifying and handling outliers

# Select the column that need to hande outliers
cut -d',' -f$outlier_col unique_data.csv | sort -nu > field_values.txt

# Calculate Q1, Q2, Q3
total_rows=$(wc -l < field_values.txt)

Q1=$(awk -v total="$total_rows" 'NR==int(total/4) {print; exit}' field_values.txt)
Q2=$(awk -v total="$total_rows" 'NR==int(total/2) {print; exit}' field_values.txt)
Q3=$(awk -v total="$total_rows" 'NR==int(total*3/4) {print; exit}' field_values.txt)

echo $Q1
echo $Q2
echo $Q3

# Calculate the IQR and determine the bounds for outliers
IQR=$(echo "$Q3 - $Q1" | bc)
lower_bound=$(echo "$Q1 - 1.5 * $IQR" | bc)
upper_bound=$(echo "$Q3 + 1.5 * $IQR" | bc)

echo $lower_bound
echo $upper_bound


# Replace outliers with Q2 (Median)
awk -F',' -v q2="$Q2" -v lb="$lower_bound" -v ub="$upper_bound" -v col="$outlier_col" '
{
    if ($col < lb || $col > ub) {
        $col = q2;
    }
    print $0;
}' OFS=',' unique_data.csv > final_output.csv

rm -f input_data.csv input_data1.csv clean_data.csv unique_data.csv field_values.txt

