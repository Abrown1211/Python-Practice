import csv

searchType = input("Search by invoice id (id) or customer last name (lname)?: ")

while searchType != 'id' and searchType != 'lname':
    print("ERROR: You must enter either 'id' for invoice id search or 'lname' for customer last name search")
    searchType = input("Search by invoice id (id) or customer last name (lname)?: ")

searchTerm = input("Enter your search term: ")

file = open('sales_data.csv', 'r')
reader = csv.reader(file)
header = next(reader)

termCount = 0

for row in reader:
    if searchTerm in row:
        termCount = termCount + 1
        print(row)

print("{0} records found.".format(termCount))
    