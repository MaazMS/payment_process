from datetime import datetime, date
from app.PaymentGetways import PaymentGateways


class ProcessPayment:


    def credit_card_number(self):

        card = list(input("Enter card number\t").strip())
        rmv_last_digit =card.pop()
        card.reverse()

        processing_card_no = []
        for index, card_no in enumerate(card):

            if index % 2 ==0:
                double_card_no = int(card_no) * 2

                if double_card_no > 9:
                    double_card_no = double_card_no - 9
                processing_card_no.append(double_card_no)
            else:
                processing_card_no.append(int(card_no))
        check_card_no = int(rmv_last_digit) + sum(processing_card_no)

        if check_card_no % 10 == 0:
            print("it is valid credit card number")
        else:
            print("it is not valid credit card number")

    def card_holder(self):

        cardholder_name  = input("Enter card holder name\t")
        if not cardholder_name.isalpha():
            print("Enter card holder name as string")

    def expiration_date(self):

        expiration_date = input("Enter expiration date of card  ")
        card_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
        current_datetime = date.today()

        if card_date <= current_datetime:
            print("DateTime, it cannot be in the past")
        else:
            print("Expiration Date is correct in card ")

    def security_code(self):

        Sec_Code = input("Enter Security Code\t")
        if len(Sec_Code) != 3 or not Sec_Code.isdecimal():
            print("Security Code should be 3 digits ")
        else:
            print("corect Security Code ")

    def check_amount(self):

        Amount = int(input("Enter amount"))
        if Amount < 0 :
            print("Enter positive amount ")


obj = ProcessPayment()
# obj.credit_card_number()
# obj.card_holder()
# obj.expiration_date()
# obj.security_code()
# obj.check_amount()

