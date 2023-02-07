Домашнє завдання, лекція 5


1. Розробити власний REST API сервер, який буде приймати три типи запитів ["GET", "POST", "DELETE"].

2. Запит POST за адресою http://localhost:<port>/api/add_record/<record> повинен додавати вказаний запис та повертати відповідь: New added record: <record>

3. Запит GET за адресою http://localhost:<port>/api/last_10_records повинен відображати 10 останніх доданих записів в форматі json: {'last 10 added records': [r1, r2, r3 ...]}

4. Запит DELETE за адресою http://localhost:<port>/api/delete_record/<record> повинен видаляти вказаний запис та повертати відповідь: Removed record: <record>

5. Цей код описати в файлі main.py

6. Після успішного тестування розробленого API сервера, описати Dockerfile на базі Linux в якому потрібно встановити Python3, додати робочу папку code і цю папку перемістити код main.py

7. Запустити контейнер та виконати будь який запит для перевірки роботи REST API сервера


how to use:

curl -i -H "Content-Type: application/json" -X POST --data-binary "{\"id\":2, \"name\":\"Book of songs\"}"  http://127.0.0.1:5000/api/add_record

curl -i -H "Content-Type: application/json" -X DELETE --data-binary "{\"id\":2}"  http://127.0.0.1:5000/api/delete_record

curl -i -H "Content-Type: application/json" -X GET  http://127.0.0.1:5000/api/last_10_records


docker run -d -p 5000:5000 image_id