"""
Coded by A.M. ALMARUFUZZAMAN from North South University | ID#1420469042 | CSE425 | Faculty: Dr. Kamruddin Nur | Spring 2019
"""
import csv
import os
import sys

def open_file():
	with open("air_quality_Nov2017.csv", 'r') as file: # Opening the csv file (Dataset) with read (r) mode
	
		file_reader = csv.reader(file) # Keeping all contents to a variable named file
		attributes = next(file_reader)
		data_list = []

		rows = 0

		for row in file_reader:
			if len(row) != 0:
				data_list  = data_list + [row]
				rows += 1

		for i in range(rows):
			if data_list[i][0] == "Barcelona - GrÃ\xa0cia":
				data_list[i][0] = "Barcelona - Gràcia"

	file.close()

	return file_reader, attributes, data_list, rows

def search_answers():
	file_reader, attributes, data_list, rows = open_file()

	sta_list = []

	for line in data_list:
		if len(line) != 0:
			sta_list = sta_list + [line[0]]

	sta_list = list(dict.fromkeys(sta_list))

	city = []
	station_list = []

	for i in range(len(sta_list)):
		new = sta_list[i].split()
		new1 = new[2]
		if len(new) > 3:
			new1 = new1 +" "+ new[3]
		city = city + [new[0]]
		station_list = station_list + [new1]

	city = list(dict.fromkeys(city))
	city = ', '.join(city)

	stations_ans_1 = "\nThere are total " + str(len(station_list)) + " " + attributes[0] + " in " + city + ".\nAnd those Stations are: " + ", ".join(station_list) + " from " + city + "."

	return stations_ans_1, station_list, city, sta_list

def bottom(task):
	message = "\n\n----- Type 0 to Go back to " + task + " related Query Menu. -----\n----- Type 1 to Go back to Main Menu. -----\n----- Or Type anything to terminate.-----\n\nType Option Here: "
	answer = int(input(message))
	if(answer == 0):
		os.system('cls')

		if task == "Stations":
			station_menu()
		elif task == "Air":
			air_menu()
		elif task == "O3":
			o3_menu()
		elif task == "NO2":
			no2_menu()
		elif task == "PM10":
			pm10_menu()
		elif task == "Other":
			other_menu()
	elif(answer == 1):
		os.system('cls')

		main_menu()
	else:
		sys.exit("Program Terminated")

def station_menu():
	task = "Stations"
	file_reader, attributes, data_list, rows = open_file()
	stations_ans_1, station_list, city, sta_list = search_answers()
	go_back = "\n----- Type 0 to Go Back to Main Menu. -----\n"

	station_menu_ = "\n----- Stations related Query. -----\n\n"
	station_menu_0 = "Query Options: \n\n"
	station_menu_1 = "How many Stations are there? And What are those?\n"
	station_menu_2 = "Enter a Station name for Checking that Station's existance and for all related data.\n"
	station_menu_3 = "Enter a existing Station name for Checking that Station's Longitude and Latitude.\n"

	print(station_menu_, station_menu_0, "Type 1 to query about -",station_menu_1, "Type 2 to query about -", station_menu_2, "Type 3 to query about -", station_menu_3, go_back)

	query_station = int(input("----- Here, Type for query. -----\n\nQuery Input: "))

	if query_station == 1:
		os.system('cls')

		print("QUERY: ", station_menu_1)
		print("Answer: ", stations_ans_1)
		bottom(task)

	elif query_station == 2:
		os.system('cls')

		print("QUERY: ", station_menu_2)
		sta_name = input("Answer: \nEnter a Station Name: ")
		
		sta_name = sta_name.lower()

		sta_name = sta_name.split()
		for i in range(len(sta_name)):
			sta_name[i] = sta_name[i].capitalize() 
		sta_name = ' '.join(sta_name)

		j = -1
		
		for i in range(0,len(station_list)):
			if sta_name == station_list[i]:
				j = i

		for i in range(0,len(sta_list)):
			if sta_name == sta_list[i]:
				j = i

		if j == -1:
			print("The Station named - '",sta_name,"' is not found in the file.\nTry again.\n")
			station_menu()
		if j > -1:
			print("\n", sta_name, "is present at the list.\n\nAnd the Station -", sta_name,"- Releted Data Rows are: \n")
			total = 0

			for i in range(len(data_list)):
				if sta_list[j] == data_list[i][0]:
					total += 1
					print(total," - ", data_list[i])
			print("\n\nTotal Data rows for ", sta_name, "Station is = ", total)
			bottom(task)

	elif query_station == 3:
		os.system('cls')

		print("QUERY: ", station_menu_3)
		sta_name = input("Answer: \nEnter a Station Name: ")
		
		sta_name = sta_name.lower()

		sta_name = sta_name.split()
		for i in range(len(sta_name)):
			sta_name[i] = sta_name[i].capitalize() 
		sta_name = ' '.join(sta_name)

		j = -1
		
		for i in range(0,len(station_list)):
			if sta_name == station_list[i]:
				j = i

		for i in range(0,len(sta_list)):
			if sta_name == sta_list[i]:
				j = i

		if j == -1:
			print("The Station named - '",sta_name,"' is not found in the file.\nTry again.\n")
			station_menu()
		if j > -1:
			longitude = data_list[j][2]
			latitude = data_list[j][3]
			print("\n", sta_name, "is present at the list.\n\nAnd the Station's Longitude is = ", longitude, "& the Latitude is = ", latitude,"\n")
			bottom(task)

	elif query_station == 0:
		os.system('cls')

		print("\n----- Returned at Main Menu. -----\n\n")

		main_menu()
	elif query_station == 9:
		os.system('cls')
		
		sys.exit("Program Terminated")
	else:
		os.system('cls')

		print("\n----- Invalid Query Input. -----\n\n----- Please Type again. -----\n\n")
		station_menu()

