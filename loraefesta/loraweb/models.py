from django.db import models
from django.utils.translation import ugettext_lazy as _

class Collection(models.Model):
    name = models.CharField(max_length=130,verbose_name = _('name'),)
    title = models.CharField(max_length=130,verbose_name = _('title'),)
    slug = models.SlugField(max_length=50,verbose_name = _('slug'),)
    abstract  = models.CharField(max_length=255,verbose_name = _('abstract'),)
    media = models.ImageField(upload_to="collection",verbose_name = _('media'),)
    pub = models.BooleanField()
    pub_order = models.SmallIntegerField()

    class Meta:
        verbose_name = _('collection')
        verbose_name_plural = _('collection')

class Yarn(models.Model):
    collection = models.ForeignKey(Collection)
    name = models.CharField(max_length=130,verbose_name = _('name'),)
    title = models.CharField(max_length=130,verbose_name = _('title'),)
    slug = models.SlugField(max_length=50,verbose_name = _('slug'),)
    abstract  = models.CharField(max_length=255,verbose_name = _('abstract'),)	
    text = models.TextField(verbose_name = _('text'),)
    media = models.ImageField(upload_to="yarn",verbose_name = _('media'),)
    pub = models.BooleanField(verbose_name = _('media'),)
    pub_order = models.SmallIntegerField(verbose_name = _('media'),)
    class Meta:
        verbose_name = _('yarn')
        verbose_name_plural = _('yarn')

class News(models.Model):
    title = models.CharField(max_length=130,verbose_name = _('title'),)
    abstract  = models.CharField(max_length=255,verbose_name = _('abstract'),)
    slug = models.SlugField(max_length=50,verbose_name = _('slug'),)	
    date = models.DateField(verbose_name = _('date'),)
    text = models.TextField(verbose_name = _('text'),) 
    media = models.ImageField(upload_to="news",verbose_name = _('media'),)
    pub = models.BooleanField(verbose_name = _('pub'),)
    pub_order = models.SmallIntegerField(verbose_name = _('pub_order'),)

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')


