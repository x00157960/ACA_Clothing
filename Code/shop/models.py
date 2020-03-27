from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Category(models.Model):
    name = models.TextField()
    products = models.ManyToManyField('Product') 

    class Meta:
        verbose_name_plural = "Categories"

    def get_products(self):
        return Product.objects.filter(category=self)

    def __str__(self):
        return self.name 

    #def get_absolute_url(self):
        #return reverse('product_list_by_category',args=[self.id])

    
class Product(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(400, 400)],
                                format='JPEG',
                                options={'quality':60})
    description = models.TextField()
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
