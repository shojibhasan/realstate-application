from django.urls import path
from . import views


urlpatterns =[
    path('',views.listings_index,name='listing_index'),
    path('<int:listing_id>',views.listing,name='listing'),
    path('search/',views.search,name='search'),
    path('inquiry/',views.listings,name='inquiry'),
]