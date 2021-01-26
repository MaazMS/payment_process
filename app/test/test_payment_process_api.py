from app.view.views import app
from flask import json
from controller.exception import InvalidCardDetailsError, InvalidAmountError
import pytest
from unittest.mock import patch

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


def test_invalid_card_details():
    response = app.test_client().post(
        '/process_payment/',
        data=json.dumps({
            "credit_card_number": "508963066400183",
            "card_holder": "Maaz",
            "expiration_date": "2021-02-02",
            "security_code": "123",
            "amount": 100}),
        content_type='application/json',
    )
    assert response.status_code == 400


def test_invalid_amount():
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
    assert response.status_code == 400