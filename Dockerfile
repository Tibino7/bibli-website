FROM python:3.8.0

COPY bibli /opt/bibli/

WORKDIR /opt/bibli

ENV MONGO_HOST="172.17.0.2"
ENV MONGO_PORT=27017
ENV MONGO_DB=bibli_db
ENV MONGO_USER=mongoadmin
ENV MONGO_PWD=secret

RUN pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt &&\
    python3 manage.py makemigrations books &&\
    python3 manage.py migrate &&\
    python3 manage.py createsuperuserauto --username tibino7 --password toto --preserve --no-input --email 'tibino7@github.com'

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]