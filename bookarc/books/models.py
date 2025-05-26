from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction','Fiction'),
        ('nonfiction','Non-Fiction'),
        ('sci','Sci-Fi'),
        # …add as needed
    ]

    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    cover = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.name
