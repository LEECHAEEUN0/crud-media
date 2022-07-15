from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    writer = models.CharField(max_length=20, null = True, blank = True, default = "이채은")
    feelings = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank = True, null=True)

    def __str__(self):
        return self.title    
    