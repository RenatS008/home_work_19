### Описание задания:

### Шаг 1. Создайте пользователя

Используя Flask-RESTX, создайте три неймспейса и отдельные папки под них. Пропишите соответствующие методы.
- [ ] Создайте модель и схему пользователя и добавьте к ней CRUD (views с методами GET/POST/PUT). 

Создайте Class-Based Views и напишите методы, которые возвращали бы пустые строки или какие-то рандомные данные. 
Запустите приложение и, используя Postman, убедитесь, что всё работает.

### Шаг 2. Добавьте методы генерации хеша пароля пользователя
- [ ] Для сложной архитектуры — в слой с бизнес-логикой.
- [ ] Для сложной архитектуры хешируем пароли с помощью `pbkdf2_hmac`.

### Шаг 3. Добавьте недостающие методы

- [ ] У моделей `Director` и `Genre` отсутствуют методы `POST`, `PUT`, `DELETE`. Добавьте их. 
- [ ] Добавьте методы в сервис и в DAO. 

### Шаг 4. Добавьте эндпоинты аутентификации

**Эндпоинт**

`POST` /auth/ — возвращает `access_token` и `refresh_token` или `401` **Доступ**  Anonymous (кто угодно)

`PUT` /auth/ — возвращает `access_token` и `refresh_token` или `401` **Доступ**   Anonymous (кто угодно)

`POST /auth` — получает логин и пароль из Body запроса в виде JSON, далее проверяет соотвествие с данными в БД (есть ли такой пользователь, такой ли у него пароль)
и если всё оk — генерит пару access_token и refresh_token и отдает их в виде JSON.

`PUT /auth` — получает refresh_token из Body запроса в виде JSON, далее проверяет refresh_token и если он не истек и валиден — генерит пару access_token и refresh_token и отдает их в виде JSON.

### Шаг 5. Ограничьте доступ на чтение

- [ ] Защитите (ограничьте доступ) так, чтобы к некоторым эндпоинтам был ограничен доступ для запросов без токена. Для этого создайте декоратор `auth_required` и     декорируйте им методы, которые нужно защитить.

**Эндпоинт**                           

`GET` /directors/ + /directors/id         Authorized Required
 
`GET` /movies/ + /movies/id               Authorized Required

`GET` /genres/ + /genres/id               Authorized Required


** requirements **
aniso8601==9.0.1
attrs==21.2.0
click==8.0.3
Flask==2.0.2
flask-restx==0.5.1
importlib-metadata==4.8.1
itsdangerous==2.0.1
Jinja2==3.0.2
jsonschema==4.1.2
MarkupSafe==2.0.1
pyrsistent==0.18.0
pytz==2021.3
six==1.16.0
typing-extensions==3.10.0.2
Werkzeug==2.0.2
zipp==3.6.0
marshmallow~=3.17.0
PyJWT~=2.4.0
