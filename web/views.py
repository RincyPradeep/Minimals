from django.shortcuts import render
from web.models import Option,Help,Price


def index(request):
    options = Option.objects.all()
    helps = Help.objects.all()
    prices = Price.objects.all()

    context = {
        "options" : options,
        "helps" : helps,
        "prices" : prices
    }

    return render(request,"index.html", context=context)
