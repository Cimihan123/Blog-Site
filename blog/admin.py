from django.contrib import admin

# Register your models here.
from .models import *



admin.site.register(Skill)

admin.site.register(Contact)


admin.site.register(Post)

admin.site.register(Comment)
