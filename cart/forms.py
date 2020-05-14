from django import forms
from django.utils.translation import gettext_lazy as _


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='quantity', max_value=99)
    update = forms.BooleanField(label='upd', required=False, initial=False)
