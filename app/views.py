from django.http import JsonResponse
from .models import Users


def all_users_view(request):
    all_users = list(Users.get_all_users().values())
    return JsonResponse({'all_users': all_users})
