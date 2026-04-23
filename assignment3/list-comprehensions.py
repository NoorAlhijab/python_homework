# Task 3

import csv
new_list = []
with open('../csv/employees.csv', 'r') as file:
    read_content = csv.reader(file)
    for row in read_content:
        new_list.append(row)
    # To create a list of employee full names, skipping header row
    employee_names_list = [row[1] + " " + row[2] for row in new_list[1:]]   
    #print(employee_names_list)

    # To create list of employee names that contain the letter 'e'
    employee_names_with_e = [name for name in employee_names_list if 'e' in name.lower()]
    #print(employee_names_with_e)

