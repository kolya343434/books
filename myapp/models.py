from django.db import models


# Модель для таблицы area_of_expertise
class AreaOfExpertise(models.Model):
    area = models.CharField(max_length=100)  # Название области специализации

    def __str__(self):
        return self.area


# Модель для таблицы author
class Author(models.Model):
    surname = models.CharField(max_length=50)  # Фамилия автора
    name = models.CharField(max_length=50)  # Имя автора
    patronymic = models.CharField(max_length=50, blank=True, null=True)  # Отчество автора (необязательно)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic or ''}".strip()


# Модель для таблицы books
class Book(models.Model):
    name = models.CharField(max_length=100)  # Название книги
    number_of_pages = models.IntegerField(blank=True, null=True)  # Количество страниц
    year_of_publication = models.IntegerField(blank=True, null=True)  # Год публикации
    area_of_expertise = models.ForeignKey(
        AreaOfExpertise,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="books"
    )  # Связь с таблицей AreaOfExpertise
    authors = models.ManyToManyField(Author, related_name="books")  # Many-to-Many связь с Author
    file = models.FileField(upload_to='books/', blank=True, null=True)  # Поле для загрузки файлов

    def __str__(self):
        return self.name




class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


