from django.contrib import admin
from .models import Lecture, Member, Member_Lecture
# Register your models here.

admin.site.register(Member)
admin.site.register(Lecture)
admin.site.register(Member_Lecture)