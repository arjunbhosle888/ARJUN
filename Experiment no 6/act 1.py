#Store daily expenses in a file and calculate total monthly expense.
Created on Mon Mar 23 15:14:03 2026
@author: arjun bhosale
file_name = "daily_expenses.txt"
with open(file_name, "w") as file:


file.write("Daily Expenses (in Rs): \n")
file.write("100\n")



file.write("250\n")



file.write("300\n")
file.write("150\n")
file.write("200\n")



print(f"Data written to {file_name} successfully. \n")
print("Reading file content:")
with open(file_name, "r") as file:
content = file.read()

Daily Expenses (in Rs):

print(content)
with open(file_name, "a") as file
