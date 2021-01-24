from flask import Flask, request, Response
from controller import payment
from controller.payment import InvalidCardDetailsError, InvalidAmountError, PaymentFailed, RetryTransactionError, PaymentGatewayNotAvailableError


app = Flask(__name__)


@app.route('/payment_info/', methods=['POST'])
def process_payment():
    try:
        card_details = request.get_json()
        credit_card_number = card_details.get("credit_card_number")
        card_holder = card_details.get("card_holder")
        expiration_date = card_details.get("expiration_date")
        security_code = card_details.get("security_code")
        amount = card_details.get("amount")
        payment_details = payment.process_payment(credit_card_number, card_holder, expiration_date, security_code, amount)
        return Response("Payment is processed", status=200)

    except InvalidCardDetailsError as e:
        return Response("The request is invalid", status=400)

    except InvalidAmountError as e:
        return Response("The request is invalid", status=400)

    except PaymentFailed as e:
        return Response("The request is invalid", status=400)

    except RetryTransactionError as e:
        return Response("The request is invalid", status=400)

    except PaymentGatewayNotAvailableError as e:
        return Response("The request is invalid", status=400)


    except Exception as e:
        # TODO log(e)
        return Response("internal server error", status=500)

