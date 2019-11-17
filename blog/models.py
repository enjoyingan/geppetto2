from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    writer=models.CharField(max_length=200, default=True)
    name=models.CharField(max_length=200, default=True)
    pub_date=models.DateTimeField('date published')
    phone=models.CharField(max_length=200, default=True)
    body=models.TextField()
    age=models.IntegerField(default=0)

    def __str__(self):
        return self.title