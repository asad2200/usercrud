from django.views.generic import View, ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from user_app.models import UserModel
from django.shortcuts import get_object_or_404

from .forms import UserAddressForm, UserModelForm


class UserListView(ListView):
    """
        A ListView to display all users
    """

    model = UserModel
    context_object_name = "user_list"
    template_name = "user_app/user_list.html"


class UserDetailView(DetailView):
    """
        A DetailView to display user detail
    """

    model = UserModel
    template_name = "user_app/user_detail.html"


class UserCreateView(View):
    """
        A UserCreateView to create user and useraddress.
    """

    template_name = "user_app/user_form.html"

    def get_success_url(self):
        return reverse("user_app:user_list")

    def get(self, request, *args, **kwargs):
        context = {
            "user_form": UserModelForm(),
            "user_address_form": UserAddressForm(),
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        user_form = UserModelForm(request.POST, request.FILES)
        user_address_form = UserAddressForm(request.POST)
        if user_form.is_valid() and user_address_form.is_valid():
            user = user_form.save()
            user_address = user_address_form.save(commit=False)
            user_address.user = user
            user_address.save()
            return redirect(self.get_success_url())
        else:
            context = {
                "user_form": user_form,
                "user_address_form": user_address_form,
            }
            return render(request, self.template_name, context=context)


class UserUpdateView(View):
    """
        A UserUpdateView to create user and useraddress.
    """

    template_name = "user_app/user_form.html"

    def get_success_url(self):
        return reverse("user_app:user_list")

    def get(self, request, id, *args, **kwargs):
        user = get_object_or_404(UserModel, pk=id)
        context = {
            "user_form": UserModelForm(instance=user),
            "user_address_form": UserAddressForm(instance=user.user_address),
        }
        return render(request, self.template_name, context=context)

    def post(self, request, id, *args, **kwargs):
        user = get_object_or_404(UserModel, pk=id)
        user_form = UserModelForm(request.POST, request.FILES, instance=user)
        user_address_form = UserAddressForm(request.POST, instance=user.user_address)
        if user_form.is_valid() and user_address_form.is_valid():
            user_form.save()
            user_address_form.save()
            return redirect(self.get_success_url())
        else:
            context = {
                "user_form": user_form,
                "user_address_form": user_address_form,
            }
            return render(request, self.template_name, context=context)
