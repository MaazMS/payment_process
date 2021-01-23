class CreditCardNumberError(Exception):
    """Raised when a CreditCardNumber it should be a invalid credit card number)"""

class CardHolderError(Exception):
    """"Raised when CardHolder should be string"""

class ExpirationDateError(Exception):
    """" DateTime, it cannot be in the past """

class SecurityCodeError(Exception):
    """"Not string, and not  3 digits) """

class AmountError(Exception):
    """"Not decimal amd positive amount """