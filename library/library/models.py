# models.py
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('fantasy', 'Fantasy'),
        ("children's books", "Children's Books"),
        ('self-help', 'Self-Help'),
        ('philosophy', 'Philosophy'),
        ('technology', 'Technology'),
        ('academic', 'Academic'),
    ]
    
    id = models.CharField(max_length=5, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    cover = models.ImageField(upload_to='book_covers/')
    description = models.TextField()
    published_date = models.DateField()
    
    def __str__(self):
        return self.title

class UserBookRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    borrow_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = ('user', 'book')