"""REST views."""
from RESTAPI.serializers import LocationSerializer
from Locations.models import Location
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class LocationListView(ListAPIView):
    """Display List of all Locations."""

    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def list(self, request, *args, **kwargs):
        """Return List of all locations."""
        return super(LocationListView, self).list(request, *args, **kwargs)


@api_view()
def LocationSingleView(request, *args, **kwargs):
    """Display Single Location."""
    filter_by = kwargs['name']
    to_show = Location.objects.get(name=filter_by)
    img_link = to_show.map_img._get_url()
    img_link = 'http://localhost:8000' + img_link
    return Response({'Name': to_show.name, 'Key': to_show.key, 'Link To Map Image': img_link})


