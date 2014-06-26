from lfs.plugins import PaymentMethodProcessor
from lfs.payment.settings import PM_ORDER_IMMEDIATELY

__author__ = 'ceasaro'


class IdealPaymentMethodProcessor(PaymentMethodProcessor):
    """
    Ideal LFS payment method implementation.

    see also LFS docs:
        http://lightning-fast-shop.readthedocs.org/en/latest/developer/howtos/how_to_add_own_payment_methods.html
    """

    def process(self):
        """
        The process method must return a dictionary with following keys (most of them are optional):

        accepted (mandatory)
            Indicates whether the payment is accepted or not. if this is False the customer keeps on the checkout
            page and gets the message below. If this is True the customer will be redirected to next_url or to LFS'
            thank-you page
        message (optional)
            This message is displayed on the checkout page, when the order is not accepted.
        message_location (optional)
            The location, where the message is displayed.
        next_url (optional)
            The url to which the user is redirect after the payment has been processed. if this is not given
            the customer is redirected to the default thank-you page.
        order_state (optional)
            The state in which the order should be set. It's just PAID. If it's not given the state keeps in SUBMITTED.
        """
        total = self.order.price

        return {
            "accepted": True,
            "next_url": self.get_pay_link(),
        }

    def get_create_order_time(self):
        """
        Returns the time when the order should be created. It is one of:

        PM_ORDER_IMMEDIATELY
            The order is created immediately before the payment is processed.

        PM_ORDER_ACCEPTED
            The order is created when the payment has been processed and
            accepted.
        """
        return PM_ORDER_IMMEDIATELY

    def get_pay_link(self):
        """
        Returns a link to the payment service to pay the current order, which
        is displayed on the thank-you page and the order confirmation mail. In
        this way the customer can pay the order again if something has gone
        wrong.
        """
        # iDEAL requires a POST while LFS performs a GET
        # We redirect to a form that performs a POST to iDEAL

        return "/ideal/order/%s" % self.order.uuid


