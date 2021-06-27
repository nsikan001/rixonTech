from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    # return HttpResponse("this is the home page")
    return render(request, 'index.html', {})


def services(request):
    return render(request, 'services.html', {})


def about(request):
    return render(request, 'about.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def contact(request):
    if request.method == 'POST':
        # to =
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # send email
        send_mail(
            subject,
            message,
            email,
            ['adaowonsikan6952@gmail.com'],
        )
        # send_mail(
        #     fname,
        #     lname,
        #     message,
        #     subject,
        #     email,
        #     ['adaowonsikan69@gmail.com'],
        #
        # )
        return render(request, 'contact.html', {'fname':fname})
    return render(request, 'contact.html', {})