from django.db import models

class Kiosk(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    kiosk = models.ForeignKey(Kiosk, related_name='icecreams', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.flavor})"

