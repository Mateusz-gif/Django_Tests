import datetime
from urllib.request import urlopen

from django.test import LiveServerTestCase
from django.urls import reverse
from django.utils import timezone

from polls.models import Question


class PollsLiveServerTests(LiveServerTestCase):
    def test_index_page_displays_published_question(self):
        Question.objects.create(
            question_text="Live server question",
            pub_date=timezone.now() - datetime.timedelta(days=1),
        )

        response = urlopen(f"{self.live_server_url}{reverse('polls:index')}")
        html = response.read().decode("utf-8")

        self.assertIn("Live server question", html)