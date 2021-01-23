from flask import Flask, request
from app.validator import ValidateCardInfo


app = Flask(__name__)

@app.route('/ProcessPayment', methods=['GET'])
def ProcessPayment():

   # credit_card_number = request.args['creditcardnumber']
   # card_holder = request.args['cardholder']
   # expiration_date = request.args['expiration_date']
   # security_code= request.args['securitycode']
   amount = request.args['amount']

   # credit_card_number_info = ValidateCardInfo.credit_card_number(credit_card_number)
   # card_holder_info = ValidateCardInfo.card_holder(card_holder)
   # expiration_date_info = ValidateCardInfo.expiration_date(expiration_date)
   # security_code_info = ValidateCardInfo.security_code(security_code)
   amount_info = ValidateCardInfo.check_amount(amount)

   return '''
          Amount:{} '''.format(amount_info)


if __name__ == '__main__':
    app.run(debug= False)