import requests

url_base = 'http://127.0.0.1:5000/v1/'
add_tax_url = f'{url_base}add/tax'

add_tax_url_tax_result = requests.post(url=add_tax_url, json={"code": 54, "tax": 100})
print(f'Результат добавления налога "{add_tax_url_tax_result.status_code}": {add_tax_url_tax_result.content}')


output_taxes_url = f'{url_base}fetch/taxes'
output_taxes_url_tax_result = requests.get(url=output_taxes_url)
print(f'Вывод всех записей "{output_taxes_url_tax_result.status_code}": {output_taxes_url_tax_result.content}')

calc_tax_url = f'{url_base}fetch/calc?code=54&cadastral_value=300000&month_of_ownership=36'

calc_tax_url_tax_result = requests.get(url=calc_tax_url)
print(f'Результат расчета налога "{calc_tax_url_tax_result.status_code}": {calc_tax_url_tax_result.content}')

'''
    Делаем run main.py -> Выбираем справа вверху test (1).py и запускаем в режиме debug (жучок)"
'''