from django.contrib import admin

from .models import Article, Info, Image, Subject, BestWorks

admin.site.register(Article)
admin.site.register(Info)
admin.site.register(Image)
admin.site.register(Subject)
admin.site.register(BestWorks)
