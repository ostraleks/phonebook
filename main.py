import menu
import input

def main():
    menu.main_menu('Start')
    while (True):
        menu.main_menu('Main')
        value = input('Выберите пункт меню: ')
    match value:
                case 1:
                    print('=' * 50)
                    print('Ввод новой записи')
                    print('=' * 50)

                    # try:
                    input.input_data()
                    # except:
                        
                        # continue
                # case 2:
                #     print('=' * 50)
                #     print('Калькулятор для работы с комплексными числами')
                #     print('=' * 50)

                #     ui.choice_menu_complex_nums()
                #     value_2 = input('Выберите действие с числами: ')
                #     value_2 = ex.check_input_menu(value_2)
                #     log.oper_logger(value_2)

                #     try:
                #         if 1 <= value_2 <= 7:
                #             ui.calc_complex_nums(value_2)
                #     except:
                #         log.actions_logger('Пользователь ввёл некорректные данные для вычисления.')
                #         print('Некорректное значение! Введите число!\n')
                #         print('=' * 50)
                #         continue
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
       
        