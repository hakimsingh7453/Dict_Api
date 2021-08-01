from django.db import models

class dicts(models.Model):
    spelling=models.CharField(max_length=50)
    meaning=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.spelling