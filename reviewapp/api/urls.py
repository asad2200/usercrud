from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import ApartmentReviewViewSet

urlpatterns = [
    path(
        'review/<int:apartment_id>',
        ApartmentReviewViewSet.as_view({'get': 'retrive', 'post':'create'}),
        name='user_apartment_review',
    ),
]