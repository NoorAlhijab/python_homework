import csv
import os
import custom_module
from datetime import datetime

# Task 2: Read a CSV File
def read_employees():
    new_dict = {}
    new_list = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            read_content = csv.reader(file)
            # To get the header row
            header = next(read_content)
            new_dict["fields"] = header
            # To get the rest of rows
            for row in read_content:
                new_list.append(row)
            new_dict['rows']=new_list
        return new_dict
    except Exception as e:
        print(e)

employees = read_employees()
## print(employees)

## Task 3: Find the Column Index
def column_index(column_name):
   index = employees['fields'].index(column_name)
   return index

employee_id_column = column_index('employee_id')
## print(employee_id_column)

# Task 4: Find the Employee First Name
def  first_name(row_number):
    # Call column_index function to get frist name index
    first_name_column = column_index("first_name")
    # Get the row using row number
    row = employees['rows'][row_number]
    # Get the first name from that row
    value = row[first_name_column]
    return value
first_name(0)

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    #print(matches)
    return matches
employee_find(16)

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    # print(matches)
    return matches
employee_find_2(1)

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key = lambda row: row[last_name_column])
    return employees["rows"]   
sort_by_last_name()
## print(employees)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    new_dict ={}
    # Using range start from index 1 to Skip employee_id
    for i in range(1, len(row)):
       #print(row[i])
       key = employees['fields'][i]
       value = row[i]
       new_dict[key]=value
    #print (new_dict)
    return new_dict
emp_dict = employee_dict([1,"Cindy","Wade","+222 656-486-3727"])
#print(emp_dict)

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    all_emp_dict = {}
    for row in employees['rows']:
        #print(row[0])
        key = row[0]
        value = employee_dict(row)
        #print(employee_dict(row))
        all_emp_dict[key] = value
        #print(all_emp_dict)
    return all_emp_dict  
all_employess = all_employees_dict()
#print(all_employess)

#Task 10: Use the os Module
def get_this_value():
    value = os.getenv("THISVALUE")
    #print(value)
    return value
get_this_value()


#Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret("MyNewSecret")
#print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_file(file_path):
    data_dict = {}
    rows = []
    try:
        with open(file_path, 'r') as file:
            read_content = csv.reader(file)
            header = next(read_content)
            data_dict['fields'] = header
            for row in read_content:
                # Convert each row to tuple
                rows.append(tuple(row))
            data_dict['rows'] = rows
        return data_dict
    except Exception as e:
        print(e)

def read_minutes():
    minutes1 = read_file('../csv/minutes1.csv')
    minutes2 = read_file('../csv/minutes2.csv')
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
#print(minutes1)
#print(minutes2)

#Task 13: Create minutes_set
def create_minutes_set():
    minutes_set1 = set(minutes1['rows'])
    minutes_set2 = set(minutes2['rows'])
    minutes_set = minutes_set1.union(minutes_set2)
    return minutes_set

minutes_set = create_minutes_set()
#print(minutes_set)

#Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    convert_datetime = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return convert_datetime
minutes_list= create_minutes_list()
#print(minutes_list)

#Task 15: Write Out Sorted List
def write_sorted_list():
    # To sort minutes list by datetime
    minutes_list.sort(key=lambda x: x[1])
    convert_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    try:
        with open('./minutes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1['fields'])
            writer.writerows(convert_list)
        return convert_list
    except Exception as e:
        print(e)    
sorted_date_list = write_sorted_list()
#print(sorted_date_list)













