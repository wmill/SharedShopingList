from django.shortcuts import render, get_object_or_404
from shoppinglist.models import ShoppingItem
# Create your views here.

#@login_required
def index(request):
  if request.method == "POST":
    #creating or updating an item
    
    user = request.user
    item_name = request.POST['item_name']
    ShoppingItem.objects.create(name=item_name, user=user)


  return defaultIndex(request)


def defaultIndex(request):
  #render list of items
  #print dir(request.user)
  context = {'shopping_items': ShoppingItem.objects.all()}
  return render(request, 'index.html', context)

def create(request):
  if request.method == "POST":
    
    user = request.user
    item_name = request.POST['item_name']
    ShoppingItem.objects.create(name=item_name, user=user)


def update(request):
  pass

def delete(request):
  #we'll just use 
  if request.method == "POST":
    pass