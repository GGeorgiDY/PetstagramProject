# искам да вземеш гото имидж който се казва python:3.10
FROM python:3.10

# направи ъпдейт на операционната система
RUN apt update -y \
    && apt upgrade -y

# сетвам си два environment variables които са задължителни когато деплоойваме за пайтън
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED 1

# тук започва нашата конфигурация
#
ENV HOME=/home/app
# аз искам да деплойна апликейшъна в ето тази папка
ENV APP_HOME=home/app/web

#ENV STATICFILES_HOLE=/tpm/staticfiles

#RUN mkdir -p $STATICFILES_HOME

# отиди в тази директория, която ако не съществува я създай
WORKDIR $APP_HOME

# след това ъпгрейдвам pip-a
RUN pip install --upgrade pip

# копирам requirements.txt вътре в контейнера (в ето тази папка $APP_HOME)
COPY ./requirements.txt .

# изпълнявам install
RUN pip install -r requirements.txt

# копирам всичко от текущата директория в ето тази директория $APP_HOME
COPY . .
