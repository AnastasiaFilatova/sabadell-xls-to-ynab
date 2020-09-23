import os
import sys
import csv
import pandas as pd


fn = sys.argv[1]
print(fn)

excel_file = os.path.abspath(fn)

print('Provided budget file: {}'.format(excel_file))

budget_file = excel_file[:-4] + '.csv'
new_file_path = budget_file[:-4] + '-ynab' + '.csv'




def read_excel(excel_file, budget_file):

	df = pd.read_excel(excel_file)
	df.to_csv(budget_file, index=False)
	print('File converted to csv: {}'.format(budget_file))


def parse_csv_with_panda(budget_file):
	filtered_csv = pd.read_csv(budget_file, usecols=[0, 1, 5, 3], skiprows=[x for x in range(8)], parse_dates=[0])
	new_headers = {'F. Operativa': 'Date', 'Concepto': 'Payee', 'Referencia 1': 'Memo', 'Importe': 'Amount'}
	filtered_csv.rename(columns=new_headers, inplace=True)
	
	print('Parsed csv budget file')
	print('*******************************************************************************')
	print(filtered_csv)
	print('*******************************************************************************')
	return filtered_csv
	
	
def write_to_csv(budget_file, data, new_file_path):
	data.to_csv(new_file_path, index=False)
	print('Created file for ynab: {}'.format(new_file_path))

read_excel(excel_file, budget_file)

data = parse_csv_with_panda(budget_file)

write_to_csv(budget_file, data, new_file_path)