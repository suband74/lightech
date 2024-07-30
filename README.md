# API для работы со балансом пользователя и перемещении денег между пользователями системы.

- Регистрация пользователя + получение токена `users/authentication/`
    - payload = {
        "email": email,
        "password": str
    }
- Пополнение баланса по емэйлу (доступно любому пользователю) POST `payment/income/`
   - payload = {
        "email": "email",
        "amount": int
    }
- Перечисление средств со своего счета на счет партнера POST `payment/spend/`
   - payload = {
        "partner_id": partner_id,
        "amount": int
    }
- Получить баланс своего счета `payment/balance/`

## Установка проекта на локальный компьютер:

1. Клонировать репозиторий:
```
git clone https://github.com/suband74/lightech
```
2. Установить docker и docker-compose. Инструкции по установке доступны в официальной документации.
3. В папке с проектом выполнить команду:
```
docker-compose up
```
4. Интерактивная документация к сервису доступна по адресу:

```
http://127.0.0.1:8000/swagger/
```

### Установка проекта для разработки

1. Должен быть предустановлен менеджер зависимостей `poetry`. Или установите `poetry` любым удобным способом. 
   Например: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -` 
2. Затем выполните установку зависимостей проекта: `poetry install`



#### Внешние зависимости

- Тестирование кода с помощью [pytest](https://docs.pytest.org/en/6.2.x/)
