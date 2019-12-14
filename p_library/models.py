from django.db import models



class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Redaction(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    title = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    redaction = models.ForeignKey(Redaction, null=True, on_delete=models.SET_NULL)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='catalog_images')

    def __str__(self):
        return self.title

class Friend(models.Model):
    friend_name = models.CharField(max_length=30)
    borrowed_books = models.ManyToManyField(Book)

    def __str__(self):
        return self.friend_name