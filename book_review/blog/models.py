from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='blog/images/', default = "https://www.pressgazette.co.uk/wp-content/uploads/2020/11/shutterstock.jpg")

    def __str__(self):
        return self.title
