from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.
class Presenter(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(get_user_model(),
                      on_delete=models.CASCADE,
                      related_name='presenters')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('attendee_detail', args=[str(self.id)])


