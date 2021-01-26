class InvalidCardDetailsError(Exception):
    """ raise when Card details are not valid"""


class PaymentFailed(Exception):
    """raise when transaction is failed """


class PaymentGatewayNotAvailableError(Exception):
    """raise when payment gateway is not available"""


class InvalidAmountError(Exception):
    """raise when amount is not valid """
