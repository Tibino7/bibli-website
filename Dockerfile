FROM python:3.8.0

COPY bibli /opt/bibli/

WORKDIR /opt/bibli

ENV MYSQL_HOST=172.17.0.2
ENV MYSQL_PORT=3306

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations books
RUN python3 manage.py sqlmigrate books 0001
RUN python3 manage.py migrate

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]