from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class IndexTestCase(TestCase):
    def test_index_is_renderable(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            "<title>Page de contenu — Titre du site</title>",
        )
