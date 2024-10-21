from django.db import models


class Location(models.Model):
    locationName = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.locationName


class Item(models.Model):
    itemname = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    ItemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemname
