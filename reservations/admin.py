from django.contrib import admin
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from allauth.account.models import EmailAddress
from .models import Reservation, Review
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.utils import get_attachment_model

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):  
    list_display = ('customer', 'reservation_date', 'reservation_time')
    search_fields = (['customer__full_name__icontains', 'reservation_date'])
    list_filter = ('customer', 'reservation_date',)



@admin.register(Review)
class FeedbackAdmin(SummernoteModelAdmin):
    list_filter = ('review_date',)
    search_fields = (['reviewer_name', 'subject'])

# ADMIN PANELS THAT I WILL NOT NEED
admin.site.unregister(Site)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(EmailAddress)
admin.site.unregister(get_attachment_model())
