from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author, AreaOfExpertise

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Создание тестовых данных
        self.area = AreaOfExpertise.objects.create(area="Programming")
        self.author = Author.objects.create(surname="Doe", name="John")
        self.book = Book.objects.create(
            name="Example Book",
            number_of_pages=300,
            year_of_publication=2022,
            area_of_expertise=self.area
        )
        self.book.authors.add(self.author)

