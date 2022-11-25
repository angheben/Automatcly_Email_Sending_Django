from django import forms
from django.core.mail.message import EmailMessage


class ContactForms(forms.Form):
    name = forms.CharField(label="Name", max_length=100, min_length=1)
    email = forms.CharField(label="Email", max_length=100, min_length=1)
    subject = forms.CharField(label="Subject", max_length=120, min_length=1)
    message = forms.CharField(label="Message", widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f"Name {name}\n, Email: {email}\n, subject: {subject}\n Message: {message}\n"
        mail = EmailMessage(
            subject="Email sent by django2 system",
            body=content,
            from_email='contat@domain.com',
            to=['user@domain.com'],
            headers={'Reply to': email}
        )
        mail.send()
