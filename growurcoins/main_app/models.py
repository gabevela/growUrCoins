from django.db import models
from platformdirs import user_config_dir
from django.contrib.auth.models import User

# Create your models here.

#Relationships: #always put the FK on many side.
# ONE Cart will have MANY Ads (FK = cart_id)
# ONE User will have ONE Cart
# ONE User will have MANY Ads (FK = user_id)
# ONE User will have MANY REVIEWS(FK = user_id)

class Ad(models.Model): #this model is missing the FK, user_id from the usertable
    # user_id = models.  #this is the FK from the User table
    ad_title = models.CharField(max_length=15)
    coins = models.IntegerField()
    description = models.TextField(max_length=250)
    offer_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    stock_inventory = models.IntegerField()
    picture_one = models.URLField(max_length=200)
    category = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    def __str__(self):
        return self.ad_title
            
class Cart(models.Model):
    quantity = models.IntegerField()
    total_cost = models.IntegerField()
    # user_id: models.
    # ad_id: 

class Reviews(models.Model):
    ratings = models.IntegerField()
    feedback = models.TextField(max_length=250)

#class User(models.Model):
#     username = models.CharField(15)
#     password = models.CharField(8)
#     email = models.CharField(50)
#     first_name = models.CharField(15)
#     last_name = models.CharField(15)
#     # cart_id:models.IntegerField()  #FK of Cart table
#     # coins
