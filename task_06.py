product_list = []
analytic_dict = {'name': [], 'price': [], 'count': [], 'unit': []}
while True:
    product_counter = len(product_list) + 1
    product_name = input(f'Введите название товара {product_counter}: ')
    product_price = input(f'Введите цену товара {product_counter}: ')
    product_count = input(f'Введите кол-во товара {product_counter}: ')
    product_unit = input(f'Введите ед. измерения товара {product_counter}: ')
    product_list.append((
        product_counter, {
            'name': product_name,
            'price': product_price,
            'count': product_count,
            'unit': product_unit
        }
    ))
    if input('Закончить введение товаров Yy/Nn (N)? ').capitalize() == 'Y':
        break
for el in product_list:
    for key in el[1].keys():
        if analytic_dict[key].count(el[1][key]) < 1 and key == 'unit':
            analytic_dict[key].append(el[1][key])
        elif key != 'unit':
            analytic_dict[key].append(el[1][key])
print(f'products list {product_list}')
print(f'analytics dict {analytic_dict}')
