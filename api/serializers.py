from rest_framework import serializers
from .models import Item, Location


class Itermserializer(serializers.ModelSerializer):
    class Meta:
        model = Item 
        fields= ('__all__')

class Locationserializer(serializers.ModelSerializer):
    class Meta:
        model = Item 
        fields= ('__all__')