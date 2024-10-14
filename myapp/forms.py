from django import forms
from myapp.models import User

class loginform(forms.ModelForm):

    class Meta:
        model=User
        fields=['name', 'lastname', 'password']

        widgets={
            'name': forms.TextInput(attrs={
                'placeholder':'enter name'
            })
        }