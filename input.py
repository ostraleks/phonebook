


def input_data():
    import csv
    from pdb import line_prefix
    id = 0
    head = ['Фамилия', 'Имя', 'Отчество', '№ телефона']
    line = []
    for i in head:
        enter = input(f'Введите {i} ')
        line.append(enter)
    line.insert(0, id)
    with open('phonebook.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(line)
    


    