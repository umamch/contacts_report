from rest_framework_json_api import serializers
from csv_contacts.models import Contacts


class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacts
        fields = ('firstname', 'lastname', 'street', 'zip', 'city', 'image')
