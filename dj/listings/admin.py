from django.contrib import admin
from listings.models import listings,Inquiry



class ListingAdmin(admin.ModelAdmin):
    class Meta:
        model = listings

    list_display = ['id', 'title','address','city','realtor','is_published']
    list_display_links = ['id','title']
    list_filter =('realtor'),
    list_editable = ('is_published'),
    search_fields = ('title','address','desc','city','price'),
    list_per_page = 20

admin.site.register(listings, ListingAdmin)


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['listing', 'user', 'phone']
    class Meta:
        model = Inquiry






admin.site.register(Inquiry, InquiryAdmin)
