# Create your views here.
from django.http.response import HttpResponse
from lfs.caching.utils import lfs_get_object_or_404
from lfs.cart.models import CartItem
from lfs.cart.views import cart as cart_view
from lfs.cart.utils import get_cart
from lfs.core.signals import cart_changed

def delete_cart_item(request, cart_item_id):
    """
    Deletes the cart item with the given id.
    """
    lfs_get_object_or_404(CartItem, pk=cart_item_id).delete()

    cart = get_cart(request)
    cart_changed.send(cart, request=request)

    return HttpResponse(cart_view(request))
