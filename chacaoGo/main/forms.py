from django       import forms
from main.models  import User

class UserForm(forms.ModelForm):
    """Clase para usuario"""
    username = forms.CharField(max_length = 20,required=True)
    fullname = forms.CharField(max_length = 30,required=True)
    password = forms.EmailField(max_length = 128,required=True,widget=forms.PasswordInput()) #Para sha
    password2= forms.EmailField(max_length = 128,required=True,widget=forms.PasswordInput()) #Para sha
    email    = forms.EmailField(required=True) #Para sha
    userType = forms.CharField(max_length = 11,required=True) 
    #added    = models.DateTimeField(auto_now_add=True) 

    class Meta:
        model = User
        fields = ['username','fullname','password','password2','email','userType']