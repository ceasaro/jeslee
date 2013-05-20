# Create your views here.
from django.core.mail import send_mail
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from lfs.caching.utils import lfs_get_object_or_404
from lfs.cart.models import CartItem
from lfs.cart.views import cart as cart_view, cart_inline
from lfs.cart.utils import get_cart
from lfs.core.signals import cart_changed


def cart(request, template_name="lfs/cart/cart.html"):
    """
    The main view of the cart.
    """
    return render_to_response(template_name, RequestContext(request, {
        "voucher_number": lfs.voucher.utils.get_current_voucher_number(request),
        "shopping_url": request.META.get("HTTP_REFERER", "/"),
        "cart_inline": cart_inline(request),
        }))

def delete_cart_item(request, cart_item_id):
    """
    Deletes the cart item with the given id.
    """
    lfs_get_object_or_404(CartItem, pk=cart_item_id).delete()

    cart = get_cart(request)
    cart_changed.send(cart, request=request)

    return HttpResponse(cart_view(request))

def test_email(request):
    send_mail('Subject here', 'Here is the message.', 'from@example.com',
        ['ceesvw@gmail.com'], fail_silently=False)
#    send_customer_added(user=request.user)