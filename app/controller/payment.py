from base.customer_information.customer import CardDetails
from pydantic import ValidationError
from controller.exception import InvalidCardDetailsError, RetryTransectionError, PaymentFailed
from controller.constants import PaymentGateways
from base.gateways.payment_gateways import PremiumPaymentGateway, CheapPaymentGateway, ExpensivePaymentGateway


def process_payment_validation(credit_card_number, card_holder, expiration_date, security_code, amount):
    try:
        card_validation =  CardDetails(
        card_number= credit_card_number,
        customer_name= card_holder,
        exp_date= expiration_date,
        cvv= security_code,

        )

    except ValidationError as e:
            raise InvalidCardDetailsError ("Card details are not valid ")


    if int(amount) <= PaymentGateways.CHEAP_PAYMENT_GATEWAY_LIMIT.value:
        try:
            money = CheapPaymentGateway()
            money.create_transection()
        except:
            raise  PaymentFailed("transection is failed")

    elif (int(amount) >= PaymentGateways.EXPENSIVE_PAYMENT_GATEWAY_LIMIT.value) and (
            int(amount) <= PaymentGateways.PREMIUM_PAYMENT_GATEWAY_LIMIT.value):
        try :
            money = ExpensivePaymentGateway()
            transection_status=money.create_transection()
            if not transection_status :
                raise RetryTransectionError ("Expensive Payment Gateway not available")
            try:
                money = CheapPaymentGateway()
                money.is_available()
            except :
                raise RetryTransectionError("Cheap Payment Gateway not available")
        except:
            raise PaymentFailed("transection is failed")

    elif int(amount) >= PaymentGateways.PREMIUM_PAYMENT_GATEWAY_LIMIT.value:
        try:
            money = PremiumPaymentGateway()
            transection_status = money.create_transection()
            if not transection_status :
                raise RetryTransectionError ("Transection failed")
            try:
                money = PremiumPaymentGateway()
                money.is_payment_failed()
            except :
                raise RetryTransectionError("Cheap Payment Gateway not available")
        except:
            raise  PaymentFailed ("transection is failed")


