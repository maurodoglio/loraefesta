from modeltranslation.translator import translator, TranslationOptions
from models import Collection, Yarn, News

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'abstract','text')

translator.register(News, NewsTranslationOptions)


class CollectionTranslationOptions(TranslationOptions):
    fields = ('name','title', 'abstract')

translator.register(Collection, CollectionTranslationOptions)

class YarnTranslationOptions(TranslationOptions):
    fields = ('name','title', 'abstract','text')

translator.register(Yarn, YarnTranslationOptions)

