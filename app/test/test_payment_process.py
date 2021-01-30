import pytest
from controller.payment import process_payment
from controller.exception import InvalidCardDetailsError, InvalidAmountError


def test_invalid_card_number():
    """
    :return: Ths test for card number validation. If card number is not valid it raise exception InvalidCardDetailsError
    """

    credit_card_number = "508963066400183"
    card_holder = "Maaz"
    expiration_date = "2022-02-02"
    security_code = "123"
    amount = 100
    with pytest.raises(InvalidCardDetailsError) as e:
        assert process_payment(
            credit_card_number, card_holder, expiration_date, security_code, amount
        )


def test_invalid_customer_name():
    """
    :return: Ths test for customer name validation. If customer name is not valid it raise exception InvalidCardDetailsError
    """

    credit_card_number = "5089630664001838"
    card_holder = "123"
    expiration_date = "2022-02-02"
    security_code = "123"
    amount = 100
    with pytest.raises(InvalidCardDetailsError) as e:
        assert process_payment(
            credit_card_number, card_holder, expiration_date, security_code, amount
        )


def test_invalid_expiration_date():
    """
    :return: Ths test for expiration date validation. If expiration date is not valid it raise exception InvalidCardDetailsError
    """

    credit_card_number = "5089630664001838"
    card_holder = "Maaz"
    expiration_date = "2019-02-02"
    security_code = "123"
    amount = 100
    with pytest.raises(InvalidCardDetailsError) as e:
        assert process_payment(
            credit_card_number, card_holder, expiration_date, security_code, amount
        )


def test_invalid_security_code():
    """
    :return: Ths test for security code validation. If security code is not valid it raise exception InvalidCardDetailsError
    """

    credit_card_number = "5089630664001838"
    card_holder = "Maaz"
    expiration_date = "2022-02-02"
    security_code = "12345"
    amount = 100
    with pytest.raises(InvalidCardDetailsError) as e:
        assert process_payment(
            credit_card_number, card_holder, expiration_date, security_code, amount
        )


def test_invalid_amount():
    """
    :return: Ths test for amount validation. If amount is less then equal to zero it raise exception InvalidCardDetailsError
    """
    credit_card_number = "5089630664001838"
    card_holder = "Maaz"
    expiration_date = "2022-02-02"
    security_code = "123"
    amount = -100
    with pytest.raises(InvalidAmountError) as e:
        assert process_payment(
            credit_card_number, card_holder, expiration_date, security_code, amount
        )
