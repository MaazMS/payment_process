from enum import Enum


class PaymentGateways(Enum):
    """ "
    This class have constant variable which is use to define payment gateway limit and payment gateway name.
    """

    CHEAP_PAYMENT_GATEWAY_LIMIT = 20
    EXPENSIVE_PAYMENT_GATEWAY_LIMIT = 21
    PREMIUM_PAYMENT_GATEWAY_LIMIT = 500
    CHEAP_PAYMENT_GATEWAY = " Cheap payment gateway"
    EXPENSIVE_PAYMENT_GATEWAY = "Expensive payment gateway "
    PREMIUM_PAYMENT_GATEWAY = "Premium payment gateway"
