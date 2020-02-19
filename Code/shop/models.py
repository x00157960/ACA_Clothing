from django.db import models

class Category(models.Model):
    name = models.TextField()

    def get_products(self):
        return Product.objects.filter(category=self)

    def __str__(self):
        return self.name

"""def get_absolute_url(self):
return reverse('product_list_by_category',args=[self.id])"""


class Product(models.Model):
    name = models.TextField()
    """image = models.ImageField(upload_to='images/', blank=True)
    image_thumbnail = ImageSpecField(source='image',
    processors=[ResizeToFill(50, 50)],
    format='JPEG',
    options={'quality':60})"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
