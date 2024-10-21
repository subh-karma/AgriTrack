from rest_framework import generics
from .serializers import Itermserializer, Locationserializer 
from .models import Item,Location
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Storage API!")

class ItemList (generics.ListCreateAPIView):
    serializer_class= Itermserializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None :
            queryset=queryset.filter(itemLocation=location)
        return queryset
    
class ItemDetail(generics.RetrieveDestroyAPIView):
    serializer_class=Itermserializer
    queryset = Location.objects.all()



class LocationList(generics.ListCreateAPIView):
    serializer_class=Locationserializer
    queryset = Location.objects.all()


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=Locationserializer
    queryset = Location.objects.all()

 