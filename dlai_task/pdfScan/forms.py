from django import forms
from multiselectfield import MultiSelectFormField

#signup and signin forms.
class signup_form(forms.Form):
    username = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder':'Username','class': 'sign'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Email','class': 'sign'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value = True,attrs={'placeholder':'Password','class': 'sign'}))
    confirm_pass = forms.CharField(widget=forms.PasswordInput(render_value = True,attrs={'placeholder':'Confirm Password','class': 'sign'}))

class signin_form(forms.Form):
    username = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder':'Username','class': 'sign'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value = True,attrs={'placeholder':'Password','class': 'sign'}))