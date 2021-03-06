from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return "First name: {0}\nLast name: {1}\nEmail: {2}".format(self.first_name, self.last_name, self.email)


