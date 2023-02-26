Запуск практики:
```bash
cp .env.exmaple .env # Делается при первом запуске.

source activate 

docker compose up -d

mongosh init.js # Подключаемся к контейнеру под $MONGO_ADMIN_USER (по умолчанию - root) и исполняем .js скрипт.
mongosh # Подключаемся через mongosh под $MONGO_ADMIN_USER (по умолчанию - root) и работаем с консолью.