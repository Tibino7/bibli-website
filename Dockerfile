FROM python:3.8.0

COPY bibli /opt/bibli/

WORKDIR /opt/bibli

ENV POSTGRES_HOST=172.17.0.2
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=books
ENV POSTGRES_USER=tibino7
ENV POSTGRES_PWD=toto

RUN pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt &&\
    python3 manage.py makemigrations books &&\
    python3 manage.py migrate &&\
    python3 manage.py createsuperuserauto --username tibino7 --password toto --preserve --no-input --email 'tibino7@github.com'

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]