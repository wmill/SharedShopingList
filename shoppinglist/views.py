from django.shortcuts import render, get_object_or_404, redirect
from shoppinglist.models import ShoppingItem
from django.contrib.auth import logout
from django.http import HttpResponse


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
  #this method also deletes
  if request.method == "POST":
    item_name = request.POST['item_name']
    item_id = request.POST['item_id']
    user = request.user

    item = get_object_or_404(ShoppingItem, pk=item_id)

    print request.POST

    if 'submit' in request.POST:
      item.name = item_name
      item.user = user

      item.save()

    elif 'delete' in request.POST:
      item.delete()

    else:
      #form action missing
      #TODO raise a 400 error
      print "bad request"
      pass

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
  return redirect('login_view')