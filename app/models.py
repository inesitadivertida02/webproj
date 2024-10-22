from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateField()
    authors = models.ManyToManyField(Author)  # Many-to-many relationship with Author
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # Change to ForeignKey

    def __str__(self):
        return self.title
