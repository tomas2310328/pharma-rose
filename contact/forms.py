from django import forms

# contact forms


class ContactForm(forms.Form):
    name        = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder':'your full name'}))
    email       = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'example@gmail.com'}))
    message     = forms.CharField(required=True,widget=forms.Textarea)
