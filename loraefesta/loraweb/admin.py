from django.contrib import admin
from models import Collection, Yarn, News
from modeltranslation.admin import TranslationAdmin

class NewsAdmin(TranslationAdmin):
    pass

admin.site.register(News, NewsAdmin)

class CollectionAdmin(TranslationAdmin):
    pass

admin.site.register(Collection, CollectionAdmin)

class YarnAdmin(TranslationAdmin):
    pass

admin.site.register(Yarn, YarnAdmin)