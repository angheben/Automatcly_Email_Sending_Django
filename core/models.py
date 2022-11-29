from django.db import models
from stdimage import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    creation = models.DateField(name='Creation', auto_now_add=True)
    modification = models.DateField(name='Modification', auto_now=True)
    active = models.BooleanField(name='Active?', default=True)

    class Meta:
        abstract = True


class Product(Base):
    name = models.CharField(name='Name', max_length=100)
    price = models.DecimalField(name='Price', max_digits=8, decimal_places=2)
    stock = models.IntegerField(name='Stock')
    image = StdImageField(name='Image', upload_to='Products', variations={'thumb': (124, 124)})
    slug = models.SlugField(name='Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name


def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(product_pre_save, sender=Product)
