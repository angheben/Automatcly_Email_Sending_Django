from django.shortcuts import render
from .forms import ContactForms
from django.contrib import messages
from .forms import ProductModelForm
from .models import Product


def index(request):
    prod = Product.objects.all()
    context = {
        'prod': prod
    }
    return render(request, "index.html", context)


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
    if str(request.method) == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully registered')
            form = ProductModelForm()
        else:
            messages.error(request, 'Register denied')
    else:
        form = ProductModelForm()
    context = {
        'form': form
    }
    return render(request, "product.html", context)
