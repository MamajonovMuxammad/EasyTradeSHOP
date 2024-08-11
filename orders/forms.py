from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        # или используйте 'exclude', если вы хотите исключить определенные поля:
        # exclude = ['paid', 'created', 'updated']
