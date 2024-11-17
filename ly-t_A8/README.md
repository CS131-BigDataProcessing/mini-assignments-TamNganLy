# A8 Directory  

## Files  
- **preprocessing.sh**: A shell script that automates the cleaning and preprocessing of data. It performs tasks: removing missing value, removing duplicate entries, and handling outliers.  
- **about_script.txt**: A document explaining the reasoning behind the tasks implemented in `preprocessing.sh` and listing the names of the group members.  

## How to Run  

Run the script using the following syntax:  
```bash  
sh preprocessing.sh <filename> <number_of_columns> <outlier_column>  
```
Example:
```bash 
sh preprocessing.sh AB_NYC_2019.csv 16 10  
```
