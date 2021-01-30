from pydantic import BaseModel, validator
from datetime import date
from typing import Optional


class CardDetails(BaseModel):
    card_number: str
    customer_name: str
    exp_date: date
    cvv: Optional[str] = None

    @validator("card_number")
    def card_number_validate(cls, card_no):
        """
        :param card_no: This function take card number and check card number is valid or not.
        :return:  It return valid card number and if card number is not validate it return valueError
        """

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
        """
        :param cardholder_name: This function take card holder name and validate the card holder name
        :return: It return valid card holder name if card holder name is not valid it return assert error
        """

        assert cardholder_name.isalpha(), "cardholder name must be alphabet"
        return cardholder_name

    @validator("exp_date")
    def expiration_date(cls, expiration_date):
        """
        :param expiration_date: This function take card expiration date and validate the card expiration date
        :return: It return valid card expiration date if card expiration date is not validate it return valueError
        """

        current_datetime = date.today()
        if expiration_date <= current_datetime:
            raise ValueError(" expiration date cannot be in the past", expiration_date)
        return expiration_date

    @validator("cvv")
    def security_code(cls, sec_code):
        """
        :param sec_code: This function take card security code and validate the card security code
        :return: It return valid card security code if card security code is not valid it return assert error
        """

        assert sec_code.isdecimal(), " Invalid security code "
        assert len(sec_code) == 3, "Invalid security code "
        return sec_code

    def get_card_details(self):
        """
        :return: This function is return card details such as card number, customer name, expiration date,
        security code
        """

        return {
            "card_number": self.card_number,
            "customer_name": self.customer_name,
            "exp_date": self.exp_date,
            "cvv": self.cvv,
        }
