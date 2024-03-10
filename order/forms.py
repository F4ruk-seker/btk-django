

from django import forms

from order.models import Order, ShopCart


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields: tuple = 'first_name', 'last_name', 'address', 'city', 'postal_code', 'country'


class ShopCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields: tuple = 'quantity',

