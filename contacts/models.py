from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20, blank=True)
    house_id = models.CharField(max_length=12, blank=True)
    email = models.EmailField()
    telephone = models.PositiveIntegerField(blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.email} <--> {self.name}"
