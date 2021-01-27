import pytest
from controller import payment


@pytest.fixture
def test_cheap_payment_gateway(mocker):
    credit_card_number = "508963066400183"
    card_holder = "Maaz"
    expiration_date = "2022-02-02"
    security_code = "123"
    amount = 20
    mocker.patch(payment.process_payment, return_value=True)
    assert payment.process_payment(credit_card_number, card_holder, expiration_date, security_code, amount) == True
