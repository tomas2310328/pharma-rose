from django.shortcuts import render
from .models import Checking
from django.db.models import Q
# Create your views here.


def checking_serial(request):
    qs = Checking.objects.all()

    barcode = request.GET.get('code')
    serial = request.GET.get('serial')

    if serial != '' and serial is not None and barcode != '' and barcode is not None:
        qs = qs.filter(Q(serial_number__iexact=serial) & Q(bar_code__iexact=barcode))

    context = {
        "queryset":qs,
        "barcode":barcode,
        "serial":serial
    }


    return render(request , "check/check_code.html", context)
