from django.test import TestCase
from pytest import raises

from netaxept.actions import payments
from netaxept.actions.payments import PaymentRegistrationNotCompleted
from netaxept.models import Payment


class PaymentTest(TestCase):

    def test_invalid_state(self):
        payment = Payment.objects.create(
            transaction_id='1234567890',
            order_number='an-order-number',
            amount=100,
            currency_code='NOK',
            success=False)
        with raises(PaymentRegistrationNotCompleted):
            payments.sale(payment.id)

    def test_valid_state(self):
        payment = Payment.objects.create(
            transaction_id='1234567890',
            order_number='an-order-number',
            amount=100,
            currency_code='NOK',
            success=True)
        payments.sale(payment.id)
