#Sabadell xls to YNAB csv 
======
Python programm which converts xsl file with transactions from Sabadell bank to csv file and formats it for YNAB.
Check out YNAB formatting requirements here: https://docs.youneedabudget.com/article/921-formatting-csv-file

#How to use the programm
1. Clone the project
2. cd into the project folder
3. Export xls file with transactions from Sabadell bank  and save it in the following format: "DD-MM-YEAR.xls"
4. Run the programm:

...python3 csv_to_ynab.py <provide a path to xls file with transactions from Sabadell>

...Example:
 
...python3 csv_to_ynab.py ~/Documents/budget/17-09-2020.xls
   
5. Programm will save the file to the folder where xls file located but with a different name, in the following format "DD-MM-YEAR-ynab.csv"
6. Import saved file to the inab
