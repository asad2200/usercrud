from django.urls import path, include

from . import views

app_name = "reviewapp"
urlpatterns = [
    path("", views.ApartmentListView.as_view(), name="apartment_list"),
    path("review/<int:apartment_id>", views.ReviewCreateView.as_view(), name="add_apartment_review"),
]
