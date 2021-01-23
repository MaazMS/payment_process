from pydantic import BaseModel, validator
from datetime import date
from typing import Optional
from base.gateways.payment_geteways import ValidatePaymentGateways


class Customer(BaseModel):
    card_number: str
    customer_name: str
    exp_date: date
    cvv: Optional [str] = None
    amount: int

    @validator("card_number")
    def card_number_validate(cls, card_no ):
        card = list(card_no)
        rmv_last_digit = card.pop()
        card.reverse()

        processing_card_no = []
        for index, card_no in enumerate(card):
            if index % 2 == 0:
                double_card_no = int(card_no) * 2
                if double_card_no > 9:
                    double_card_no = double_card_no - 9
                processing_card_no.append(double_card_no)
            else:
                processing_card_no.append(int(card_no))
        check_card_no = int(rmv_last_digit) + sum(processing_card_no)
        if check_card_no % 10 != 0:
            raise ValueError("it is not valid credit card number", card)
        return card

    @validator("customer_name")
    def card_holder(cls, cardholder_name):
        assert cardholder_name.isalpha(), 'cardholder name must be alphabet'
        return cardholder_name

    @validator("exp_date")
    def expiration_date(cls, expiration_date):
        current_datetime = date.today()
        if expiration_date <= current_datetime:
            raise ValueError(" expiration date cannot be in the past", expiration_date)
        return expiration_date

    @validator("cvv")
    def security_code(cls, sec_code):
        assert sec_code.isdecimal(), "Enter security code should be digit"
        assert len(sec_code) == 3, "Security Code should be equal 3 digits"
        return sec_code

    @validator("amount")
    def check_amount(cls, amount):
        if amount < 0:
            raise ValueError("Enter positive amount ")
        else:
            ValidatePaymentGateways.type_payment_geteways(amount)
        return amount