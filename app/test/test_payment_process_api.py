from app.view.views import app
from flask import json


def test_payment_process_successful():
    """
    :return: It return response payment process successful by status code 200
    """
    response = app.test_client().post(
        "/process_payment/",
        data=json.dumps(
            {
                "credit_card_number": "5089630664001838",
                "card_holder": "Maaz",
                "expiration_date": "2021-02-02",
                "security_code": "123",
                "amount": 100,
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 200


def test_invalid_card_details():
    """
    :return: It return response invalid card details by status code 400
    """

    response = app.test_client().post(
        "/process_payment/",
        data=json.dumps(
            {
                "credit_card_number": "508963066400183",
                "card_holder": "Maaz",
                "expiration_date": "2021-02-02",
                "security_code": "123",
                "amount": 100,
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 400


def test_invalid_amount():
    """
    :return: It return response invalid amount by status code 400
    """
    response = app.test_client().post(
        "/process_payment/",
        data=json.dumps(
            {
                "credit_card_number": "5089630664001838",
                "card_holder": "Maaz",
                "expiration_date": "2021-02-02",
                "security_code": "123",
                "amount": -100,
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 400


def test_payment_failed():
    """
    :return: It return response payment failed by status code 400
    """

    response = app.test_client().post(
        "/process_payment/",
        data=json.dumps(
            {
                "credit_card_number": "5089630664001838",
                "card_holder": "Maaz",
                "expiration_date": "2021-02-02",
                "security_code": "123",
                "amount": -10,
            }
        ),
        content_type="application/json",
    )
    assert response.status_code == 400


def test_internal_server_error():
    """
    :return: It return response internal server error by status code 500
    """

    response = app.test_client().post(
        "/process_payment/",
        data=json.dumps(
            {
                "credit_card_number": "5089630664001838",
                "card_holder": "Maaz",
                "expiration_date": "2021-02-02",
                "security_code": "123",
                "amount": 0,
            }
        ),
        content_type="application",
    )
    assert response.status_code == 500
