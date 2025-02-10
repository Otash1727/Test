from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView  # 
from rest_framework import status
from .models import Organazation
from .serializer.serializers import OrganizationDetailSerializer  #
from .authentication import OrganizationTokenAuthentication

from rest_framework.permissions import AllowAny



class OrganizationListAPIView(APIView):
    authentication_classes = [OrganizationTokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        # `request.user` is actually the authenticated `Organazation` object
        organization = request.user  
        
        # Fetch only the authenticated organization's data
        serializer = OrganizationDetailSerializer(organization)
        return Response(serializer.data)
   

    #def get(self, request):
    #    organizations = Organazation.objects.prefetch_related(
    #        'phonenumber_set',
    #        'building_set',
    #        'food_types',  # Fixed related name
    #        'car_types',  # Fixed related name
    #        'other_product_types'  # Fixed related name
    #    ).all()
    #    serializer = OrganizationDetailSerializer(organizations, many=True)
    #    return Response(serializer.data)


# Retrieve a single organization by ID
class OrganizationDetailAPIView(RetrieveAPIView):
    authentication_classes = [OrganizationTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Organazation.objects.all()
    serializer_class = OrganizationDetailSerializer






