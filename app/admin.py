from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Ayah, Surah
# Register your models here.


admin.site.unregister(User)
admin.site.unregister(Group)


admin.site.register(Ayah)
admin.site.register(Surah)