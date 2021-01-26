from controller.exception import PaymentGatewayNotAvailableError


class CheapPaymentGateway:
    repeat = 0

    def create_transaction(self, **kwargs):
        return True

    def is_available(self):
        while self.repeat == 0:
            CheapPaymentGateway.repeat += 1
            break
        return False


class ExpensivePaymentGateway:

    def create_transaction(self, **kwargs):
        try:
            return True
        except PaymentGatewayNotAvailableError as e:
            # TODO: log(e)
            raise PaymentGatewayNotAvailableError("Expensive PaymentGateway is unavailable at this moment")
        except Exception as e:
            raise e


class PremiumPaymentGateway:

    def create_transaction(self, **kwargs):
        return True

