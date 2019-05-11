from django.shortcuts import render


# main Views


def home(request):
    return render(request, 'home.html', {})
