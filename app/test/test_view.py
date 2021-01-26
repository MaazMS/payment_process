from app.view.views import app
from flask import json
from controller.exception import InvalidCardDetailsError, InvalidAmountError
import pytest


def test_card_successful():
    response = app.test_client().post(
        '/process_payment/',
        data=json.dumps({
            "credit_card_number": "5089630664001838",
            "card_holder": "Maaz",
            "expiration_date": "2021-02-02",
            "security_code": "123",
            "amount": 100}),
        content_type='application/json',
    )
    assert response.status_code == 200


def test_card_details_error():

    with pytest.raises(InvalidCardDetailsError)as e:
        response = app.test_client().post(
            '/process_payment/',
            data=json.dumps({
                "credit_card_number": "5089",
                "card_holder": "Maaz",
                "expiration_date": "2021-02-02",
                "security_code": "123",
                "amount": 100}),
            content_type='application/json',
        )


    assert response.status_code == 400
    # assert 'Card details are not valid' == str(e)
    print(str(e))

def test_amount_error():

    with pytest.raises(InvalidAmountError) as e:
        response = app.test_client().post(
            '/process_payment/',
            data=json.dumps({
                "credit_card_number": "5089630664001838",
                "card_holder": "Maaz",
                "expiration_date": "2021-02-02",
                "security_code": "123",
                "amount": -100}),
            content_type='application/json',
        )
    print(str(e))