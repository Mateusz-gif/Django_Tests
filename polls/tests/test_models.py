import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question_returns_false(self):
        """
        was_published_recently() should return False for future questions.
        """
        future_time = timezone.now() + datetime.timedelta(days=30)
        question = Question(pub_date=future_time)

        self.assertIs(question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question_returns_true(self):
        """
        was_published_recently() should return True for questions published
        within the last day.
        """
        recent_time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        question = Question(pub_date=recent_time)

        self.assertIs(question.was_published_recently(), True)