def quality(item, var):
	file_reader, attributes, data_list, rows = open_file()
	stations_ans_1, station_list, city, sta_list = search_answers()

	for i in range(len(attributes)):
		if item == attributes[i]:
			j = i

	var_list_for_item = []
	for i in range(len(data_list)):
		if data_list[i][j] == var:
			var_list_for_item = var_list_for_item + [data_list[i]]

	city_new = city + " - "

	print("There are total of", len(var_list_for_item), "results found for", var, item,".\n\n")

	if len(var_list_for_item) != 0:
		print("Those are:\n")
		for i in range(len(var_list_for_item)):
			print((i+1),".", var, item, "for", var_list_for_item[i][0].replace(city_new, ""), "Station of", city,"was Generated at -", var_list_for_item[i][13])

def air_menu():
	task = "Air"
	go_back = "\n----- Type 0 to Go Back to Main Menu. -----\n"

	air_menu_ = "\n\n----- Air related Query. -----\n\n"
	air_menu_0 = "Query Options: \n\n"
	air_menu_1 = "Stations list with Generated Date and time for the Good Air Quality.\n"
	air_menu_2 = "Stations list with Generated Date and time for the Moderate Air Quality.\n"

	print(air_menu_, air_menu_0, "Type 1 to query about - ", air_menu_1, "Type 2 to query about - ", air_menu_2, go_back)

	query_air = int(input("----- Here, Type for query. -----\n\nQuery Input: "))

	item = "Air Quality"

	if query_air == 1:
		os.system('cls')

		print("QUERY: ", air_menu_1)
		print("Answer: ")

		var = "Good"
		quality(item, var)
		bottom(task)

	elif query_air == 2:
		os.system('cls')

		print("QUERY: ", air_menu_2)
		print("Answer: ")

		var = "Moderate"
		quality(item, var)
		bottom(task)

	elif query_air == 0:
		os.system('cls')

		print("\n----- Returned at Main Menu. -----\n\n")

		main_menu()
	elif query_air == 9:
		os.system('cls')
		
		sys.exit("Program Terminated")
	else:
		os.system('cls')

		print("\n----- Invalid Query Input. -----\n\n----- Please Type again. -----\n\n")
		air_menu()

