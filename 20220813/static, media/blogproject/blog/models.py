from django.db import models

class Blog(models.Model):
    location = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    duration = models.TextField(max_length=100)
    price = models.TextField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50] + '...'