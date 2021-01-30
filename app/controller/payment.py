from base.customer_information.customer import CardDetails
from pydantic import ValidationError
from controller.exception import (
    InvalidCardDetailsError,
    PaymentFailed,
    PaymentGatewayNotAvailableError,
    InvalidAmountError,
)
from controller.constants import PaymentGateways
from base.gateways.payment_gateways import (
    PremiumPaymentGateway,
    CheapPaymentGateway,
    ExpensivePaymentGateway,
)


def process_payment(
    credit_card_number, card_holder, expiration_date, security_code, amount
):
    """
    :param credit_card_number:
    :param card_holder:
    :param expiration_date:
    :param security_code:
    :param amount:
    :return: flag and string
     flag : Flag show the status of payment which are true means payment successful and false means payment failed
    string : The string are show that payment successful with payment gateway name
    """

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

    if not int(amount) >= 0:
        raise InvalidAmountError("Amount Invalid")

    target_card_details = card_details.get_card_details()
    if int(amount) <= PaymentGateways.CHEAP_PAYMENT_GATEWAY_LIMIT.value:
        try:
            cheap_payment_gateway = CheapPaymentGateway()
            cheap_payment_gateway.create_transaction(**target_card_details)
            return True, PaymentGateways.CHEAP_PAYMENT_GATEWAY
        except Exception as e:
            # TODO log(e)
            raise PaymentFailed("Transaction  failed")

    elif (int(amount) >= PaymentGateways.EXPENSIVE_PAYMENT_GATEWAY_LIMIT.value) and (
        int(amount) <= PaymentGateways.PREMIUM_PAYMENT_GATEWAY_LIMIT.value
    ):
        try:
            expensive_payment_gateway = ExpensivePaymentGateway()
            expensive_payment_gateway.create_transaction()
            return True, PaymentGateways.EXPENSIVE_PAYMENT_GATEWAY
        except PaymentGatewayNotAvailableError as e:
            # TODO log(e)
            try:
                cheap_payment_gateway = CheapPaymentGateway()
                cheap_payment_gateway.create_transaction(**target_card_details)
                return True, PaymentGateways.CHEAP_PAYMENT_GATEWAY
            except Exception as e:
                # TODO: log(e)
                raise PaymentFailed("Transaction failed")

    elif int(amount) >= PaymentGateways.PREMIUM_PAYMENT_GATEWAY_LIMIT.value:
        retry = 0
        while retry < 3:
            try:
                premium_payment_gateway = PremiumPaymentGateway()
                premium_payment_gateway.create_transaction(**target_card_details)
                return True, PaymentGateways.PREMIUM_PAYMENT_GATEWAY
            except Exception as e:
                # TODO log(e)
                if retry == 3:
                    raise PaymentFailed("Transaction failed")
            retry += 1
