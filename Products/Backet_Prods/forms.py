from django import forms


class BasketForm(forms.Form):
    quantity = forms.IntegerField()