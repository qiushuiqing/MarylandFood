# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MFcountry
from .models import MFrestaurant

# Register your models here.
admin.site.register(MFcountry)
admin.site.register(MFrestaurant)