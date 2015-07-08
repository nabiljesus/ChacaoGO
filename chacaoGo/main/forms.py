from django       import forms
from django.forms import ModelForm, DateInput
from django.forms.widgets import TextInput
from main.models  import User,Event,TYPECHOICES
import datetime

class UserForm(forms.ModelForm):
    """Clase para formulario de usuario"""
    username = forms.CharField(max_length = 20,required=True)
    fullname = forms.CharField(max_length = 30,required=True)
    password = forms.CharField(max_length = 128,required=True,widget=forms.PasswordInput()) #Para sha
    password2= forms.CharField(max_length = 128,required=True,widget=forms.PasswordInput()) #Para sha
    email    = forms.EmailField(required=True) #Para sha
    #userType = forms.CharField(max_length = 11,required=True) 
    #added    = models.DateTimeField(auto_now_add=True)

    def isValid(self):
        #Chequeo de validez muy basico
        valid = True
        #Y explota... fucking shit
        #valid = valid and self.cleaned_data['password'] == self.cleaned_data['password2']
        return valid

    class Meta:
        model = User
        fields = ['username','fullname','password','password2','email']

#Calculo de fecha minima y maxima
from datetime import datetime, timedelta
date  = datetime.now()
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





# class LoginForm(forms.ModelForm):
#     username = forms.CharField(max_length = 20,required=True,widget=forms.TextInput(attrs={'class':'invisible center','id':'username'}))
#     password = forms.CharField(max_length = 128,required=True,widget=forms.PasswordInput(attrs={'class':'invisible center','id':'password'})) #Para sha

#     def is_valid(self):
#         valid = super(LoginForm, self).is_valid()

#         if not valid:
#             return valid

#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']



#         res  = (type(username) is str) and (type(password) is str)
#         if res:
#             res  = len(username) <= 20 and len(password) <= 128

#         return res

#     class Meta:
#         model = User
#         fields = ['username','password']
