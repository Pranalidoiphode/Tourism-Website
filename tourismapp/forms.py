from tourismapp.models import Travel,Book
from django.forms import ModelForm
from django import forms

class TravelForm(forms.ModelForm):
    class Meta:
        model=Travel
        fields="__all__"

class DateSelectorForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['t_id', 'no_people', 'dates']
        

