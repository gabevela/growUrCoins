from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('growurcoins/', views.grow_index, name='index'), #shows the index of all Ads
    path('growurcoins/home', views.grow_home, name='home'), #shows the home of all categories
    path('growurcoins/<int:ad_id>', views.grow_details, name='details'),   #Details of a specific Ad
    path('growurcoins/new', views.grow_new, name='new'), # url to show "create ad" form
    path('growurcoins/create', views.grow_create, name='create'), #this will save the "create ad" form into the database
    path('growurcoins/<int:ad_id>/delete', views.grow_delete, name='delete'),   #Delete a specific Ad
    path('growurcoins/<int:ad_id>/add_photo/', views.add_photo, name='add_photo'), #add photo in new
    path('growurcoins/listing/<str:category>', views.grow_category, name='details'),   #Details of a specific Ad
]

