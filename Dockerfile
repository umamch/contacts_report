From python:3.10

# Install system depedencies

RUN pip install --upgrade pip

# Install python dependencies
WORKDIR /tmp/
COPY . /tmp/
RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
