from django.test import SimpleTestCase
from django.urls import resolve, reverse

from polls.views import IndexView


class PollsURLTests(SimpleTestCase):
    def test_index_url_resolves_to_index_view(self):
        url = reverse("polls:index")
        resolver = resolve(url)

        self.assertEqual(resolver.func.view_class, IndexView)