from django.db import models

# Create your models here.
class studentRecords(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    book_name=models.CharField(max_length=300)
    issue_date=models.DateField(auto_now=False)
    return_date=models.DateField(auto_now=False)

    def __str__(self):
        return self.first_name


class bookDataset(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    isbn=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    quantity=models.IntegerField()

    def __str__(self):
        return self.title

class issueRecords(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    book_id = models.IntegerField()
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    issue_date = models.DateField(auto_now=False)

    def __str__(self):
        return self.first_name




