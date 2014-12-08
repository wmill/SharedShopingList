from django.contrib.auth.models import User
from shoppinglist.models import ShoppingItem

john = User.objects.create_user('john', 'john@example.com', 'abc123')
joan = User.objects.create_user('joan', 'joan@example.com', 'abc123')
suzy = User.objects.create_user('suzy', 'suzy@example.com', 'abc123')
billy = User.objects.create_user('billy', 'billy@example.com', 'abc123')

ShoppingItem.objects.create(name='tomatoes', user=john)
ShoppingItem.objects.create(name='cookies', user=john)
ShoppingItem.objects.create(name='kale', user=joan)
ShoppingItem.objects.create(name='potatoes', user=suzy)
ShoppingItem.objects.create(name='tacos', user=billy)
