from django.test import TestCase
from .models import Comic, Rating

class RatingTestCase(TestCase):
    def setUp(self):
        Comic.objects.create(title="Test Comic", author="Author", rating=0)

    def test_rating_creation_and_update(self):
        comic = Comic.objects.get(title="Test Comic")
        Rating.objects.create(comic=comic, user_id=1, value=5)
        self.assertEqual(comic.rating, 5)

    def test_get_comic_rating(self):
        comic = Comic.objects.get(title="Test Comic")
        response = self.client.get(f'/api/comics/{comic.id}/rating/')
        self.assertEqual(response.json()['rating'], comic.rating)
