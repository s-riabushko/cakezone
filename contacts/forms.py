from django import forms
from .models import MessageFromCustomer, Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control border-white p-3', 'placeholder': 'Your Email'}),
        }


class MessageFromCustomerForm(forms.ModelForm):
    class Meta:
        model = MessageFromCustomer
        fields = ('name', 'email', 'subject', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                           'style': 'height: 55px;', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                             'style': 'height: 55px;', 'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                              'style': 'height: 55px;', 'placeholder': 'Your subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control bg-light border-0 px-4',
                                             'rows': '4;', 'placeholder': 'Message'}),
        }
