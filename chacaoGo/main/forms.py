from django       import forms
from main.models  import User,Event

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


        
class EventForm(forms.ModelForm):
    """Clase para formulario de usuario"""
    name        = forms.CharField(max_length = 30,required=True)
    description = forms.CharField(max_length = 500,required=True)
    start       = forms.CharField(max_length = 128,required=True,widget=forms.PasswordInput()) #Para sha
    end         = forms.EmailField(required=True) 

    class Meta:
        model = Event
        fields = ['name','description','start','end','evType']







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
