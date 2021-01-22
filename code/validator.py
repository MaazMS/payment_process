from datetime import datetime, date
from code.exception import CreditCardNumberError,CardHolderError, ExpirationDateError, SecurityCodeError, AmountError
from code.constants import PaymentGateways





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

        return  cardholder_name


    def expiration_date(self):

        expiration_date = input("Enter expiration date of card  ")
        card_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
        current_datetime = date.today()

        if card_date <= current_datetime:
            raise ExpirationDateError("DateTime, it cannot be in the past", expiration_date)

        return expiration_date


    def security_code(self):

        Sec_Code = input("Enter Security Code\t")
        if len(Sec_Code) != 3 or not Sec_Code.isdecimal():
            raise SecurityCodeError("Security Code should be 3 digits ", Sec_Code)

        return Sec_Code

    def check_amount(self):

        Amount = int(input("Enter amount\t"))
        if Amount < 0:
            raise AmountError("Enter positive amount ")
        else:
            print("check paymentGeteway call")
            # type_payment_Geteways(Amount)
            ValidatePaymentGateways.type_payment_Geteways(Amount)
        return Amount


# def type_payment_Geteways(Amount ):
#     print("check paymentGeteway def type_payment_Geteways ")
#     print(type(Amount))
#     if Amount <= PaymentGateways.CHEAPPAYMENTGAYEWAY:
#         print("CheapPaymentGateway")
#     elif (Amount >= PaymentGateways.EXPENSIVEPAYMENTGAYEWAY) and (PaymentGateways.PREMIUMPAYMENTGAYEWAY <= Amount):
#         print("ExpensivePaymentGateway")
#     elif Amount >= PaymentGateways.PREMIUMPAYMENTGAYEWAY:
#         print("PremiumPaymentGateway")
#
class ValidatePaymentGateways:

    def type_payment_Geteways(Amount):

       print("check paymentGeteway def type_payment_Geteways ")
       print(type(Amount))
       if Amount <= PaymentGateways.CHEAPPAYMENTGAYEWAY:
           print("CheapPaymentGateway")
       elif (Amount >= PaymentGateways.EXPENSIVEPAYMENTGAYEWAY) and  (PaymentGateways.PREMIUMPAYMENTGAYEWAY <= Amount):
           print("ExpensivePaymentGateway")
       elif Amount >= PaymentGateways.PREMIUMPAYMENTGAYEWAY:
           print("PremiumPaymentGateway")

obj = ValidateCardInfo()
obj.check_amount()