import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }

    with open('orders.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        data['orders'].append(dict_to_json)

    with open('orders.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


write_order_to_json('Chair', 4, 2500, 'Freed', '10-03-2010')
write_order_to_json('Table', 1, 11400, 'Yuan', '02-12-2011')
write_order_to_json('Sofa', 2, 7600, 'Cox', '23-05-2007')
write_order_to_json('Carpet', 3, 900, 'Keller', '30-06-2015')
