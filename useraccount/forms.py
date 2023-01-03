from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.urls import reverse_lazy
from .models import Profile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_zip(value):
    if len(str(value)) >5:
        raise ValidationError(
            _('%(value)s Se requieren cinco dígitos'),
            params={'value': value},
        )
class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class' : 'form-control',
                                    'id' : 'username',
                                    'placeholder' : 'Username'
                                }))
    
    
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={
                                'class' : 'form-control',
                                'id' : 'username',
        '                       placeholder' : 'example@gmail.com',
        }))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class' : 'form-control',
                                }))
    
    
    
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email

    def clean_role(self):
        role = self.cleaned_data.get('email')

        return role

    
   
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),

        )

    
class UsrChangeFrm(UserChangeForm):
    
    def __init__(self, *args, **kwargs):
        super(UsrChangeFrm, self).__init__(*args, **kwargs)
  
        for fieldname in ['password']:
            self.fields[fieldname].widget = forms.HiddenInput()
                
           
  
    username = forms.CharField(label='Nombre | (alias)',max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre(s)',max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Apellido(s)', max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    
    email = forms.CharField(label='Correo Electrónico',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'type':'email'}))
   
    class Meta:
      
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
        
    
class PwdChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Password actual',widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password','placeholder':'Clave actual'}))
    new_password1= forms.CharField(label='Password nuevo',max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password','placeholder':'Almenos seis dígitos'}))
    new_password2= forms.CharField(label='Confirma password',max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password','placeholder':'Almenos seis dígitos'}))

    class Meta:
      model = User
      fields = ('old_password', 'new_password1', 'new_password2')  



   

class ProfileForm(forms.ModelForm):
    street = forms.CharField(label='Calle',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip = forms.IntegerField(label='Código Postal', validators=[validate_zip],
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='Ciudad',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    
    country = forms.CharField(label='País',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    
    class Meta:
      
        model = Profile
        fields = ['street', 'zip', 'city', 'country']
        
        
                        
