from django.forms import ModelForm
from .models import Personne
from django.contrib.auth.models import User
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        
class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ['cnpe', 'telephone', 'metier']
        
 
