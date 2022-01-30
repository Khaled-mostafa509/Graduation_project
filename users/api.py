from .models import Home
from .serializers import HomeSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])

def Home_listAPI(request):
    all_ads=Home.objects.all()
    data=HomeSerializers(all_ads,many=True).data
    return Response({'data':data})