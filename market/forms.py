from django import forms
from .models import Market

class MarketPost(forms.ModelForm):
    class Meta:
        model=Market
        fields=['name', 'photo', 'price','num','category','sentence', 'description']