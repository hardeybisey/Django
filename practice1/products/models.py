from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)  # maxlength required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField()
    featured = models.BooleanField(default=True)  # null = True, default= True

    def get_absolute_url(self):
        # f'/products/{self.id}/
        return reverse('products:product_detail', kwargs={'my_id': self.id})
