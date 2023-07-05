From python:3.10

# Install system depedencies

RUN pip install --upgrade pip
#RUN apt-get update && apt-get install -y procps

# Install python dependencies
WORKDIR /tmp/
COPY . /tmp/
RUN pip install -r requirements.txt
RUN pip freeze > requirements.txt

EXPOSE 8000


CMD python manage.py runserver
#CMD ["sleep", "infinity"]