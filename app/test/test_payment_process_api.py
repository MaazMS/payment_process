from app.view.views import app
from flask import json


def test_payment_process_successful():
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


def test_payment_failed():
    response = app.test_client().post(
        '/process_payment/',
        data=json.dumps({
            "credit_card_number": "5089630664001838",
            "card_holder": "Maaz",
            "expiration_date": "2021-02-02",
            "security_code": "123",
            "amount": 0}),
        content_type='application',
    )
    assert response.status_code == 400

def test_internal_server_error():
    response = app.test_client().post(
        '/process_payment/',
        data=json.dumps({
            "credit_card_number": "5089630664001838",
            "card_holder": "Maaz",
            "expiration_date": "2021-02-02",
            "security_code": "123",
            "amount": 0}),
        content_type='application',
    )
    assert response.status_code == 500
