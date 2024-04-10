from django.db import models

# Create your models here.


class Iris(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()

    classifiction = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return str(self.classifiction) if self.classifiction else "No classifiction"
