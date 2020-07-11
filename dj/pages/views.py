from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

from listings.models import listings
from realtos.models import Realtor
from listings.model_choices import *


def index(request):
    latest = listings.objects.order_by('-list_date')[:3]

    context={
        'latest':latest,
        'state_choices':state_choices,
        'badrooms_choices':badrooms_choices,
        'price_choices':price_choices,
    }

    return render(request, 'pages/index.html',context)

def about(request):
    team = Realtor.objects.order_by('-contact_date')[:3]
    #print(team)

    context ={
        'team':team,
    }
    return render(request,'pages/about.html',context)
