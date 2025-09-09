from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-field", "placeholder": "Your name"}
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-field", "placeholder": "Your email"}
        )
    )

    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-field", "placeholder": "Subject"}),
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-field", "rows": 6, "placeholder": "Your Message"}
        )
    )
    captcha = CaptchaField(
        widget=CaptchaTextInput(
            attrs={"class": "form-field", "placeholder": "Enter CAPTCHA"}
        )
    )
