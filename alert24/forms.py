from django import forms 


class Students(forms.Form):
    name = forms.CharField(widget=forms.EmailInput(
        attrs={
            "placeholder":"Enter your message...",
            "type": "date",
            "class": 'form-control bg-success-subtle'
        }
    ))
    email = forms.CharField()
    message = forms.CharField()