from flask import Flask, request

app = Flask(__name__)

@app.route('/query1')
def ProcessPayment():

   creditcardnumber = request.args['creditcardnumber']
   cardholder = request.args['cardholder']
   expiration_date = request.args['expiration_date']
   securitycode= request.args['securitycode']
   check_amount = request.args['check_amount']


   return '''<h1>Credit CardNumber: {}</h1>
   cardholder: {} 
   ExpirationDate:{} 
   SecurityCode:{} 
   Amount:{}
   '''.format(creditcardnumber,cardholder,expiration_date,securitycode,check_amount)

if __name__ == '__main__':
    app.run(debug= False)