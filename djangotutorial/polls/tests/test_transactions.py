import datetime

from django.db import transaction
from django.test import TransactionTestCase
from django.utils import timezone

from polls.models import Question


class QuestionTransactionTests(TransactionTestCase):
    def test_atomic_block_rolls_back_question_creation(self):
        """
        A Question created inside an atomic block should be rolled back
        when the transaction is marked for rollback.
        """
        with transaction.atomic():
            Question.objects.create(
                question_text="Temporary question",
                pub_date=timezone.now() - datetime.timedelta(days=1),
            )
            transaction.set_rollback(True)

        self.assertEqual(Question.objects.count(), 0)