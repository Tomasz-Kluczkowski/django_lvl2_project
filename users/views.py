from django.shortcuts import render

from users.models import User


# Create your views here.
def users_index(request):
    users = User.objects.order_by('last_name')
    users_dict = {"users_records": users}
    return render(request, "users/index.html", context=users_dict)


def index(request):
    return render(request, "index.html")
