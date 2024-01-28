from django import forms
from purchase.models import PurchaseClass

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseClass
        fields = ['car', 'user']
