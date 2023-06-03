# Тестовое задание для 2035.university
Eсть таблицы с действиями `actions`, специализациями `specializations`, инструментами `tools` и связями между ними `actions_tools`, `specializations_actions` и `specializations_tools`.
## Задача:
Написать REST API, который будет предоставлять информацию из базы.<br> 
Нужны эндпойнты, которые будут отдавать списком действия, специализации и инструменты по GET.<br>
Ещё эндпойнт, который по GET-запросу с параметрами вида `action=Автоматизация Bash`, `tool=Linux` возвращает информацию о связи в виде словаря.
## Описание решения:
• Локальный запуск:<br>
&emsp;Установка зависимостей `requirements.txt`<br>
&emsp;Пример environments `.env.example`<br>
&emsp;Запуск приложения `start.py`<br>
• Запуск из Docker:<br>
&emsp;Запуск команд из каталога с файлом `docker-compose.yml`<br>
&emsp;`docker-compose build`<br>
&emsp;`docker-compose up`<br>
&emsp;Порт по-умолчанию 8000<br>
• Эндпоинт описания API: `/docs` и `/openapi.json`<br>
• Добавил пагинацию для GET `actions`, `specializations`, `tools`.<br>
• При необходимости можно дополнить тестами.
## Стек
FastAPI, SQLAlchemy, pydantic, uvicorn