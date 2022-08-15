from sys import argv


def calculate(h_value, o_value, p_value):
    return h_value * o_value + p_value


try:
    script_name, hours, oklad, premium = argv
    print(f'результат расчета {calculate(float(hours), float(oklad), float(premium))}')
except ValueError:
    print('Неверно указано кол-во параметров, пример использования python task_01.py 10 100 0, кол-во часов, ставка, '
          'премия')
