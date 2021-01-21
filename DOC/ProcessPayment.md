### ProcessPayment
1. ProcessPayment method is receive request.   
* To access the incoming data in Flask, you have to use the request object. 
* String begins after the question mark (?)
* Two key-value pairs separated by an ampersand (&).  
* key is followed by an equals sign (=) and then the value.   

``` 
@app.route('/query1')
def ProcessPayment():
    p1 = request.args.get('payment1')  # or  p1 = request.args['payment1'] same
    return '''<h1>The payment value is: {}</h1>'''.format(p1)

```
**http://127.0.0.1:5000/query1?payment1=1000**
* payment1 is the key 
* 1000 is value 
method 1 
* if key doesn't exist, returns None
example1
`http://127.0.0.1:5000/query1?pay=1000`   
* because `payment1` is the key not `pay`     

method 2   
`p1 = request.args['payment1']`  
* if key is not exist it will return a 400 error.   
` 400 Bad Request: The browser (or proxy) sent a request that this server could not understand.`    

##### any error : 500 internal server error
* Wrong syntax `request.arg`  
* If I am use `p1 = request.arg['payment1']` 
* pass correct url `http://127.0.0.1:5000/query1?payment1=200`
``` 
Internal Server Error
The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
``` 

##### The request is invalid 400 Bad Request 
* if I am use `p1 = request.args['payment1']` 
* pass wrong key in url `http://127.0.0.1:5000/query1?pay=200`
` 400 Bad Request: The browser (or proxy) sent a request that this server could not understand.
KeyError: 'payment1'`  

#### CreditCardNumber Validation
1. Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm.  
2. real-life applications to test credit or debit card numbers as well as SIM card serial numbers.  
3. input into a list of numbers,it easier to work.   
4. strip() which will take care of any extra whitespace.    
5. reverse() is reverse string 
