
from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username= forms.CharField(max_length=30, label='Telefon nömrəsi', required=True, widget=forms.TextInput(attrs={'type': 'tel'}))
    parol= forms.CharField(max_length=20, label='Parol', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.ModelForm):
    
    
    first_name= forms.CharField(max_length=30, label='')
    username= forms.CharField(label='', max_length=10, widget=forms.TextInput(attrs={'type': 'tel'}))
    email= forms.EmailField(label='', required = False , max_length=50, widget=forms.TextInput(attrs={'type': 'email'}))
    password1= forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'type': 'password'}))



    
    class Meta:
        model= User

        fields=[
            'first_name',
            'username',
            'email',
            'password1',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs = {'pattern': "\d*", 'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);', 'maxlength': '30', 'placeholder': 'Ad və soyad', 'minlength': '3'}
        self.fields['username'].widget.attrs = {'pattern': "\d*", 'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);', 'maxlength': '10', 'placeholder': 'Tel nömrəsi (050XXXXXXX)', 'minlength': '10'}
        self.fields['email'].widget.attrs = {'pattern': "\d*", 'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);', 'maxlength': '20', 'placeholder': 'Email', 'minlength': '5'}
        self.fields['password1'].widget.attrs = {'pattern': "\d*", 'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);', 'maxlength': '30', 'placeholder': 'Parol', 'minlength': '8'}

        