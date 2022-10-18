


def input_data():
    import csv
    from pdb import line_prefix
    # id = 0
    head = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    line = []
    for i in head:
        enter = input(f'Введите {i} ')
        line.append(enter)  
    with open('phonebook.csv', 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(line)
    


    