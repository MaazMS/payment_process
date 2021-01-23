from  flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def process_payment():
    credit_card_number = request.args.get("creditcardnumber")
    card_holder = request.args.get("cardholder")
    expiration_date = request.args.get("expiration_date")
    security_code = request.args.get("security_code")
    amount = request.args.get("amount")
    return jsonify(credit_card_number, card_holder, expiration_date, security_code, amount)
