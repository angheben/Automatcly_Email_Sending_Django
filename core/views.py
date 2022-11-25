from django.shortcuts import render
from .forms import ContactForms
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def contact(request):
    form = ContactForms(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print('The message has been sent')
            print(f'Name: {name}')
            print(f'Email: {email}')
            print(f'Subject: {subject}')
            print(f'Message: {message}')

            messages.success(request, "E-mail successfully sent")
            form = ContactForms()
        else:
            messages.error(request, 'An error has occurred to subject the email')
    context = {
        "form": form
    }
    return render(request, "contact.html", context)


def product(request):
    return render(request, "product.html")
