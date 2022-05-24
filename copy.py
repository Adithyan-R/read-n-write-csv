import csv

try:
	def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
		
		"""
		Inputs:
		filename   - name of CSV file
		table      - list of dictionaries containing the table to write
		fieldnames - list of strings corresponding to the field names in order
		separator  - character that separates fields
		quote      - character used to optionally quote fields
		Output:
		Writes the table to a CSV file with the name filename, using the
		given fieldnames.  The CSV file should use the given separator and
		quote characters.  All non-numeric fields will be quoted.
		"""
		with open(filename, 'w', newline='') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
											delimiter=separator,
											quotechar=quote,
											quoting=csv.QUOTE_NONNUMERIC)        
			writer.writeheader()
			for value in table:
				writer.writerow({fieldnames[0]: value[fieldnames[0]],
								fieldnames[1]: value[fieldnames[1]],
								})            


except FileNotFoundError:
	msg='FileNotFoundError'

finally:
	print(write_csv_from_list_dict('table1.csv', [{'col1': 'data7', 'col2': 'data8'}, \
													{'col1': 'data9', 'col2': 'data10'}, \
												], \
													['col1', 'col2'], ',', '"'))



try:
	def read_csv_fieldnames(filename, separator, quote):
		"""
		Inputs:
		filename  - name of CSV file
		separator - character that separates fields
		quote     - character used to optionally quote fields
		Ouput:
		A list of strings corresponding to the field names in
		the given CSV file.
		"""
    
		with open(filename, newline='') as csvfile:
				
			reader = csv.DictReader(csvfile,
									delimiter=separator,
									quotechar=quote)
			
			return reader.fieldnames

except FileNotFoundError:
	msg= 'File does not exist'
	print(msg)

finally:
	print(read_csv_fieldnames("table1.csv", ",", ";"))



try:
	def read_csv_as_list_dict(filename, separator, quote):
		"""
		Inputs:
		filename  - name of CSV file
		separator - character that separates fields
		quote     - character used to optionally quote fields
		Output:
		Returns a list of dictionaries where each item in the list
		corresponds to a row in the CSV file.  The dictionaries in the
		list map the field names to the field values for that row.
		"""   
    
		list_of_values = []
		
		with open(filename, newline='') as csvfile:
			reader = csv.DictReader(csvfile,
									delimiter=separator,
									quotechar=quote)
			for row in reader:
				values = {}
				for name in row:
					values[name] = row[name]
				list_of_values.append(values)
				
		return list_of_values


except FileNotFoundError:
	msg='File does not exist'
	print(msg)


finally:
	print(read_csv_as_list_dict("table1.csv", ",", ";"))
