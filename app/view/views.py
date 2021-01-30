from flask import Flask, request, Response
from controller import payment
from controller.payment import (
    InvalidCardDetailsError,
    InvalidAmountError,
    PaymentFailed,
)


app = Flask(__name__)


@app.route("/process_payment/", methods=["POST"])
def process_payment():
    """
    This function take json data for payment process.
    :return: It  Payment successful and if payment failed it return response status 400 and 500
    """
    try:
        card_details = request.get_json()
        credit_card_number = card_details.get("credit_card_number")
        card_holder = card_details.get("card_holder")
        expiration_date = card_details.get("expiration_date")
        security_code = card_details.get("security_code")
        amount = card_details.get("amount")
        payment_details = payment.process_payment(
            credit_card_number, card_holder, expiration_date, security_code, amount
        )
        return Response("Payment is processed", status=200)

    except InvalidCardDetailsError as e:
        return Response("Card details invalid", status=400)

    except InvalidAmountError as e:
        return Response("Amount invalid", status=400)

    except PaymentFailed as e:
        return Response("Payment failed", status=400)

    except Exception as e:
        # TODO log(e)
        return Response("internal server error", status=500)
