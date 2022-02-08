from pyexpat import model
from django.contrib import admin

from .models import Client


class image(admin.ModelAdmin):
    list_display =('first_name','service_visited','email','phone_no','date_created',)
    search_fileds=('first_name',)
    list_filter=('service_visited',)

# Register your models here.
admin.site.register(Client,image)


#new
