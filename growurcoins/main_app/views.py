from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from fileinput import filename
from django.shortcuts import render, redirect
from .models import Ad
import datetime
from .models import Cart


# Add the following import
from django.http import HttpResponse

#import boto3 for add photos
import uuid
import boto3
from .models import Ad, Photo

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

#amazon bucket
S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET= 'growurcoinsbucket'

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

#controller to show listing categories
def grow_category(request, category):
    print("incoming wild card value is", category)
    Ads_in_category = Ad.objects.filter(category__contains=category)
    print(Ads_in_category)
    # ad = Ad.objects.get(id=ad_id)
    # print(ad)
    # print("The ad to be rendered is", ad)
    return render(request, 'growurcoins/listing-category.html', {"Ads_in_category":Ads_in_category})
    # return HttpResponse("done")

#controller to create a form for New Ad
def grow_new(request):
    return render(request, 'growurcoins/new.html')
    # return HttpResponse("done")

#controller to create a New Ad in the database
def grow_create(request):
     print("incoming form data", request.POST)
     myad = Ad.objects.create(ad_title=request.POST['ad_title'], 
                       coins=request.POST['coins'], 
                       description=request.POST['description'],
                       offer_date = request.POST['offer_date'],
                       expiry_date = request.POST['expiry_date'],
                       stock_inventory = request.POST['stock_inventory'],
                       category = request.POST['category'],
                       address = request.POST['address'],
                       city = request.POST['city'],
                       postal_code = request.POST['postal_code'],
                       user = request.user
                       )
      
     photo_file = request.FILES.get('photo-file',None)
     print(photo_file, "*****")
     if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        filename = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, filename)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{filename}"
            print(url, filename,myad.id, "*************************")
            Photo.objects.create(url=url, ad_id=myad.id)
      
            # we can assign to cat_id or cat (if you have a cat object)
        except:
            print('An error occurred uploading file to S3')
     return redirect('/growurcoins') #redirect index page.

#controller to add an Ad to a Cart
def grow_add_to_cart(request, ad_id):
     print("incoming ", request.POST)
     mycart = Cart.objects.create(
                        user = request.user,
                        ad = Ad.objects.get(id = ad_id)
                        )
     print("Add has been added to the cart!!!") 
     return redirect('/growurcoins') #redirect index page.

######-------------------------------------------------------
#controller to view all items in Cart
def grow_cart(request):                    
    add_ids_in_cart = Cart.objects.filter(user_id = request.user.id)
    myads = []
    for item in add_ids_in_cart:
        myads.append(Ad.objects.get(id=item.ad_id))

    return render(request, 'growurcoins/cart.html', {"myads": myads} ) #redirect cart page.

######------------------------------------------------------------
#controller to delete the Ad
def grow_delete(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    ad.delete()
    return render(request, 'growurcoins/delete.html', {"ad": ad})

#controller to add photo
def add_photo(request, ad_id):
    #get photo sent by frontend 

    return redirect('detail', ad_id=ad_id)

#controller to home categories
def grow_home(request,):
    listCategories = Ad.objects.values_list('category', flat=True).distinct()
    print(listCategories)
    return render(request, 'growurcoins/home.html',{"listCategories" : listCategories})

def grow_checkout(request,):
    print("user_id", request.user.id) 
    add_ids_in_cart = Cart.objects.filter(user_id = request.user.id)
    myads = []
    
    for item in add_ids_in_cart:
        myads.append(Ad.objects.get(id=item.ad_id))
        
    print(myads)
    ad_coins = [] 
    for ad in myads:
        ad_coins.append(ad.coins)
        print(ad.coins)
    total_coins = sum(ad_coins)
    print(total_coins)


    return render(request, 'growurcoins/thankyou.html', {"total_coins" : total_coins }  )

def grow_delete_cart(request, ):
    print("going back to home menu") 
    print("user_id", request.user.id) 
    add_ids_in_cart = Cart.objects.filter(user_id = request.user.id)
    myads = []
    
    for item in add_ids_in_cart:
        myads.append(Ad.objects.get(id=item.ad_id))
        print("_______________")
        print(item.ad_id)

    for ad in add_ids_in_cart:
        delete_ad = Ad.objects.get(id=ad.ad_id)
        delete_ad.delete()
        print(ad.ad_id)

    print(myads)
    
    return redirect('/growurcoins') #redirect index page.

def grow_search(request):
    if request.method == 'POST':
        searched = request.POST['search']
        Ads = Ad.objects.filter(ad_title__contains=searched)
        return render(request, 'growurcoins/search.html', {'searched': searched, 'Ads': Ads})
    else:
        return redirect('/growurcoins/home') #redirect home page.

    
#####---------

    # def grow_delete(request, ad_id):
    # ad = Ad.objects.get(id=ad_id)
    # ad.delete()
    # return render(request, 'growurcoins/delete.html', {"ad": ad})
