from datetime import datetime, date
from app.exception import CreditCardNumberError, CardHolderError, ExpirationDateError, SecurityCodeError, AmountError
from app.constants import PaymentGateways
from app.External_geteway import BasePaymentGateway
from app.External_geteway import CheapBasePaymentGateway, ExpensiveBasePaymentGateway, PremiumBasePaymentGateway


class ValidateCardInfo:

    def credit_card_number(self):
        card = list(input("Enter card number\t").strip())
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
            raise CreditCardNumberError("it is not valid credit card number", {card})

        return card

    def card_holder(self):

        cardholder_name = input("Enter cardholder name\t")
        if not cardholder_name.isalpha():
            raise CardHolderError("Enter card holder name as string")
        return cardholder_name

    def expiration_date(self):
        expiration_date = input("Enter expiration date of card  ")
        card_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
        current_datetime = date.today()

        if card_date <= current_datetime:
            raise ExpirationDateError("DateTime, it cannot be in the past", expiration_date)

        return expiration_date

    def security_code(self):
        sec_code = input("Enter Security Code\t")
        if sec_code == None:
            pass
            if len(sec_code) != 3 or not sec_code.isdecimal():
                raise SecurityCodeError("Security Code should be 3 digits ", sec_code)
        return sec_code

    def check_amount(self):
        amount = int(input("Enter amount\t"))
        if amount < 0:
            raise AmountError("Enter positive amount ")
        else:
            ValidatePaymentGateways.type_payment_geteways(amount)
        return amount


class ValidatePaymentGateways(BasePaymentGateway):

    def type_payment_geteways(amount):
        if amount <= PaymentGateways.CHEAPPAYMENTGAYEWAY.value:
            CheapBasePaymentGateway()
        elif (amount >= PaymentGateways.EXPENSIVEPAYMENTGAYEWAY.value) and (
                amount <= PaymentGateways.PREMIUMPAYMENTGAYEWAY.value):
            ExpensiveBasePaymentGateway()
        elif amount >= PaymentGateways.PREMIUMPAYMENTGAYEWAY.value:
            PremiumBasePaymentGateway()

# obj = ValidateCardInfo()
# obj.check_amount()