from controller.constants import PaymentGateways


class BasePaymentGateway:
    def __init__(self, repeat=0):
        self.repeat = repeat

class PremiumBasePaymentGateway(BasePaymentGateway):
    def __init__(self, repeat=3):
        print("PremiumPaymentGateway")
        super(PremiumBasePaymentGateway, self).__init__(repeat)

class ExpensiveBasePaymentGateway(BasePaymentGateway):
    def __init__(self, repeat=1):
        print("ExpensiveBasePaymentGateway")
        super(ExpensiveBasePaymentGateway, self).__init__(repeat)

class CheapBasePaymentGateway(BasePaymentGateway):
    def __init__(self, repeat=0):
        print("CheapBasePaymentGateway")
        super(CheapBasePaymentGateway, self).__init__(repeat)


class ValidatePaymentGateways(BasePaymentGateway):

    def type_payment_geteways(amount):
        if amount <= PaymentGateways.CHEAP_PAYMENT_GATEWAY_LIMIT.value:
            CheapBasePaymentGateway()
        elif (amount >= PaymentGateways.EXPENSIVE_PAYMENT_GATEWAY_LIMIT.value) and (
                amount <= PaymentGateways.PREMIUM_PAYMENT_GATEWAY_LIMIT.value):
            ExpensiveBasePaymentGateway()
        elif amount >= PaymentGateways.PREMIUM_PAYMENT_GATEWAY_LIMIT.value:
            PremiumBasePaymentGateway()