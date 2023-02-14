## Практические работы по курсу "Администрирование баз данных"

### Quick start
Необходимо установить:
- docker
- docker compose

Запуск практики:
```bash
cp .env.exmaple .env # Делается при первом запуске. После необходимо зайти и поменять пароль для root пользователя.

source activate 

docker compose up -d
cd practice1 # Любая папка с практикой.

mongosh init.js # Подключаемся к контейнеру под $MONGO_ADMIN_USER (по умолчанию - root) и исполняем .js скрипт. В папке может быть несколько скриптов.
mongosh # Подключаемся через mongosh под $MONGO_ADMIN_USER (по умолчанию - root) и работаем с консолью.
```