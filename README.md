This Django application built to read CSV data from google docs URL and show them in UI and please follow the below steps to set up and run this application

Dependency: Python3.10

git clone https://github.com/umamch/contacts_report.git workdir

cd workdir

# Execution steps for hosting the application on your machine
pip install -r requirements.txt

python manage.py runserver

That's it, you can use this application with the below URLS in your browser

http://127.0.0.1:8000/contacts/

http://127.0.0.1:8000/contacts/<id> => id is in between 0 to 3 as CSV contains 4 records

http://127.0.0.1:8000/contactsset/ => JSON API


# Execution steps for hosting the application as a docker container
docker build . -t contacts

docker run -p 8000:8000 contacts


# Execute unit testing
python manage.py test
