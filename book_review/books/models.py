from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='books/images/')
    review = models.TextField(max_length=6000)

    def __str__(self):
        return self.title
