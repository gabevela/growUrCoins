from fileinput import filename
from django.shortcuts import render, redirect
from .models import Ad
import datetime

# Add the following import
from django.http import HttpResponse

#import boto3 for add photos
import uuid
import boto3
from .models import Ad, Photo

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
                       street_number = request.POST['street_number'],
                       street_name = request.POST['street_name'],
                       city = request.POST['city'],
                       postal_code = request.POST['postal_code'],
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

#controller to delete the Ad
def grow_delete(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    ad.delete()
    return render(request, 'growurcoins/delete.html', {"ad": ad})


#controller to add photo
def add_photo(request, ad_id):
    #get photo sent by frontend 

    return redirect('detail', ad_id=ad_id)
