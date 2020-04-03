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

    def get_absolute_url(self):
        return reverse('product_list_by_category',args=[self.id])

    
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
    one_star = models.IntegerField(null=True)
    two_star = models.IntegerField(null=True)
    three_star = models.IntegerField(null=True)
    four_star = models.IntegerField(null=True)
    five_star = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def get_one_star(self):
        star_total = self.one_star + self.two_star + self.three_star + self.four_star + self.five_star
        one_star_total = 100 * (self.one_star / star_total)
        return one_star_total

    def get_two_star(self):
        star_total = self.one_star + self.two_star + self.three_star + self.four_star + self.five_star
        two_star_total = 100 * (self.two_star / star_total)
        return two_star_total

    def get_three_star(self):
        star_total = self.one_star + self.two_star + self.three_star + self.four_star + self.five_star
        three_star_total = 100 * (self.three_star / star_total)
        return three_star_total

    def get_four_star(self):
        star_total = self.one_star + self.two_star + self.three_star + self.four_star + self.five_star
        four_star_total = 100 * (self.four_star / star_total)
        return four_star_total

    def get_five_star(self):
        star_total = self.one_star + self.two_star + self.three_star + self.four_star + self.five_star
        five_star_total = 100 * (self.five_star / star_total)
        return five_star_total