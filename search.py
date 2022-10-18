import csv
def search_data(name_string): 
    reader = {}  
    with open('phonebook.csv', 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Фамилия'] == name_string:
                return row


