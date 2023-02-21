# Описание

Данный проект является моим первым написанным на Python-фреймворке Django проектом. С помощью него можно записывать изученные темы и добавлять к ним описание, редактировать и удалять их. В проекте реализована авторизация пользователя, а также хранение данных в БД.

# Требования

В качестве СУБД используется sqlite3, проект будет развёрнут с помощью Docker-Compose, который входит в состав Docker (Скачать Docker можно по [ссылке](https://docs.docker.com/get-docker/)). Используемые библиотеки хранятся в файле requirements.txt.

# Развертывание приложения

Для того, чтобы развернуть приложение, нужно:

1) скопировать файлы в локальную директорию с помощью команды

  $ git clone https://github.com/ighorstepanenko/Django_learning_logs.git

2) перейти в скопированную директорию и развернуть приложение в Docker-Compose, для этого необходимо выполнить следующие команды:

  $ cd Django_learning_logs/
  $ sudo docker compose up -d

> Если пишет, что данный адрес уже используется, то просмотрите с помощью команды `sudo ss -lptn 'sport = :<PORT>'` какой процесс использует данный адрес и остановите процесс с помощью команды `kill -KILL <PID>' либо измените в Dockerfile порт с "8000" на любой свободный в команде EXSPOSE

3) перейти в браузере по адресу http://localhost:8000/ (либо http://localhost:<прописанный вами порт>/)


