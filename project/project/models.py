from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        db_table = 'author'

    def __str__(self) -> str:
        return self.name

class category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    year = models.IntegerField()
    book_category = models.ForeignKey(category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'

    def __str__(self) -> str:
        return self.name


class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'

    def __str__(self) -> str:
        return self.author.name

class Review(models.Model):
    comment = models.CharField(max_length=100)
    star_given = models.IntegerField()
    user = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self) -> str:
        return self.comment