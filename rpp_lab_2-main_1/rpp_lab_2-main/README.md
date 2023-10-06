Создание виртуальной среды:
```sh
python3 -m venv env
```
Установка зависимостей:
```sh
./env/Scripts/pip3 install -r requirements
```
Запуск сервера:
```sh
./env/Scripts/python3 main.py
```
# Примеры запросов (локально):
```sh
curl -X POST "http://127.0.0.1:5000/v1/add/tax" -d "{\"code\": \"54\", \"tax\": \"100\"}" -H "Content-type: application/json" -H "Accept: application/json"
```
```sh
curl -X GET "http://127.0.0.1:5000/v1/fetch/taxes" -H "Content-type: application/json" -H "Accept: application/json"
```
```sh
curl -X GET "http://127.0.0.1:5000/v1/fetch/tax?code=54" -H "Content-type: application/json" -H "Accept: application/json"
```
```sh
curl -X GET "http://127.0.0.1:5000/v1/fetch/calc?code=54&cadastral_value=2&month_of_ownership=24" -H "Content-type: application/json" -H "Accept: application/json"
```
```sh
curl -X POST "http://127.0.0.1:5000/v1/update/tax" -d "{\"code\": \"54\", \"tax\": \"300\"}" -H "Content-type: application/json" -H "Accept: application/json"
```
# Примеры запросов (vercel):
```sh
curl -X POST "https://rpp-lab-2.vercel.app/v1/add/tax" -d "{\"code\": \"54\", \"tax\": \"100\"}" -H "Content-type: application/json" -H "Accept: application/json"
```
```sh
curl -X GET "https://rpp-lab-2.vercel.app/v1/fetch/taxes" -H "Content-type: application/json" -H "Accept: application/json"
```
```sh
curl -X GET "https://rpp-lab-2.vercel.app/v1/fetch/tax?code=54" -H "Content-type: application/json" -H "Accept: application/json"
```
```sh
curl -X GET "https://rpp-lab-2.vercel.app/v1/fetch/calc?code=54&cadastral_value=2&month_of_ownership=24" -H "Content-type: application/json" -H "Accept: application/json"
```
```sh
curl -X POST "https://rpp-lab-2.vercel.app/v1/update/tax" -d "{\"code\": \"54\", \"tax\": \"300\"}" -H "Content-type: application/json" -H "Accept: application/json"
```