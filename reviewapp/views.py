from django.views.generic import ListView, CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Exists, OuterRef

from reviewapp.models import Apartment, ApartmentReview
from .forms import ApartmentReviewForm


class ApartmentListView(ListView):
    """
        A ListView to display all apartment
    """

    model = Apartment
    context_object_name = "apartment_list"
    template_name = "reviewapp/apartment_list.html"

    def get_queryset(self):
        # Check if user is authenticated or not then
        # Get boolean value of user added review or not for apartment in apartment list
        if self.request.user.is_authenticated:
            queryset = self.model.objects.annotate(
                is_added_review=Exists(
                    ApartmentReview.objects.filter(user=self.request.user, apartment=OuterRef('pk'))
                )
            ).all()
            return queryset

        return super().get_queryset()
    
class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
        A CreateView to add review to the department
    """

    model = ApartmentReview
    form_class = ApartmentReviewForm
    template_name = "reviewapp/add_apartment_review.html"
    
    def get_success_url(self):
        return reverse("reviewapp:apartment_list")
    
    def get_user_apartment_review(self, user, apartment):
        return ApartmentReview.objects.filter(apartment=apartment, user=user).last()

    def get_context_data(self, **kwargs):
        apartment = get_object_or_404(Apartment, pk=self.kwargs['apartment_id'])
        kwargs['apartment'] = apartment

        apartment_review = self.get_user_apartment_review(apartment=apartment, user=self.request.user)
        if apartment_review:
            kwargs['apartment_review'] = apartment_review

        return super().get_context_data(**kwargs)
    
    def get_template_names(self):
        """
            If user already gave review then return apartment_user_review template.
        """

        apartment = get_object_or_404(Apartment, pk=self.kwargs['apartment_id'])
        apartment_review = self.get_user_apartment_review(apartment=apartment, user=self.request.user)
        if apartment_review:
            return "reviewapp/apartment_user_review.html"

        return self.template_name