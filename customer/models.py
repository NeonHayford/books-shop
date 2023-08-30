from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, max_length= 32,verbose_name='book id')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='slug')
    category = models.CharField(max_length=70)
    file = models.FileField(upload_to='files/%h')
    description = models.TextField(blank=True)
    publisher = models.CharField(max_length=150)
    published = models.DateField(blank=True, null=True)
    added_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=3.99)


AV, NOTAV, CS = 'AV', 'NOTAV', 'CS'
STATUS = [
    (AV, 'Available'),
    (NOTAV, 'Not Available'),
    (CS, 'Comming Soon')
]
class BookStatus(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default=AV)



class Subscription(models.Model):
    email = models.EmailField(verbose_name='Subscription')

