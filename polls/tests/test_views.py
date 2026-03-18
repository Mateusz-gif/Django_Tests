import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from polls.models import Question


def create_question(question_text, days):
    return Question.objects.create(
        question_text=question_text,
        pub_date=timezone.now() + datetime.timedelta(days=days),
    )


class QuestionIndexViewTests(TestCase):
    def test_future_question_is_not_displayed(self):
        create_question("Future question", days=5)

        response = self.client.get(reverse("polls:index"))

        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question_is_displayed(self):
        question = create_question("Past question", days=-5)

        response = self.client.get(reverse("polls:index"))

        self.assertQuerySetEqual(response.context["latest_question_list"], [question])