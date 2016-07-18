"""REST views."""
from RESTAPI.serializers import LocationSerializer
from Locations.models import Location
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
#from rest_framework.permissions import IsAuthenticated

class LocationListView(ListAPIView):
    """Locations."""

    queryset = Location.objects.all()
    serializer_class = LocationSerializer


    def list(self, request, *args, **kwargs):

        return super(LocationListView, self).list(request, *args, **kwargs)

#class LocationListView(viewsets.ModelViewSet):
#    """Locations."""
#
#    queryset = Location.objects.all()
#    serializer_class = LocationSerializer