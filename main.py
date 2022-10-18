import menu
import input_data
import search

def main():
    menu.main_menu('Start')
    while (True):
        menu.main_menu('Main')
        value = int(input('Выберите пункт меню: '))
        match value:
            case 1:
                print('=' * 50)
                print('Ввод новой записи')
                print('=' * 50)
                input_data.input_data()
                
            case 2:
                print('=' * 50)
                print('Поиск записи')
                print('=' * 50)
                search_string = []
                name = input('Введите фамилию ')
                search_string = search.search_data(name)
                for key,value in search_string.items():
                    print(key, ':', value)

                # case 3:
                #     print('Запущен выход из программы')
                #     ui.exit_menu("End")

                #     value_exit = input('Выберите действие с числами: ')
                #     value_exit = ex.check_input_menu(value_exit)

                #     if value_exit == 1:
                #         continue
                #     else:
                #         print("*" * 50, '\nСпасибо, что использовали наше приложение, всего Вам доброго!!!')
                #         break
                # case _:
                #     print('\n' * 10, 'Введите число в указанном диапазоне!\n')
                #     print('=' * 50)

main()
       
        