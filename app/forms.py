from django.forms.fields import DateField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import( PasswordChangeForm, UserCreationForm , 
UserChangeForm ,AuthenticationForm ,SetPasswordForm, UsernameField , PasswordResetForm)
from django.forms import TextInput, fields , EmailInput, widgets
from django.contrib.auth import password_validation
from django.utils.translation import gettext , gettext_lazy as _
from app.models import*
from django.core.exceptions import ValidationError

class RegistrationFormUser(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control','placeholder':'Enter the  Password '}),
        help_text=password_validation.password_validators_help_text_html(),
        )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control' , 'placeholder':'Confirm Password Again'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
        )
    class Meta:
        model=User
        fields=('username' , 'email')
        labels={'email':'Email'}
       
        widgets = {
        'username':TextInput(attrs={'class':'form-control','placeholder':'Enter the Username','required':'required'}),
        'email':EmailInput(attrs={'class':'form-control', 'placeholder':'Enter the Email', 'required':'required'})
        
        }

class LoginuserForm(AuthenticationForm):
     username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True ,'class':'form-control','placeholder':'Enter the Username', 'required':'required'}))
     password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control' ,'placeholder':'Enter the password', 'required':'required' }),
    )





class  MypasswordchangeForm(PasswordChangeForm):
        old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True , 'class':'form-control' ,'placeholder':'Enter the Old password', 'required':'required' }),
        )
        new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control' ,'placeholder':'Enter the New password', 'required':'required'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
        )
        new_password2 = forms.CharField(
        label=_("New password (Again)"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control' ,'placeholder':'New password (Again)', 'required':'required'}),
        )

class Usersetpasswordform(SetPasswordForm): 
        new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control' ,'placeholder':'Enter the New password', 'required':'required'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
        )
        new_password2 = forms.CharField(
        label=_("New  Confirm password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control' ,'placeholder':'Confirm password ', 'required':'required'}),
        )


class Email_Check(PasswordResetForm):
     email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email' ,'class':'form-control', 'placeholder':'Enter the Email', 'required':'required'})
    )




# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model=Profile
#         fields=('first_name' , 'last_name' , 'birthday' , 'city','address','state')
 
#         widgets={
#             'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the first name', 'required':'required'}),
#             'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the  last name', 'required':'required'}),
#             'birthday':forms.SelectDateWidget(years=range(1980 , 2050) ,attrs={'class':'form-control', 'placeholder':'Enter the birthday', 'required':'required'}),
#             'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the city', 'required':'required'}),
#             'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the address', 'required':'required'}),
#             'state':forms.Select(attrs={'class':'form-control', 'placeholder':'Enter the state', 'required':'required'}),
            
#         }



class DateInput(forms.DateInput):
    input_type = 'date'

class PICKUP_form_type(forms.ModelForm):
    class Meta:
        model=Select_Goods
        fields=('pick_city' , 'drop_city' , 'truck_type','Select_date_type' , 'Select_good_type' , 'Select_customer_type' ,'enter_weight','mobile')
 
        widgets={
            'pick_city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Pickup City', 'required':'required'}),
            'drop_city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Drop City', 'required':'required'}),
            'truck_type':forms.Select(attrs={'class':'form-control', 'placeholder':'Select Truck Type', 'required':'required'}),
            'Select_date_type':DateInput(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}),
            'Select_good_type':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Select Full Truck Goods Type', 'required':'required'}),
            'Select_customer_type':forms.Select(attrs={'class':'form-control', 'placeholder':'', 'required':'required'}),
            'enter_weight':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Weight ( ONE TON = 1000 KG )', 'required':'required'}),
            'mobile':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Mobile Number', 'required':'required'}),
           

}



class VenderForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control','placeholder':'Enter the  Password '}),
        help_text=password_validation.password_validators_help_text_html(),
        )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control' , 'placeholder':'Confirm Password Again'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
        )

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True ,'class':'form-control','placeholder':'Enter the Username', 'required':'required'}))

    class Meta:
        model=Vender
        fields=('username','first_name', 'last_name',  'email', 'Company_name_or_shop_name', 'GST_Number')
        widgets={
            'username':TextInput(attrs={'class':'form-control','placeholder':'Enter the Username','required':'required'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the first name', 'required':'required'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the  last name', 'required':'required'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter the Email', 'required':'required'}),
            'Company_name_or_shop_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the company or shop name', 'required':'required'}),
            'GST_Number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'GST Number Optional','required':'none'}),
        }
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
      }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



