from base.customer_information.customer import Customer
from pydantic import ValidationError

def credit_card_details(credit_card_number, card_holder, expiration_date, security_code, amount):
    try:
        card_validation =  Customer(
        card_number= credit_card_number,
        customer_name= card_holder,
        exp_date= expiration_date,
        cvv= security_code,
        amount= amount

        )

    except ValidationError as e:
            print(e.json())