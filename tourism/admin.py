from django.contrib import admin

from tourism.models import Tag, Tour, TourBooking, TourReview, Tourist

admin.site.register(Tag)
admin.site.register(Tour)
admin.site.register(Tourist)
admin.site.register(TourBooking)
admin.site.register(TourReview)
