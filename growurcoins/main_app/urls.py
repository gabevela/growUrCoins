from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('growurcoins/', views.grow_index, name='index'), #shows the index of all Ads
 path('growurcoins/<int:ad_id>', views.grow_details, name='details'),   #Details of a specific Ad
 path('growurcoins/new', views.grow_new, name='new'), # url to show "create ad" form
 path('growurcoins/create', views.grow_create, name='create'), #this will save the "create ad" form into the database
 path('growurcoins/<int:ad_id>/delete', views.grow_delete, name='delete'),   #Delete a specific Ad
 path('growurcoins/<int:ad_id>/add_photo/', views.add_photo, name='add_photo'), #add photo in new 
 path('accounts/signup/', views.signup, name='signup'),
 path('growurcoins/listing/<str:category>', views.grow_category, name='details'), 
 path('growurcoins/home', views.grow_home, name='home'), #shows the home of all categories
 path('growurcoins/<int:ad_id>/add_to_cart', views.grow_add_to_cart, name='add_to_cart'), #this will save the "ad" into the logged in user's cart model in the database 
 path('growurcoins/cart', views.grow_cart, name='cart'), #this will take us to the cart  
 path('growurcoins/checkout', views.grow_checkout, name='thankyou'), #this will checkout the cart   
 #path('growurcoins/thankyou', views.grow_thankyou, name='thankyou'), #this will checkout the cart   

]
