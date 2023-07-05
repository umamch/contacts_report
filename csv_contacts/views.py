from csv_contacts.serializers import ContactsSerializer
from rest_framework import viewsets
from django.template import loader
from django.http import HttpResponse
from .models import Contacts
from django.templatetags.static import static
import requests
import validators
import logging
import datetime


class ContactsViewSet(viewsets.ModelViewSet):
    """Class to provide JSON API to use GET, POST,PUT and Fileter operations on Contacts DB table
    Usage:GET http://127.0.0.1:8000/contactsset/
          GET http://127.0.0.1:8000/contactsset/1/
    """
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


def is_url_image(image_url):
    """Support function for check_image method to identify url is type image or not"""
    try:
        image_formats = ("image/png", "image/jpeg", "image/jpg")
        r = requests.head(image_url)
        if r.headers["content-type"] in image_formats:
            return True
        return False
    except Exception as err:
        write_log('warning', err)


def check_image(image):
    """Function used to check the input url is an image or not
     Input: image url
     """
    if (validators.url(str(image))) and (is_url_image(str(image))):
        return True
    else:
        return False


def contacts_list(request, id=None):
    """REST API method to UI display integration
     Provide data from Contacts table in DB
     Usage:GET http://127.0.0.1:8000/contacts/
           GET http://127.0.0.1:8000/contacts/1
     """
    try:
        if id is not None:
            singleContact = Contacts.objects.get(id=id)
            if not check_image(singleContact.image):
                singleContact.image = static('images/thumbnail.png')
            context = {
                'singleContact': singleContact,
            }
        else:
            contacts = Contacts.objects.all().values()
            for item in contacts:
                if not check_image(item['image']):
                    item['image'] = static('images/thumbnail.png')
            context = {
                'contacts': contacts,
            }
        template = loader.get_template('csv_contacts.html')
    except AttributeError as err:
        write_log('error', err)
        return HttpResponse("<h>No Records with provided attribute ID: " + id + "</h>")
    except Exception as err:
        write_log('error', err)
        return HttpResponse("<h>Error: " + str(err) + "</h>")
    return HttpResponse(template.render(context, request))


def write_log(log_level, ex):
    """Method for logging the messages at different levels of application
    Parameters: log level and message
    it is uses logging module internally
    """
    logging.basicConfig(filename='contacts.log', filemode='w', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    if log_level.lower() == 'error':
        logger.error(ex)
    else:
        logger.info(ex)
