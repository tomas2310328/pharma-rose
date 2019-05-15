from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
# Create your views here.


def contact(request):
    title = 'Contact-US'
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            emailFrom = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'message from {n}'.format(n=name)
            emailTo = settings.EMAIL_HOST_USER
            # emailTo = getattr(settings, "EMAIL_HOST_USER", "thomas.adel31@gmail.com")
            send_mail(subject, message, emailFrom, [emailTo], fail_silently=True)

            messages.success(request, "Your Message Has Been Sent, Our staff will call back later and answer your questions.")
            return redirect("contact:contact")
    else:
        form = ContactForm()



    context = {
        'form': form,
        'title': title
    }

    return render(request, 'contact/contact.html', context)






#
# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['to@example.com'],
#     fail_silently=False,
# )