def values_(var, find):
	file_reader, attributes, data_list, rows = open_file()
	stations_ans_1, station_list, city, sta_list = search_answers()

	for i in range(len(attributes)):
		if var == attributes[i]:
			j = i

	value_for_var = []

	for i in range(len(data_list)):
		if data_list[i][j] != "NA":
			value_for_var = value_for_var + [data_list[i]]

	value_list = []
	for line in value_for_var:
		if len(line) != 0:
			value_list = value_list + [line[j]]

	if find == "Maximum":
		get_value = max(value_list)
	elif find == "Minimum":
		get_value = min(value_list)

	print("The", find, var, "is = ", get_value, ".")
	value_station = []
	for i in range(len(value_for_var)):
		if value_for_var[i][j] == get_value:
			value_station = value_station + [value_for_var[i]]

	city_new = city + " - "

	l = 0

	print("The list of", find, var, "contained Stations are:-\n")
	for i in range(len(value_station)):
		l += 1
		print(l,". The", find, var, get_value, "is from", value_station[i][0].replace(city_new, ""), "Station of", city,"and was Generated at -", value_station[i][13])
	print("\n\nTotal of ", l, " results found for the", find,"of", var, "Search.")

def o3_menu():
	task = "O3"
	go_back = "\n----- Type 0 to Go Back to Main Menu. -----\n"

	o3_menu_ = "\n\n----- O3 (tropospheric Ozone) related Query. -----\n\n"
	o3_menu_0 = "Query Options: \n\n"
	o3_menu_1 = "Stations list with Generated Date and time for the Good O3 (tropospheric Ozone) Quality.\n"
	o3_menu_2 = "Stations list with Generated Date and time for the Moderate O3 (tropospheric Ozone) Quality.\n"
	o3_menu_3 = "What is the Maximum value for O3 (tropospheric Ozone) and which station(s) has that?\n"
	o3_menu_4 = "What is the Minimum value for O3 (tropospheric Ozone) and which station(s) has that?\n"

	print(o3_menu_, o3_menu_0, "Type 1 to query about - ", o3_menu_1, "Type 2 to query about - ", o3_menu_2, "Type 3 to query about - ", o3_menu_3, "Type 4 to query about - ", o3_menu_4, go_back)

	query_o3 = int(input("----- Here, Type for query. -----\n\nQuery Input: "))

	item = "O3 Quality"

	if query_o3 == 1:
		os.system('cls')

		print("QUERY: ", o3_menu_1)
		print("Answer: ")

		var = "Good"
		quality(item, var)
		bottom(task)

	elif query_o3 == 2:
		os.system('cls')

		print("QUERY: ", o3_menu_2)
		print("Answer: ")

		var = "Moderate"
		quality(item, var)
		bottom(task)

	elif query_o3 == 3:
		os.system('cls')

		print("QUERY: ", o3_menu_3)
		print("Answer: ")

		var = "O3 Value"
		find = "Maximum"
		values_(var, find)
		bottom(task)

	elif query_o3 == 4:
		os.system('cls')

		print("QUERY: ", o3_menu_4)
		print("Answer: ")

		var = "O3 Value"
		find = "Minimum"
		values_(var, find)
		bottom(task)

	elif query_o3 == 0:
		os.system('cls')

		print("\n----- Returned at Main Menu. -----\n\n")

		main_menu()
	elif query_o3 == 9:
		os.system('cls')
		
		sys.exit("Program Terminated")
	else:
		os.system('cls')

		print("\n----- Invalid Query Input. -----\n\n----- Please Type again. -----\n\n")
		o3_menu()

