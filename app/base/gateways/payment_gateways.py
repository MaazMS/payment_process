from controller.exception import PaymentGatewayNotAvailableError


class CheapPaymentGateway:
    def create_transaction(self, **kwargs):
        """
        :param kwargs: This function take card details for transaction.
        :return: Transaction successful
        """

        return True


class ExpensivePaymentGateway:
    def create_transaction(self, **kwargs):
        """
        :param kwargs: This function take card details for transaction.
        :return: Transaction successful if payment gateway is not available it create one transaction from cheap payment
        gateway and if payment is failed it raise exception
        """
        try:
            return True
        except PaymentGatewayNotAvailableError as e:
            # TODO: log(e)
            raise PaymentGatewayNotAvailableError(
                "Expensive PaymentGateway is unavailable at this moment"
            )
        except Exception as e:
            raise e


class PremiumPaymentGateway:
    def create_transaction(self, **kwargs):
        """
        :param kwargs: This function take card details for transaction.
        :return: Transaction successful if transaction is failed retry 3 transaction.
        """

        return True
