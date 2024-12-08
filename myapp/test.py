# from rest_framework.test import APITestCase
# from rest_framework import status
# from .models import Book, Author, AreaOfExpertise
#
# class BookAPITestCase(APITestCase):
#     def setUp(self):
#         # Создание тестовых данных
#         self.area = AreaOfExpertise.objects.create(area="Programming")
#         self.author = Author.objects.create(surname="Doe", name="John")
#         self.book = Book.objects.create(
#             name="Example Book",
#             number_of_pages=300,
#             year_of_publication=2022,
#             area_of_expertise=self.area
#         )
#         self.book.authors.add(self.author)



#  from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse
# from .models import Book, Author, AreaOfExpertise
#
#
# class BookAPITestCase(APITestCase):
#     def setUp(self):
#         # Создание областей специализации
#         self.area_programming = AreaOfExpertise.objects.create(area="Programming")
#         self.area_science = AreaOfExpertise.objects.create(area="Science")
#
#         # Создание авторов
#         self.author_john = Author.objects.create(surname="Doe", name="John")
#         self.author_jane = Author.objects.create(surname="Smith", name="Jane", patronymic="A.")
#
#         # Создание книг
#         self.book1 = Book.objects.create(
#             name="Example Book",
#             number_of_pages=300,
#             year_of_publication=2022,
#             area_of_expertise=self.area_programming
#         )
#         self.book1.authors.add(self.author_john)
#
#         self.book2 = Book.objects.create(
#             name="Science Fundamentals",
#             number_of_pages=250,
#             year_of_publication=2021,
#             area_of_expertise=self.area_science
#         )
#         self.book2.authors.add(self.author_jane)
#
#         self.book3 = Book.objects.create(
#             name="Advanced Programming",
#             number_of_pages=400,
#             year_of_publication=2023,
#             area_of_expertise=self.area_programming
#         )
#         self.book3.authors.add(self.author_john, self.author_jane)

    # def test_get_book_list(self):
    #     url = reverse('book-list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 3)
    #
    # def test_get_book_detail(self):
    #     url = reverse('book-detail', args=[self.book2.id])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['name'], "Science Fundamentals")
    #
    # def test_create_book(self):
    #     url = reverse('book-list')
    #     data = {
    #         "name": "New Book",
    #         "number_of_pages": 350,
    #         "year_of_publication": 2024,
    #         "area_of_expertise": self.area_programming.id,
    #         "authors": [self.author_john.id, self.author_jane.id]
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Book.objects.count(), 4)
    #     self.assertEqual(Book.objects.get(id=response.data['id']).name, "New Book")
    #
    # def test_update_book(self):
    #     url = reverse('book-detail', args=[self.book1.id])
    #     data = {
    #         "name": "Updated Example Book",
    #         "number_of_pages": 320,
    #         "year_of_publication": 2022,
    #         "area_of_expertise": self.area_programming.id,
    #         "authors": [self.author_john.id]
    #     }
    #     response = self.client.put(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.book1.refresh_from_db()
    #     self.assertEqual(self.book1.name, "Updated Example Book")
    #     self.assertEqual(self.book1.number_of_pages, 320)
    #
    # def test_delete_book(self):
    #     url = reverse('book-detail', args=[self.book3.id])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertFalse(Book.objects.filter(id=self.book3.id).exists())

# from myapp.models import Author, AreaOfExpertise, Book
#
# # Создание областей специализации
# area_programming = AreaOfExpertise.objects.create(area="Programming")
# area_science = AreaOfExpertise.objects.create(area="Science")
# area_mathematics = AreaOfExpertise.objects.create(area="Mathematics")
#
# # Создание авторов
# author_john = Author.objects.create(surname="Doe", name="John")
# author_jane = Author.objects.create(surname="Smith", name="Jane", patronymic="A.")
# author_alice = Author.objects.create(surname="Brown", name="Alice", patronymic="B.")
#
# # Создание книг
# book1 = Book.objects.create(
#     name="Python Programming",
#     number_of_pages=350,
#     year_of_publication=2021,
#     area_of_expertise=area_programming
# )
# book1.authors.set([author_john, author_jane])
#
# book2 = Book.objects.create(
#     name="Advanced Science",
#     number_of_pages=400,
#     year_of_publication=2022,
#     area_of_expertise=area_science
# )
# book2.authors.set([author_jane, author_alice])
#
# book3 = Book.objects.create(
#     name="Mathematics for Beginners",
#     number_of_pages=250,
#     year_of_publication=2020,
#     area_of_expertise=area_mathematics
# )
# book3.authors.set([author_john, author_alice])
