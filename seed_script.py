from django.contrib.auth.models import User
from shoppinglist.models import ShoppingItem

john = User.objects.create_user('john', 'john@example.com', 'abc123')
joan = User.objects.create_user('joan', 'joan@example.com', 'abc123')
suzy = User.objects.create_user('suzy', 'suzy@example.com', 'abc123')
billy = User.objects.create_user('billy', 'billy@example.com', 'abc123')

ShoppingItem.objects.create('tomatoes', john)
ShoppingItem.objects.create('cookies', john)
ShoppingItem.objects.create('kale', joan)
ShoppingItem.objects.create('potatoes', suzy)
ShoppingItem.objects.create('tacos', billy)

