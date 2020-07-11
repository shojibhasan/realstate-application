from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import listings, Inquiry
from django.contrib import messages
from .model_choices import price_choices,badrooms_choices,state_choices
from django.core.mail import send_mail
from django.conf import settings


# Listing App View

def listings_index(request):
    listing_list = listings.objects.all()
    paginator = Paginator(listing_list,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listing_list': paged_listings,
    }

    return render(request, 'listings/listings.html',context)

def listing(request,listing_id):
    listing = listings.objects.get(id=listing_id)
    return render(request,'listings/listing.html',{'listing':listing})


def search(request):
    # city_ = request.GET.get('city')  # Do Not Do This or u will be slapped
    get_method = request.GET.copy()
    keywords = get_method.get('keywords') or None
    city = get_method.get('city') or None
    print(keywords, city)
    listing_list = listings.objects.all()

    # keywords
    if keywords is not None:
        keyword = get_method['keywords']
        # print(keyword)
        listing_list = listing_list.filter(desc__icontains=keyword)     # django == Django development
        # listing_list = listing_list.filter(desc__iexact=keyword)     # django == Django

    # city
    if city is not None:
        city = get_method['city']
        listing_list = listing_list.filter(city__iexact=city)

    # state
    if 'state' in get_method:
        state = get_method['state']
        listing_list = listing_list.filter(state__iexact=state)

    # bedrooms
    if 'bedrooms' in get_method:
        bedrooms = get_method['bedrooms']
        print(bedrooms)
        listing_list = listing_list.filter(bedrooms__lte=int(bedrooms))     # 5 <= 1, 2, 3, 4, 5
        print(listing_list)

    # price
    if 'price' in get_method:
        price = get_method['price']
        listing_list = listing_list.filter(price__lte=int(price))

    context = {
        'state_choices': state_choices,
        'bedroom_choices': badrooms_choices,
        'price_choices': price_choices,
        'get_method': get_method,
        'listing_list': listing_list,
    }
    return render(request, 'listings/search.html', context)

def inquiry(request):
    if request.method == "POST":
        get_method = request.POST.copy()
        listing = get_method.get('listing') or None
        phone = get_method.get('phone') or None
        message = get_method.get('message') or None


        listing_object = listings.objects.get(title=listing)

        inquirey_exist = Inquiry.objects.filter(listing=listing_object,user=request.user)
        if not inquirey_exist:
            Inquiry.objects.creats(listing=listing_object,user=request.user,phone=phone,message=message)
            messages.success(request, 'Inquiry Message Sent Sucessfully!')
        else:
            messages.success(request, 'Inquiry Already Done')
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        send_mail(
            'Inquiry Listing From DJRE',
            'Thank You for Contracting us . We will contact you as soon as possible',
            settings.EMAIL_HOST_USER,
            [request.user.email],
            fail_silently=False,
        )