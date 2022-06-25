from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Growurcoin:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

growurcoins = [
Growurcoin('Lolo', 'tabby', 'foul little demon', 3),
Growurcoin('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
Growurcoin('Raven', 'black tripod', '3 legged cat', 4),
]

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')
#   return HttpResponse('<h1>About the GrowUrCoins</h1>')

def grow_index(request):
  return render(request, 'growurcoins/index.html', { 'growurcoins': growurcoins })