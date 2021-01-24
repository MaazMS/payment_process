from base.customer_information.customer import CardDetails
from pydantic import ValidationError
from controller.exception import InvalidCardDetailsError, RetryTransactionError, PaymentFailed, \
    PaymentGatewayNotAvailableError, InvalidAmountError
from controller.constants import PaymentGateways
from base.gateways.payment_gateways import PremiumPaymentGateway, CheapPaymentGateway, ExpensivePaymentGateway


def process_payment(credit_card_number, card_holder, expiration_date, security_code, amount):
    try:
        card_details = CardDetails(
            card_number=credit_card_number,
            customer_name=card_holder,
            exp_date=expiration_date,
            cvv=security_code,

        )

    except ValidationError as e:
        # TODO log(e)
        raise InvalidCardDetailsError("Card details are not valid ")

    try:

        if not int(amount) >= 0:
            raise InvalidAmountError("Amount Invalid")
    except InvalidAmountError as e:
        # TODO log(e)
        raise InvalidAmountError

    target_card_details = card_details.get_card_details()
    if int(amount) <= PaymentGateways.CHEAP_PAYMENT_GATEWAY_LIMIT.value:
        try:
            cheap_payment_gateway = CheapPaymentGateway()
            cheap_payment_gateway.create_transaction(**target_card_details)
        except Exception as e:
            # TODO log(e)
            raise PaymentFailed("Transaction  failed")

    elif (int(amount) >= PaymentGateways.EXPENSIVE_PAYMENT_GATEWAY_LIMIT.value) and (
            int(amount) <= PaymentGateways.PREMIUM_PAYMENT_GATEWAY_LIMIT.value):
        try:
            expensive_payment_gateway = ExpensivePaymentGateway()
            expensive_payment_gateway.create_transaction()
        except PaymentGatewayNotAvailableError as e:
            # TODO log(e)
            try:
                cheap_payment_gateway = CheapPaymentGateway()
                cheap_payment_gateway.create_transaction(**target_card_details)
            except Exception as e:
                # TODO: log(e)
                raise PaymentFailed("Transaction failed")

    elif int(amount) >= PaymentGateways.PREMIUM_PAYMENT_GATEWAY_LIMIT.value:
        try:
            premium_payment_gateway = PremiumPaymentGateway()
            transaction_status = premium_payment_gateway.create_transaction(**target_card_details)
            if not transaction_status:
                raise RetryTransactionError("Transaction failed")
            try:
                premium_payment_gateway = PremiumPaymentGateway()
                premium_payment_gateway.is_payment_failed()
            except RetryTransactionError as e:
                # TODO log(e)
                raise RetryTransactionError("Retry Transaction failed")
        except Exception as e:
            # TODO log(e)
            raise PaymentFailed("Transaction failed")