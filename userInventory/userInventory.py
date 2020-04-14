from decimal import Decimal
from django.conf import settings
from shop.models import Product

class UserInventory(object):

    def __init__(self, request):
        """
        Initialize the inventory.
        """
        self.session = request.session
        inventory = self.session.get(settings.INVENTORY_SESSION_ID)
        if not inventory:
            # save an empty inventory in the session
            inventory = self.session[settings.INVENTORY_SESSION_ID] = {}
        self.inventory = inventory

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the inventory or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.inventory:
            self.inventory[product_id] = {'quantity': 0,
                                      'price': str(product.price)}
        if update_quantity:
            self.inventory[product_id]['quantity'] = quantity
        else:
            self.inventory[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update the session inventory
        self.session[settings.INVENTORY_SESSION_ID] = self.inventory
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
      """
      Remove a product from the inventory.
      """
      product_id = str(product.id)
      if product_id in self.inventory:
          del self.inventory[product_id]
          self.save()

    def __iter__(self):
        """
        Iterate over the items in the inventory and get the products 
        from the database.
        """
        product_ids = self.inventory.keys()
        # get the product objects and add them to the inventory
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.inventory[str(product.id)]['product'] = product

        for item in self.inventory.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item          

    def __len__(self):
        """
        Count all items in the inventory.
        """
        return sum(item['quantity'] for item in self.inventory.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.inventory.values())

    def clear(self):
      # remove cart from session
      del self.session[settings.INVENTORY_SESSION_ID]
      self.session.modified = True