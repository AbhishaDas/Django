from django.db import models

# Create your models here.
class movie_info(models.Model):
    title =models.CharField(max_length=250)
    year =models.IntegerField(null=0)
    summary =models.TextField(null=True)
    
    
    def __str__(self):
        return self.title