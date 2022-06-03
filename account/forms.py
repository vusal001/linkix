
from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username= forms.CharField(max_length=10, label='Telefon nömrəsi', required=True, widget=forms.TextInput(attrs={'type': 'tel'}))
    parol= forms.CharField(max_length=20, label='Parol', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.ModelForm):
    
    
    first_name= forms.CharField(max_length=15, label='Adınız')
    username= forms.CharField(label='Telefon nömrəsi', max_length=10, widget=forms.TextInput(attrs={'type': 'tel'}))
    last_name= forms.CharField(label='Email', required = False , max_length=50, widget=forms.TextInput(attrs={'type': 'email'}))
    password1= forms.CharField(max_length=20, label='Parol', widget=forms.TextInput(attrs={'type': 'password'}))



    
    class Meta:
        model= User

        fields=[
            'first_name',
            'username',
            'last_name',
            'password1',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {'pattern': "\d*", 'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);', 'maxlength': '10', 'placeholder': '050XXXXXXX', 'minlength': '10'}
         
        