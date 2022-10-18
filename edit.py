import csv
import search
def edit_data(name_string):
    edit_line = []
    reader = {}  
    with open('phonebook.csv', 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Фамилия'] == name_string:
                edit_line = row
            file.replace(row, '')
    for key,value in edit_line.items():
        print(key, ':', value)
    number = edit_line['Телефон']
    print(number)
    # head = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    # line = []
    for i in edit_line.keys():
        enter = input(f'Изменяем значение {i}? Если да, нажмите 1 ')
        if enter == '1':
            edit_line[i] = input('Новое значение ')
    print (edit_line)    
    with open ('phonebook.csv', 'r') as file:
        old_data = file.read()
        new_data = old_data.replace('что_меняем', 'на_что_меняем')

with open ('test.txt', 'w') as f:
  f.write(new_data)
        
   

edit_data('перов')