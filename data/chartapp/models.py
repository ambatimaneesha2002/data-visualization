from django.db import models

# Create your models here.
class Product(models.Model):
     category = models.CharField(max_length=100,null=False,blank=False)
     num_of_products = models.IntegerField()

     def __str__(self):
         return f'{self.category} - {self.num_of_products}'


class EnergyInsight(models.Model):
    title = models.TextField()
    source = models.TextField()
    published = models.DateTimeField()
    added = models.DateTimeField()
    url = models.URLField()
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    relevance = models.IntegerField()
    intensity = models.IntegerField()
    likelihood = models.IntegerField()
    pestle = models.CharField(max_length=100)
    insight = models.CharField(max_length=100)
    impact = models.TextField()

    def __str__(self):
        return self.title
