from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pets:pet_list_by_category',
                       args=[self.slug])


class Pet(models.Model):
    category = models.ForeignKey(Category, related_name='pets', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    breed = models.CharField(max_length=20, blank=True, null=True,default=' ')
    color = models.CharField(max_length=20, blank=True, null=True,default=' ')
    age = models.IntegerField(default=' ')
    gender = models.CharField(max_length=10, default='')
    size = models.CharField(max_length=15, default='')
    weight = models.CharField(max_length=15, default='')
    adoption_fee = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    description = models.CharField(max_length=150, default=' ')
    image = models.ImageField(upload_to='pets/%Y/%m/%d',
                              blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('pets:pet_detail',
                       args=[self.id, self.slug])

class donation(models.Model):
    braintree_id = models.CharField(max_length=150,blank=True)


