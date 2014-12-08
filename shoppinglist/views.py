from django.shortcuts import render, get_object_or_404, redirect
from shoppinglist.models import ShoppingItem
from django.contrib.auth import logout
# Create your views here.

#@login_required
def index(request):
  #render list of items
  #print dir(request.user)
  context = {'shopping_items': ShoppingItem.objects.all()}
  return render(request, 'index.html', context)



def create(request):
  if request.method == "POST":
    
    user = request.user
    item_name = request.POST['item_name']
    ShoppingItem.objects.create(name=item_name, user=user)

  return redirect('index')


def update(request):
  if request.method == "POST":
    item_name = request.POST['item_name']
    item_id = request.POST['item_id']
    user = request.user

    item = get_object_or_404(ShoppingItem, pk=item_id)

    item.name = item_name
    item.user = user

    item.save()

  return redirect('index')



def delete(request):
  #we'll just use 
  if request.method == "POST":
    item_id = request.POST['item_id']
    item = get_object_or_404(ShoppingItem, pk=item_id)
    item.delete()

  return redirect('index')


def logout_view(request):
  logout(request)
  return redirect('index')