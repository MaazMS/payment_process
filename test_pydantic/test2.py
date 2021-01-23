from pydantic import BaseModel, validator,  ValidationError
from datetime import datetime


class Customer(BaseModel):
    card_number: str
    # customer_name: str
    # exp_date: datetime
    # cvv: str = None
    # amount: int

    def __init__(self, card_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.card_number = card_number

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
            raise ValueError("it is not valid credit card number", {str(card)})
        else:
            print("This is valid credit card number")
        return card

try:
    Customer(
        card_number = "5893804115457289",
    )
except ValidationError as e:
    print(e.json())





