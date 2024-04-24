from django.contrib import admin

# Register your models here.
from .models import User, Test, Result

admin.site.register([User, Test, Result])



