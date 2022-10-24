from django.forms import ModelForm
from contact.models import Contact
from contact.models import Ssce

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['date_created', 'date_modified']
    
class SsceForm(ModelForm):
    class Meta:
        model = Ssce
        exclude = ['date_created', 'date_modified']