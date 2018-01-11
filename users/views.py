from django.shortcuts import render
from users import forms
from users.models import User


# Create your views here.
def users_index(request):
    users = User.objects.order_by('last_name')
    users_dict = {"users_records": users}
    return render(request, "users/index.html", context=users_dict)


def index(request):
    return render(request, "index.html")


def user_registration(request):
    user_registration_form = forms.UserRegistrationForm()

    if request.method == "POST":
        user_registration_form = forms.UserRegistrationForm(request.POST)

        if user_registration_form.is_valid():

            user_registration_form.save(commit=True)

    return render(request,
                  "users/register.html",
                  {"user_registration_form": user_registration_form})

