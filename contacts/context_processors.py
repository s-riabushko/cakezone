from .models import Contacts
from .forms import SubscriberForm


def contacts(request):
    return {
        'index_contacts': Contacts.objects.first(),
        'subscriber_form': SubscriberForm()
    }