def no2_menu():
	task = "NO2"
	go_back = "\n----- Type 0 to Go Back to Main Menu. -----\n"

	no2_menu_ = "\n\n----- NO2 (Nitrogen dioxide) related Query. -----\n\n"
	no2_menu_0 = "Query Options: \n\n"
	no2_menu_1 = "Stations list with Generated Date and time for the Good NO2 (Nitrogen dioxide) Quality.\n"
	no2_menu_2 = "Stations list with Generated Date and time for the Moderate NO2 (Nitrogen dioxide) Quality.\n"
	no2_menu_3 = "What is the Maximum value for NO2 (Nitrogen dioxide) and which station(s) has that?\n"
	no2_menu_4 = "What is the Minimum value for NO2 (Nitrogen dioxide) and which station(s) has that?\n"

	print(no2_menu_, no2_menu_0, "Type 1 to query about - ", no2_menu_1, "Type 2 to query about - ", no2_menu_2, "Type 3 to query about - ", no2_menu_3, "Type 4 to query about - ", no2_menu_4, go_back)

	query_no2 = int(input("----- Here, Type for query. -----\n\nQuery Input: "))

	item = "NO2 Quality"

	if query_no2 == 1:
		os.system('cls')

		print("QUERY: ", no2_menu_1)
		print("Answer: ")

		var = "Good"
		quality(item, var)
		bottom(task)

	elif query_no2 == 2:
		os.system('cls')

		print("QUERY: ", no2_menu_2)
		print("Answer: ")

		var = "Moderate"
		quality(item, var)
		bottom(task)

	elif query_no2 == 3:
		os.system('cls')

		print("QUERY: ", no2_menu_3)
		print("Answer: ")

		var = "NO2 Value"
		find = "Maximum"
		values_(var, find)
		bottom(task)

	elif query_no2 == 4:
		os.system('cls')

		print("QUERY: ", no2_menu_4)
		print("Answer: ")

		var = "NO2 Value"
		find = "Minimum"
		values_(var, find)
		bottom(task)

	elif query_no2 == 0:
		os.system('cls')

		print("\n----- Returned at Main Menu. -----\n\n")

		main_menu()
	elif query_no2 == 9:
		os.system('cls')
		
		sys.exit("Program Terminated")
	else:
		os.system('cls')

		print("\n----- Invalid Query Input. -----\n\n----- Please Type again. -----\n\n")
		no2_menu()

def pm10_menu():
	task = "PM10"
	go_back = "\n----- Type 0 to Go Back to Main Menu. -----\n"

	pm10_menu_ = "\n\n----- PM10 (Suspended particles) related Query. -----\n\n"
	pm10_menu_0 = "Query Options: \n\n"
	pm10_menu_1 = "Stations list with Generated Date and time for the Good PM10 (Suspended particles) Quality.\n"
	pm10_menu_2 = "Stations list with Generated Date and time for the Moderate PM10 (Suspended particles) Quality.\n"
	pm10_menu_3 = "What is the Maximum value for PM10 (Suspended particles) and which station(s) has that?\n"
	pm10_menu_4 = "What is the Minimum value for PM10 (Suspended particles) and which station(s) has that?\n"

	print(pm10_menu_, pm10_menu_0, "Type 1 to query about - ", pm10_menu_1, "Type 2 to query about - ", pm10_menu_2, "Type 3 to query about - ", pm10_menu_3, "Type 4 to query about - ", pm10_menu_4, go_back)

	query_pm10 = int(input("----- Here, Type for query. -----\n\nQuery Input: "))

	item = "PM10 Quality"

	if query_pm10 == 1:
		os.system('cls')

		var = "Good"
		quality(item, var)
		bottom(task)

	elif query_pm10 == 2:
		os.system('cls')

		var = "Moderate"
		quality(item, var)
		bottom(task)

	elif query_pm10 == 3:
		os.system('cls')

		print("QUERY: ", pm10_menu_3)
		print("Answer: ")

		var = "PM10 Value"
		find = "Maximum"
		values_(var, find)
		bottom(task)

	elif query_pm10 == 4:
		os.system('cls')

		print("QUERY: ", pm10_menu_4)
		print("Answer: ")

		var = "PM10 Value"
		find = "Minimum"
		values_(var, find)
		bottom(task)

	elif query_pm10 == 0:
		os.system('cls')

		print("\n----- Returned at Main Menu. -----\n\n")

		main_menu()
	elif query_pm10 == 9:
		os.system('cls')
		
		sys.exit("Program Terminated")
	else:
		os.system('cls')

		print("\n----- Invalid Query Input. -----\n\n----- Please Type again. -----\n\n")
		no2_menu()

