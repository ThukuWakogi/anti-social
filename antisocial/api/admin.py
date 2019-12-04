from django.contrib import admin
from .models import NeighborHood, User, Business, Post, ContactInfo

admin.site.register(NeighborHood)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(ContactInfo)
