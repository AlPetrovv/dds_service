# DDS Service 

## Разворачивание проекта


Клонируем репозиторий с GitHub  
```sh
  git clone https://github.com/AlPetrovv/dds_service.git
```
1. Перейти в папку dds_service от корневой директори и создать .env файл в папке с .env.template файлом и заполнить его по примеру

2. Установить poetry(версия 1.8.4)
   * Можно установить [here](https://python-poetry.org/)
   * Или просто `pip install poetry==1.8.4`
   * Или через команду(необходимо установить curl) `curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.4 python3 -`
3. Создать виртуальное окружение
   ```sh
   poetry env use 3.10
   ```
4. Активировать виртуальное окружение
   ```sh
   source "$(poetry env info -p)"/bin/activate
   ```
5. Установить зависимости
   ```sh
   poetry install
   ```
6. Запустить базу данных 
```sh
docker compose up --build -d
```
7. Запустить миграции 
   ```sh
   python3 manage.py migrate
   ```
8. Создать суперпользователя
   ```sh
   python3 manage.py createsuperuser
   ```
9. Запустить сервер
   ```sh
   python3 manage.py runserver
   ```
10. Открыть браузер и перейти по [адресу](http://localhost:8000/admin/)