from sre_parse import CATEGORIES
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

#Relationships: #always put the FK on many side.
# ONE Cart will have MANY Ads (FK = cart_id)
# ONE User will have ONE Cart
# ONE User will have MANY Ads (FK = user_id)
# ONE User will have MANY REVIEWS(FK = user_id)

CATEGORIES = (
    "Green Beans",
    "Lettuce", "Peas", "Carrots", "Cucumbers",
)

class Ad(models.Model): #this model is missing the FK, user_id from the usertable
    # user_id = models.  #this is the FK from the User table
    ad_title = models.CharField(max_length=15)
    coins = models.IntegerField()
    description = models.TextField(max_length=250)
    offer_date = models.DateField()
    expiry_date = models.DateField()
    stock_inventory = models.IntegerField()
    picture_one = models.URLField(max_length=200)
    category = models.CharField(choices=CATEGORIES),
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ad_title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.category_name

class Photo(models.Model):
    url = models.CharField(max_length=200)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    def __str__(self):
        return f"Photo for ad_id: {self.ad_id} @{self.url}"
            
class Cart(models.Model):
    quantity = models.IntegerField()
    total_cost = models.IntegerField()
    # user_id: models.
    # ad_id: 

class Reviews(models.Model):
    ratings = models.IntegerField()
    feedback = models.TextField(max_length=250)


