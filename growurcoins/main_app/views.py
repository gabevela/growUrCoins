from django.shortcuts import render, redirect
from .models import Ad
import datetime

# Add the following import
from django.http import HttpResponse

#logic to add classes instead

# class Growurcoin:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# growurcoins = [
# Growurcoin('Lolo', 'tabby', 'foul little demon', 3),
# Growurcoin('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
# Growurcoin('Raven', 'black tripod', '3 legged cat', 4),
# ]

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')
#   return HttpResponse('<h1>About the GrowUrCoins</h1>')

#controller to show all Ads
def grow_index(request):
    ad = Ad.objects.all()
    print(ad)
    return render(request, 'growurcoins/index.html', { 'ad': ad })

#controller to show specific Ad
def grow_details(request, ad_id):
    print("incoming wild card value is", ad_id)
    ad = Ad.objects.get(id=ad_id)
    print(ad)
    print("The ad to be rendered is", ad)
    return render(request, 'growurcoins/detail.html', {"ad": ad} )
    # return HttpResponse("done")

#controller to create a form for New Ad
def grow_new(request):
    return render(request, 'growurcoins/new.html')
    # return HttpResponse("done")

#controller to create a New Ad in the database
def grow_create(request):
     print("incoming form data", request.POST)
     Ad.objects.create(ad_title=request.POST['ad_title'], 
                       coins=request.POST['coins'], 
                       description=request.POST['description'],
                       offer_date = request.POST['offer_date'],
                       expiry_date = request.POST['expiry_date'],
                       stock_inventory = request.POST['stock_inventory'],
                       picture_one = request.POST['picture_one'],
                       category = request.POST['category'],
                       street_number = request.POST['street_number'],
                       street_name = request.POST['street_name'],
                       city = request.POST['city'],
                       postal_code = request.POST['postal_code'],
                       )
     return redirect('/growurcoins') #redirect index page.