def other_menu():
	task = "Other"
	file_reader, attributes, data_list, rows = open_file()

	go_back = "\n----- Type 0 to Go Back to Main Menu. -----\n"

	other_menu_ = "\n\n----- Other Queries. -----\n\n"
	other_menu_0 = "Query Options: \n\n"
	other_menu_1 = "How many data rows has the air_quality_Nov2017.csv file?\n"
	other_menu_2 = "How many data attributes has the air_quality_Nov2017.csv file? And what are those?\n"
	other_menu_3 = "When is the data file 'air_quality_Nov2017.csv' Generated?\n"

	print(other_menu_, other_menu_0, "Type 1 to query about - ", other_menu_1, "Type 2 to query about - ", other_menu_2, "Type 3 to query about - ", other_menu_3, go_back)

	query_other = int(input("----- Here, Type for query. -----\n\nQuery Input: "))

	if query_other == 1:
		os.system('cls')

		print("QUERY: ", other_menu_1)
		print("Answer: ")

		print("\nThere are total of ", (rows-1), " Data Rows without Attributes.")
		bottom(task)
		
	elif query_other == 2:
		os.system('cls')

		print("QUERY: ", other_menu_2)
		print("Answer: ")

		print("\nThere are total of ", len(attributes), " Attributes.\nAnd those are:-\n")
		for i in range(len(attributes)):
			print((i+1), ".", attributes[i])
		print("\n")
		bottom(task)
		
	elif query_other == 3:
		os.system('cls')

		print("QUERY: ", other_menu_3)
		print("Answer: ")

		dates = []
		for line in data_list:
			if len(line) != 0:
				dates = dates + [line[13]]

		generate_date = []
		for i in range(len(dates)):
			new = dates[i].split()
			generate_date = generate_date + [new[0]]

		generate_date = list(dict.fromkeys(generate_date))

		out_ln = "The whole Data Set was Generated at "
		generate_date = ", ".join(generate_date)

		if len(generate_date) > 1 :
			out_ln = out_ln + "these dates -"
		else:
			out_ln = out_ln + "this date -"
		
		print(out_ln, generate_date)

		bottom(task)
		
	elif query_other == 0:
		os.system('cls')

		print("\n----- Returned at Main Menu. -----\n\n")

		main_menu()
	elif query_other == 9:
		os.system('cls')
		
		sys.exit("Program Terminated")
	else:
		os.system('cls')

		print("\n----- Invalid Query Input. -----\n\n----- Please Type again. -----\n\n")
		no2_menu()

def main_menu():
	main_menu_ = "----- Main Menu. -----\n\nQuery Options: \n\n"
	main_menu_1 = "Type 1 for Stations related Query.\n"
	main_menu_2 = "Type 2 for Air related Query.\n"
	main_menu_3 = "Type 3 for O3 (tropospheric Ozone) related Query.\n"
	main_menu_4 = "Type 4 for NO2 (Nitrogen dioxide) related Query.\n"
	main_menu_5 = "Type 5 for PM10 (Suspended particles) related Query\n"
	main_menu_6 = "Type 6 for Other Queries.\n"
	ext = "\n----- Or Type 0 to Terminate. -----\n\n"

	print(main_menu_, main_menu_1, main_menu_2, main_menu_3, main_menu_4, main_menu_5, main_menu_6, ext)

	query_main = int(input("----- Here, Type for query. -----\n\nQuery Input: "))

	if query_main == 1:
		os.system('cls')

		station_menu()
	elif query_main == 2:
		os.system('cls')
		
		air_menu()
	elif query_main == 3:
		os.system('cls')
		
		o3_menu()
	elif query_main == 4:
		os.system('cls')
		
		no2_menu()
	elif query_main == 5:
		os.system('cls')
		
		pm10_menu()
	elif query_main == 6:
		os.system('cls')
		
		other_menu()
	elif query_main == 0:
		os.system('cls')
		
		sys.exit("Program Terminated")
	else:
		os.system('cls')

		print("\n----- Invalid Query Input. -----\n\n----- Please Type again. -----\n\n")
		main_menu()

def main():
	os.system('cls')
	print("Lets Search something!!\n")
	open_file()
	main_menu()

	search_answers()

print("Initializing .csv type File Search Program ...")
main()
os.system("pause")
