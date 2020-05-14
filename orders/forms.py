from django import forms
from .models import Order
from localflavor.ru.forms import RU_REGIONS_CHOICES, RUPostalCodeField
# from django_countries.fields import CountryField


class OrderCreateForm(forms.ModelForm):
    city = forms.ChoiceField(choices=RU_REGIONS_CHOICES)
    postal_code = RUPostalCodeField()
    address2 = forms.CharField(required=False)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'phone', 'note']
