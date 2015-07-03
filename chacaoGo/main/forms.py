from django       import forms
from main.models  import User

class UserForm(forms.ModelForm):
    """Clase para formulario de usuario"""
    username = forms.CharField(max_length = 20,required=True)
    fullname = forms.CharField(max_length = 30,required=True)
    password = forms.CharField(max_length = 128,required=True,widget=forms.PasswordInput()) #Para sha
    password2= forms.CharField(max_length = 128,required=True,widget=forms.PasswordInput()) #Para sha
    email    = forms.EmailField(required=True) #Para sha
    userType = forms.CharField(max_length = 11,required=True) 
    #added    = models.DateTimeField(auto_now_add=True)

    def isValid(self):
        #Chequeo de validez muy basico
        valid = True
        #Y explota... fucking shit
        #valid = valid and self.cleaned_data['password'] == self.cleaned_data['password2']
        return valid

    class Meta:
        model = User
        fields = ['username','fullname','password','password2','email','userType']

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length = 20,required=True,widget=forms.TextInput(attrs={'class':'invisible','id':'username'}))
    password = forms.CharField(max_length = 128,required=True,widget=forms.PasswordInput(attrs={'class':'invisible','id':'password'})) #Para sha

    class Meta:
        model = User
        fields = ['username','password']
