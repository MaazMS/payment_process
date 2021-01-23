from  flask import Flask, request, jsonify
from controller.card import credit_card_details


app = Flask(__name__)


@app.route('/', methods = ['POST'])
def process_payment():

    credit_card_number = request.args.get("creditcardnumber")
    card_holder = request.args.get("cardholder")
    expiration_date = request.args.get("expiration_date")
    security_code = request.args.get("security_code")
    amount = request.args.get("amount")
    payment_details = credit_card_details(credit_card_number, card_holder, expiration_date, security_code, amount)
    return jsonify(payment_details)
