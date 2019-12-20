FROM python:3.6.0

COPY . /opt/bibli-website/

WORKDIR /opt/bibli-website

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate --settings=demo.settings
RUN python manage.py loaddata demo/fixtures/* --settings=demo.settings

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "--settings=demo.settings", "0.0.0.0:8000"]
