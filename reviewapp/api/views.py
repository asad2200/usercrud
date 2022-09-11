from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


from .serializers import ApartmentReviewSerializer
from reviewapp.models import Apartment, ApartmentReview

class ApartmentReviewViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and apartment review of user.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ApartmentReviewSerializer
    queryset = ApartmentReview.objects.all()

    def retrive(self, request, apartment_id=None):
        """
        Get user review for given apartment id
        """
        
        apartment = get_object_or_404(Apartment, pk=apartment_id)
        apartment_review = ApartmentReview.objects.filter(apartment=apartment, user=request.user).last()
        
        serializer = self.get_serializer(apartment_review)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, apartment_id=None):
        """
        Add review for given apartment id for requested user.
        """
        
        apartment = get_object_or_404(Apartment, pk=apartment_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(apartment=apartment, user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)