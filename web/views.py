from django.shortcuts import render
from web.models import Option


def index(request):
    options = Option.objects.all()

    context = {
        "options" : options
    }

    return render(request,"index.html", context=context)
