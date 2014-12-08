from django.shortcuts import render, get_object_or_404, redirect
from shoppinglist.models import ShoppingItem
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
  #render list of items
  #print dir(request.user)
  context = {'shopping_items': ShoppingItem.objects.all()}
  return render(request, 'index.html', context)


@login_required
def create(request):
  if request.method == "POST":
    
    user = request.user
    item_name = request.POST['item_name']
    ShoppingItem.objects.create(name=item_name, user=user)

  return redirect('index')

@login_required
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


def logout_view(request):
  logout(request)
  return redirect('login')


def login_view(request):
  context = {}
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('index')
        else:
            context['flash_error'] = "Warning: Your account has been dissabled."
    else:
        context['flash_error'] = "Invalid username or password."

  return render(request, 'login.html', context)