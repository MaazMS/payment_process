import pytest
from controller.payment import process_payment
from controller.exception import InvalidCardDetailsError, InvalidAmountError


def test_invalid_card_number():
    credit_card_number = "508963066400183"
    card_holder = "Maaz"
    expiration_date = "2022-02-02"
    security_code = "123"
    amount = 100
    with pytest.raises(InvalidCardDetailsError)as e:
        assert process_payment(credit_card_number, card_holder, expiration_date, security_code, amount)
    print(str(e))


def test_invalid_customer_name():
    credit_card_number = "5089630664001838"
    card_holder = "123"
    expiration_date = "2022-02-02"
    security_code = "123"
    amount = 100
    with pytest.raises(InvalidCardDetailsError)as e:
        assert process_payment(credit_card_number, card_holder, expiration_date, security_code, amount)
    print(str(e))


def test_invalid_expiration_date():
    credit_card_number = "5089630664001838"
    card_holder = "Maaz"
    expiration_date = "2019-02-02"
    security_code = "123"
    amount = 100
    with pytest.raises(InvalidCardDetailsError)as e:
        assert process_payment(credit_card_number, card_holder, expiration_date, security_code, amount)
    print(str(e))


def test_invalid_security_code():
    credit_card_number = "5089630664001838"
    card_holder = "Maaz"
    expiration_date = "2022-02-02"
    security_code = "12345"
    amount = 100
    with pytest.raises(InvalidCardDetailsError)as e:
        assert process_payment(credit_card_number, card_holder, expiration_date, security_code, amount)
    print(str(e))


def test_invalid_amount():
    credit_card_number = "5089630664001838"
    card_holder = "Maaz"
    expiration_date = "2022-02-02"
    security_code = "123"
    amount = -100
    with pytest.raises(InvalidAmountError)as e:
        assert process_payment(credit_card_number, card_holder, expiration_date, security_code, amount)
    print(str(e))
