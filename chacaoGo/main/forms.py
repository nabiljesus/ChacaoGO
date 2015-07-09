from django       import forms
from django.forms import ModelForm, DateInput
from django.forms.widgets import TextInput
from main.models  import *
import datetime

class UserForm(forms.ModelForm):
    """Clase para formulario de usuario"""
    username = forms.CharField(max_length = 20,required=True)
    fullname = forms.CharField(max_length = 30,required=True)
    password = forms.CharField(max_length = 128,required=True,widget=forms.PasswordInput()) #Para sha
    password2= forms.CharField(max_length = 128,required=True,widget=forms.PasswordInput()) #Para sha
    email    = forms.EmailField(required=True) #Para sha

    class Meta:
        model = User
        fields = ['username','fullname','password','password2','email']

#Calculo de fecha minima y maxima
from datetime import datetime, timedelta
date  = datetime.now()
date   = date
today = date.strftime('%Y-%m-%d')
date   = date + timedelta(days=2)
afterTomorrow = date.strftime('%Y-%m-%d')
    
class EventForm(forms.ModelForm):
    """Clase para formulario de usuario"""
    name        = forms.CharField(max_length = 30,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length = 500,required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':'5','cols':'50'}))
    evType      = forms.ChoiceField(required=True,choices=TYPECHOICES)
    start       = forms.DateField(widget=forms.TextInput(attrs={'type':'date','min':today,'max':afterTomorrow}))
    end         = forms.DateField(widget=forms.TextInput(attrs={'type':'date','min':today,'max':afterTomorrow}))

    class Meta:
        model = Event
        fields = ['name','description','evType']


class CommentForm(forms.ModelForm):
    description = forms.CharField(max_length = 500,required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':'5','cols':'50'}))

    class Meta:
        model = Comment
        fields = ['description']

